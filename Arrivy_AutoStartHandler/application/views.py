from application.files import *
from django.shortcuts import render
from django.http import HttpResponse
from django.db.models import Q
from django.utils import timezone
import logging
from datetime import datetime, timedelta
import requests

TASK_AUTO_START_DELAY_TIME = config.get('TASK_AUTO_START_DELAY_TIME_IN_MINUTES', 0) * 60
TASK_AUTO_COMPLETE_DELAY_TIME = config.get('TASK_AUTO_COMPLETE_DELAY_TIME_IN_MINUTES', 0) * 60
TASK_STATUS_COLOR = '#44a7f1'
ARRIVY_REPORTER_ID = config.get('ARRIVY_REPORTER_ID')
ARRIVY_REPORTER_NAME = config.get('ARRIVY_REPORTER_NAME')

# Create your views here.
def entity_arrival(entity_id):
    logging.info('Entity Arrival Handler')
    logging.info('Entity ID: {}'.format(entity_id))

    if not entity_id:
        logging.error("Entity ID doesn't exist")
        return

    entity_id = int(entity_id)
    entity = Entity.objects.get(pk=entity_id)
    logging.info("Entity in entity_arrival is: {}".format(entity))
    if not entity:
        logging.error("Entity Not Found")
        return

    is_company = entity.is_default
    logging.info('Company ID: {}'.format(entity.owner))

    user_key = entity.owner    

    # fetch tasks for this entity in +- 12 hours time window, which are not unscheduled and does not have any
    # task termination status as latest status
    # remove
    date_format = '%Y-%m-%d %H:%M:%S'  # Specify the format

    from_date = datetime.now() - timedelta(hours=12)
    to_date = datetime.now() + timedelta(hours=12)
    # remove
    from_date = datetime.strptime('2023-08-30 11:08:53', date_format)
    to_date = datetime.strptime('2023-08-31 11:08:53', date_format)
    # Convert local datetime to UTC
    from_date = from_date.astimezone(timezone.utc)
    to_date = to_date.astimezone(timezone.utc)
    logging.info('from date: {}'.format(from_date))
    logging.info('to date: {}'.format(to_date))
    # ---
    tasks_query = Task.objects.filter(Q(start_datetime__gte = from_date) & Q(start_datetime__lte = to_date)
                                      & Q(owner=user_key) & Q(unscheduled=False) & 
                                      Q(entity_ids__contains=[entity_id]) & Q(template_type__in=QUERY_FILTER_FOR_AUTO_START_COMPLETE))
    logging.info("task query is {}".format(tasks_query))

    tasks = tasks_query.all()

    if not tasks:
        logging.info(u"No task(s) found in 24 hours time window, for entity: {}".format(entity.name))
        return
    
    filtered_tasks = []
    filtered_task_ids = []
    for task in tasks:
        task_shadow = TaskShadow.fetch_by_task(task)
        if not statuses_meta_data.meta_data[task_shadow.status]['is_terminal']:
            filtered_tasks.append(task)
            filtered_task_ids.append(task.get_id())

    logging.info(u"Task(s) Found in 24 hours time window: {}".format(filtered_task_ids))

    # from nearest tasks, get all task for which enroute was marked and entity has not yet arrived
    # remove
    nearest_tasks = filtered_tasks
    enroute_tasks_on_which_entity_has_not_arrived = []
    for task in nearest_tasks:
        shadow = get_shadow_key_from_task_key(task.id, task.owner)
        shadow_key = shadow.id
        logging.info("shadow key is: {}".format(shadow_key))
        task_statuses = TaskStatusData.objects.filter(task_shadow=shadow_key).order_by('-time')
        # remove
        logging.info("task statuses are: {}".format(task_statuses))
        time_for_status_query = Util.get_time_for_status_query(task_statuses, task)
        logging.info(u'Reference time for statuses query: {}'.format(time_for_status_query))
        
        enroute_status = search_active_task_status_with_time_in_task_statuses_list(task_statuses,
                                                                                   TaskStatusType.ENROUTE,
                                                                                   time_for_status_query)

        arrived_status = search_active_task_status_with_time_and_entity_in_task_statuses_list(task_statuses,
                                                                                              TaskStatusType.ARRIVED,
                                                                                              time_for_status_query,
                                                                                              entity_id)

        departed_status = search_active_task_status_with_time_and_entity_in_task_statuses_list(task_statuses,
                                                                                               TaskStatusType.DEPARTED,
                                                                                               time_for_status_query,
                                                                                               entity_id)
    
        # handle case here when entity DEPARTED from task and returned before AUTO_COMPLETE/COMPLETE was marked
        auto_complete_delay_time = None
        time_difference_in_secs = None
        if enroute_status and arrived_status and departed_status:
            # if task has template check auto-start-complate not disabled
            if hasattr(task, 'template') and task.template:
                template = Template.objects.get(pk=task.template.id)        
                if not template:
                    logging.info('Task Template not found')
                    continue
                if not hasattr(template, 'disable_auto_start_complete'):
                    # default time for auto complete delay
                    auto_complete_delay_time = TASK_AUTO_COMPLETE_DELAY_TIME
                elif template.disable_auto_start_complete:
                    logging.info('Auto start complete feature was disabled on task template')
                    continue
                else:
                    # convert mins to seconds
                    auto_complete_delay_time = template.auto_complete_delay_time * 60
            else:
                # task has no template, get from company type
                company_profile = CompanyProfile.by_user(task.owner.user_id).get()
                if not company_profile:
                    logging.error('User Profile Not Found')
                    continue
                company_template = company_profile.get_template_based_on_company_type(company_profile.company_type)
                if company_template['disable_auto_start_complete']:
                    logging.info('Auto Start Complete feature was disabled on Default template present in USER PROFILE')
                    continue
                else:
                    auto_complete_delay_time = company_template['auto_complete_delay_time'] * 60

            time_difference = datetime.now().astimezone(timezone.utc) - departed_status.time
            time_difference_in_secs = int(time_difference.total_seconds())

        if (enroute_status and not arrived_status) or \
                (enroute_status and auto_complete_delay_time and time_difference_in_secs
                 and time_difference_in_secs < auto_complete_delay_time):
            enroute_tasks_on_which_entity_has_not_arrived.append(task)

    if not enroute_tasks_on_which_entity_has_not_arrived:
        logging.info(u'No nearest enroute task(s) found on which Entity: {}, has not arrived already'.format(entity.name))
        return

    logging.info(u'Nearest Enroute Task(s) on which Entity: {0}, has not arrived already are: {1}'
                 .format(entity.name, enroute_tasks_on_which_entity_has_not_arrived))
    
    # if more than one tasks found for which entity has not arrived
    enroute_status_time = datetime.now().astimezone(timezone.utc)
    task_with_earliest_enroute_status = None
    if len(enroute_tasks_on_which_entity_has_not_arrived) > 1:
        for task in enroute_tasks_on_which_entity_has_not_arrived:
            shadow = get_shadow_key_from_task_key(task.id, task.owner)
            # latest enroute status if more than one are present
            enroute_status = TaskStatusData.objects.filter(Q(type=TaskStatusType.ENROUTE) & 
                                                           Q(is_active=True) &Q(task_shadow=shadow.id)).order_by('-time')
            enroute_status = enroute_status.get()

            if enroute_status.time <= enroute_status_time:
                enroute_status_time = enroute_status.time
                task_with_earliest_enroute_status = task
            
    else:
        task_with_earliest_enroute_status = enroute_tasks_on_which_entity_has_not_arrived[0]
    
    # mark entity ARRIVED on filtered task
    logging.info(u'Task for which entity is going to be marked as ARRIVED/RETURNED is: {}'
                 .format(task_with_earliest_enroute_status))

    mark_entity_arrived_on_task = task_with_earliest_enroute_status
    
    if hasattr(mark_entity_arrived_on_task, 'template') and mark_entity_arrived_on_task.template:
        template = Template.get_by_id(mark_entity_arrived_on_task.template.id, user_key)
        if not template:
            logging.info('Task Template not found')
            return
        if not hasattr(template, 'disable_auto_start_complete'):
            # default time for auto start/complete delay
            auto_start_delay_time = TASK_AUTO_START_DELAY_TIME
            auto_complete_delay_time = TASK_AUTO_COMPLETE_DELAY_TIME
        elif template.disable_auto_start_complete:
            logging.info('Auto start complete feature was disabled on task template')
            return
        else:
            # convert mins to seconds
            auto_start_delay_time = template.auto_start_delay_time * 60
            auto_complete_delay_time = template.auto_complete_delay_time * 60

    else:
        company_profile = CompanyProfile.by_user(mark_entity_arrived_on_task.owner).get()
        if not company_profile:
            logging.error('User Profile Not Found')
            return
        company_template = company_profile.get_template_based_on_company_type(company_profile.company_type)
        if company_template['disable_auto_start_complete']:
            logging.info('Auto Start Complete feature was disabled on Default template present in USER PROFILE')
            return
        else:
            auto_start_delay_time = company_template['auto_start_delay_time'] * 60
            auto_complete_delay_time = company_template['auto_complete_delay_time'] * 60

    task_key = mark_entity_arrived_on_task.id
    shadow = get_shadow_key_from_task_key(task_key, mark_entity_arrived_on_task.owner)
    shadow_key = shadow.id
    
    task_statuses = TaskStatusData.objects.filter(task_shadow=shadow_key).order_by('-time').all()
    time_for_status_query = Util.get_time_for_status_query(task_statuses, mark_entity_arrived_on_task)
    logging.info(u'Reference time for statuses query: {}'.format(time_for_status_query))

    arrived_status = search_active_task_status_with_time_in_task_statuses_list(task_statuses, TaskStatusType.ARRIVED,
                                                                               time_for_status_query)

    entitys_arrived_status = search_active_task_status_with_time_and_entity_in_task_statuses_list(task_statuses,
                                                                                                  TaskStatusType.ARRIVED,
                                                                                                  time_for_status_query,
                                                                                                  entity_id)

    entitys_departed_status = search_active_task_status_with_time_and_entity_in_task_statuses_list(task_statuses,
                                                                                                   TaskStatusType.DEPARTED,
                                                                                                   time_for_status_query,
                                                                                                   entity_id)

    if entitys_arrived_status and entitys_departed_status:
        entitys_returned_status = search_active_task_status_with_time_and_entity_in_task_statuses_list(task_statuses,
                                                                                                       TaskStatusType.RETURNED,
                                                                                                       time_for_status_query,
                                                                                                       entity_id)
        # mark RETURNED status only once after DEPARTED status
        if entitys_returned_status and entitys_returned_status.time > entitys_departed_status.time:
            logging.info(u"Entity: {}, has already returned at customer's location".format(entity.name))
            return

        time_difference = datetime.now().astimezone(timezone.utc) - entitys_departed_status.time
        time_difference_in_secs = int(time_difference.total_seconds())
        if time_difference_in_secs < auto_complete_delay_time:
            logging.info(u'Creating RETURNED status for entity: {0}, on task: {1}'.format(entity.name,
                                                                                         mark_entity_arrived_on_task))
            time = datetime.now().astimezone(timezone.utc)
            message = entity.name + " has returned at customer's location"
            task_status_extra_fields = {'visible_to_customer': False, 'notes': message}
            task_status_type = TaskStatusType.RETURNED
            task_status_title = 'RETURNED'
            task_status = {
                'time': time,
                'type': task_status_type,
                'title': task_status_title,
                'extra_fields': task_status_extra_fields,
                'reporter_id': ARRIVY_REPORTER_ID,
                'reporter_name': ARRIVY_REPORTER_NAME,
                'color': TASK_STATUS_COLOR
            }
            create_task_status(mark_entity_arrived_on_task, task_status, entity_id, is_company)
            # task_statuses = TaskStatusData.query(ancestor=shadow_key).order(-TaskStatusData.time).fetch()

        all_entities_returned = True
        for entity_id_in_task in mark_entity_arrived_on_task.entity_ids:
            entity = Entity.get_by_id(entity_id_in_task)
            if not entity:
                logging.info("Entity Not Found against entity_id: {}, present in task.".format(entity_id_in_task))
                continue
            returned_status = search_active_task_status_with_time_and_entity_in_task_statuses_list(task_statuses,
                                                                                                   TaskStatusType.RETURNED,
                                                                                                   time_for_status_query,
                                                                                                   entity_id_in_task)

            if not returned_status:
                logging.info(u"Entity: {}, did not returned at customer's location".format(entity.name))
                all_entities_returned = False
                break

        if all_entities_returned:
            # if all entities returned, delete AUTO_COMPLETE_PENDING status
            logging.info("All task assignee's returned back, deleting AUTO COMPLETE PENDING status")
            Util.delete_task_status(mark_entity_arrived_on_task.get_id(), mark_entity_arrived_on_task.owner,
                                    TaskStatusType.AUTO_COMPLETE_PENDING, True)

        return

    time = datetime.now().astimezone(timezone.utc)
    message = entity.name + " has arrived at customer's location"
    task_status_extra_fields = {'visible_to_customer': False, 'notes': message}
    task_status_type = TaskStatusType.ARRIVED
    task_status_title = 'ARRIVED'
    task_status = {
        'time': time,
        'type': task_status_type,
        'title': task_status_title,
        'extra_fields': task_status_extra_fields,
        'reporter_id': ARRIVY_REPORTER_ID,
        'reporter_name': ARRIVY_REPORTER_NAME,
        'color': TASK_STATUS_COLOR
    }
    logging.info(u'Creating ARRIVED status for entity: {}, on task: {}'.format(entity.name,
                                                                               mark_entity_arrived_on_task))
    create_task_status(mark_entity_arrived_on_task, task_status, entity_id, is_company)
    
    # if first ARRIVED status was marked on task
    if not arrived_status:
        # check if task was already started
        try:
            start_status = TaskStatusData.objects.filter(
                Q(type=TaskStatusType.AUTO_START) | Q(type=TaskStatusType.STARTED),
                is_active=True,
                time__gt=time_for_status_query,
                task_shadow=shadow_key
            ).order_by('-time').first()
        except TaskStatusData.DoesNotExist:
            start_status = None

        if start_status:
            logging.info('Task has already started. AUTO_START_PENDING will not be triggered.')
            return

        logging.info(u'Creating AUTO_START_PENDING status on task : {}'.format(mark_entity_arrived_on_task))
        time = datetime.now().astimezone(timezone.utc) + timedelta(seconds=2)
        auto_start_time = datetime.now().astimezone(timezone.utc) + timedelta(seconds=auto_start_delay_time)
        message = "Task will be marked started at "
        task_status_extra_fields = {'visible_to_customer': False, 'notes': message,
                                    'auto_start_time': auto_start_time.isoformat()}
        task_status_type = TaskStatusType.AUTO_START_PENDING
        task_status_title = 'AUTO START PENDING'
        task_status = {
            'time': time,
            'type': task_status_type,
            'title': task_status_title,
            'extra_fields': task_status_extra_fields,
            'reporter_id': ARRIVY_REPORTER_ID,
            'reporter_name': ARRIVY_REPORTER_NAME,
            'color': TASK_STATUS_COLOR
        }
        create_task_status(mark_entity_arrived_on_task, task_status, entity_id, is_company)
        logging.info("Auto Start Pending Status Created.")
        
        url = 'http://localhost:8080/task_auto_start/'
        data = {
            'task_id': mark_entity_arrived_on_task.id,
            'entity_id': entity_id
        }
        print(data)
        # Make the HTTP request
        requests.post(url, data=data)


