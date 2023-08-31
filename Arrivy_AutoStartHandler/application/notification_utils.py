import logging
from datetime import datetime, timedelta
from django.utils import timezone
from application.files import *

def search_active_task_status_with_time_in_task_statuses_list(task_status_list, task_status_type, task_status_time):
    for status in task_status_list:
        if status.type == task_status_type and status.time > task_status_time and status.is_active == True:
            return status
    return None

def search_active_task_status_with_time_and_entity_in_task_statuses_list(task_status_list, task_status_type,
                                                                         task_status_time, entity_id):
    for status in task_status_list:
        if status.type == task_status_type and status.time > task_status_time \
                and status.is_active == True and entity_id in status.object_ids:
            return status
    return None


# For now, this function is being used in AUTO START/COMPLETE feature and for creating statuses for entity response to
# team notifications. Before, using this function else where go through its logic first.
def create_task_status(task, task_status, entity_id, is_company=False, recipient_ids=None):
    company_profile = CompanyProfile.by_user(task.owner).get()

    if not company_profile:
        logging.error("Company profile Not Found")
        return

    logging.info('entity_id: {}'.format(entity_id))
    company_id = task.owner.user_id
    user_key = task.owner.user_id
    pending_review_reminder_attempts = company_profile.pending_review_reminder_attempts
    task_id = task.get_id()
  
    object_ids = []
    if entity_id:
        object_ids.append(entity_id)

    logged_in_entity_permission_group, logged_in_entity_permission_group_id, is_time_reporting_feature_enabled = Util.get_entity_permission_group_name_and_id_for_time_reporting_feature(
        entity_id, is_company, company_profile=company_profile)

    # replace Booking Only permission group with scheduler group id to get scheduler available statuses for
    # Booking Only
    if logged_in_entity_permission_group_id == UserPermissionGroups.BOOKING_ONLY_PERMISSION_GROUP_ID:
        logged_in_entity_permission_group_id = UserPermissionGroups.SCHEDULER_PERMISSION_GROUP_ID
        logged_in_entity_permission_group = PermissionGroups.SCHEDULER

    statuses = None
    if hasattr(task, 'template') and task.template:
        # template = Template.get_by_id(task.template, parent=user_key)
        template = Template.objects.get(pk=task.template.id)
        if template:
            statuses = template.get_statuses(False, logged_in_entity_permission_group_id)
    print(statuses)
    task_status_time = task_status.get('time')
    task_status_time = task_status_time.replace(microsecond=0)
    task_status_time_original_iso_str = task_status_time.isoformat()
    task_status_type = task_status.get('type')
    task_status_title = task_status.get('title')
    task_status_extra_fields = task_status.get('extra_fields')
    task_status_color = task_status.get('color')
    reporter_name = task_status.get('reporter_name')
    reporter_id = task_status.get('reporter_id')
    
    updated_task_status_type = task_status_type
    if task_status_type == TaskStatusType.AUTO_COMPLETE:
        updated_task_status_type = TaskStatusType.COMPLETE
    elif task_status_type == TaskStatusType.AUTO_START:
        updated_task_status_type = TaskStatusType.STARTED
    
    print("1: ",updated_task_status_type)
    custom_message_template = None
    custom_message_template_name = ''
    status_to_be_used = None
    for status in statuses:
        if convert_taskstatus_to_type(status.get('type')) == updated_task_status_type:
            print("2: ",status.get('type'))
            status_to_be_used = status
            break

    if not status_to_be_used and updated_task_status_type in [TaskStatusType.STARTED, TaskStatusType.COMPLETE]:
        logging.info('The given status not found in the template. Using default status settings')
        for single_default_status in Status.DEFAULT_STATUSES:
            if updated_task_status_type == single_default_status.get('type_id'):
                status_to_be_used = single_default_status
                break

    template_status_id = status_to_be_used.get('id')

    shadow_key = get_shadow_key_from_task_key(task.id, task.owner)
    
    print(template_status_id)
    task_status_created = task.update_status(
        task_status_type,
        task_status_title,
        shadow_key,
        title=task_status_title,
        reporter_name=reporter_name,
        color=task_status_color,
        time=task_status_time,
        object_ids=object_ids,
        status=template_status_id,
        reporter_entity_id=entity_id,
        is_active=True
    )
    print("Task status created: ",task_status_created)
    task_status_id = task_status_created.get_id()
    body = ''
    
    event = Event.create(
        owner=User(company_id),
        type=convert_taskstatus_to_text(task_status_type) if task_status_type in [TaskStatusType.TASK_REJECTED,
                                                                                  TaskStatusType.TASK_ACCEPTED] else 'TASK_STATUS',
        object_id=task_id,
        object_type='TASK',
        subject_id=task_status_id,
        subject_type='TASK_STATUS',
        reporter_id=reporter_id,
        reporter_name=reporter_name,
        time=task_status_time,
        message=body
    )
    logging.info("Created event is: {}".format(event))

    if task_status_type == TaskStatusType.AUTO_START:
        Util.delete_task_status(task_id, company_id, TaskStatusType.AUTO_START_PENDING, True)

    elif task_status_type == TaskStatusType.AUTO_COMPLETE:
        Util.delete_task_status(task_id, company_id, TaskStatusType.AUTO_COMPLETE_PENDING, True)