def task_auto_start(request):
    # This handler is called by taskqueue and taskqueues always expect response code 2xx,
    # other wise they will keep on retrying a failed task.
    # We are using error code 202 here because we don't want task queues to keep on retrying this specific task.
    # As this task already contains such information which will not be available/corrected in next calls as well.
    task_id = request.POST.get('task_id')
    entity_id = request.POST.get('entity_id')

    logging.info('Task Auto Start Handler')
    if not Util.check_if_integer('task_id', task_id):
        return request.message({}, 202, message="INVALID_INPUT", description="Invalid task_id")
    task_id = int(task_id)
    if not Util.check_if_integer('entity_id', entity_id):
        return request.message({}, 202, message="INVALID_INPUT", description="Invalid entity_id")
    entity_id = int(entity_id)

    logging.info('Entity ID: {}'.format(entity_id))
    logging.info('Task ID: {}'.format(task_id))
    
    entity = Entity.objects.get(pk=entity_id)
    if not entity:
        logging.error("Entity Not Found")
        return request.message({}, 202, message="Entity Not Found", description="Entity Not Found")

    is_company = entity.is_default
    logging.info('Company ID: {}'.format(entity.owner))

    task = Task.objects.get(pk=task_id)
    if not task:
        logging.error('Task not found')
        return request.message({}, 202, message="Task not found", description="Task not found")

    logging.info(u'Task: {}'.format(task))
    shadow_key = get_shadow_key_from_task_key(task.id, task.owner)
    task_shadow = TaskShadow.fetch_by_task(task)
    # check if any task termination status was reported on task or not
    if statuses_meta_data.meta_data[task_shadow.status]['is_terminal']:
        logging.info(u'Task has already marked with one of the task termination status i.e. {}'.format(task_shadow.status_title))
        return request.message({}, 202, message="Task has already marked with one of the task termination status",
                            description="Task has already marked with one of the task termination status")

    task_statuses = TaskStatusData.objects.filter(task_shadow=shadow_key).order_by('-time').all()
    time_for_status_query = Util.get_time_for_status_query(task_statuses, task)
    logging.info(u'Reference time for statuses query: {}'.format(time_for_status_query))

    # check if entity which triggered AUTO_START was actually ARRIVED or not
    arrived_status = search_active_task_status_with_time_and_entity_in_task_statuses_list(task_statuses,
                                                                                          TaskStatusType.ARRIVED,
                                                                                          time_for_status_query,
                                                                                          entity_id)
    if not arrived_status:
        logging.info(u'Entity: {}, has not arrived on task.'.format(entity.name))
        return request.message({}, 202, message="Entity has not arrived on task",
                            description="Entity has not arrived on task")

    departed_status = search_active_task_status_with_time_and_entity_in_task_statuses_list(task_statuses,
                                                                                           TaskStatusType.DEPARTED,
                                                                                           time_for_status_query,
                                                                                           entity_id)

    try:
        start_status = TaskStatusData.objects.filter(Q(type=TaskStatusType.AUTO_START) | 
                                                    Q(type=TaskStatusType.STARTED),
                                                    is_active = True,
                                                    time__gt = time_for_status_query,
                                            task_shadow=shadow_key).order_by('-time').get()
    except TaskStatusData.DoesNotExist:
        start_status = None

    if departed_status:
        logging.info(u"Entity: {}, has already DEPARTED from the customer's location".format(entity.name))
        return request.message({}, 202, message="Entity has already DEPARTED from the customer's location",
                            description="Entity has already DEPARTED from the customer's location")

    if start_status:
        logging.info('Task has already marked STARTED or AUTO_START')
        return request.message({}, 202, message="Task has already marked STARTED or AUTO_START",
                            description="Task has already marked STARTED or AUTO_START")

    auto_start_pending_status = search_active_task_status_with_time_in_task_statuses_list(task_statuses, TaskStatusType.AUTO_START_PENDING,
                                                                                          time_for_status_query)

    if not auto_start_pending_status:
        logging.info('No Auto_Start_Pending status was found on task')
        return request.message({}, 202, message="No Auto_Start_Pending status was found on task",
                            description="No Auto_Start_Pending status was found on task")

    # report AUTO_START on task
    logging.info(u'Creating AUTO_START status for task: {}'.format(task))
    task_status_time = datetime.now()
    task_status_extra_fields = {'visible_to_customer': True}
    task_status_type = TaskStatusType.AUTO_START
    task_status_title = 'AUTO START'
    task_status = {
        'time': task_status_time,
        'type': task_status_type,
        'title': task_status_title,
        'extra_fields': task_status_extra_fields,
        'reporter_id': ARRIVY_REPORTER_ID,
        'reporter_name': ARRIVY_REPORTER_NAME,
        'color': TASK_STATUS_COLOR
    }
    create_task_status(task, task_status, entity_id, is_company)
    return HttpResponse('Success')




def EntityArrivedHandler(request):
    data = request.POST
    entity_id = data.get('entity_id')
    entity_arrival(entity_id)
    return HttpResponse("Response sent")    