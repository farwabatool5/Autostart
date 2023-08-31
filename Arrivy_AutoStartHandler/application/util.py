from django.db.models import Q
import logging
from .exceptions import *
from .model.task import (
    TaskStatusType,
    Task
)

from .model.permission import (
    UserPermissionGroups, 
    PermissionGroups,
)
from application.files import *
class Util:

    @classmethod
    def check_if_integer(cls, key, value, log_error=True):
        try:
            convert_to_int = int(value)
        except:
            if log_error:
                logging.error(u"Key: {0}, does not contain a valid integer value. Value is: {1}".format(key, value))
            return False
        return True
    
    @classmethod
    def get_time_for_status_query(cls, statuses_list, task):
        # get latest task RESCHEDULED or NOTSTARTED status
        time_for_status_query = None
        for status in statuses_list:
            if status.type == TaskStatusType.RESCHEDULED or status.type == TaskStatusType.NOTSTARTED:
                time_for_status_query = status.time
                break

        if not time_for_status_query:
            logging.info(u'NOTSTARTED or RESCHEDULED status was not found on task. Using task created datetime as time_for_status_query. Task is: {}'.format(task))
            time_for_status_query = task.created

        if not time_for_status_query:
            logging.info(u'Task created time not found. Using task updated datetime as time_for_status_query. Task is: {}'.format(task))
            time_for_status_query = task.updated

        return time_for_status_query
    
    @classmethod
    def create_user_shadow_key(cls, user_id, user_shadow_count=1):
        if user_shadow_count == 1:
            return ndb.Key('UserShadow', user_id)
        elif user_shadow_count == 2:
            # For worker scheduling, Documents
            return ndb.Key('UserShadow2', user_id)
        elif user_shadow_count == 3:
            # For external integrations
            return ndb.Key('UserShadow3', user_id)
        elif user_shadow_count == 4:
            # For data fetch history
            return ndb.Key('UserShadow4', user_id)
        elif user_shadow_count == 5:
            # For documents history
            return ndb.Key('UserShadow5', user_id)
        elif user_shadow_count == 6:
            # For default inventory
            return ndb.Key('UserShadow6', user_id)
        elif user_shadow_count == 7:
            # For default supplies
            return ndb.Key('UserShadow7', user_id)
        elif user_shadow_count == 8:
            # For task inventory
            return ndb.Key('UserShadow8', user_id)
        elif user_shadow_count == 9:
            # For task supply
            return ndb.Key('UserShadow9', user_id)
        elif user_shadow_count == 10:
            # For task inventory label
            return ndb.Key('UserShadow10', user_id)
        elif user_shadow_count == 11:
            # For Task Backup
            return ndb.Key('UserShadow11', user_id)
        elif user_shadow_count == 12:
            # For Task Inventory History
            return ndb.Key('UserShadow12', user_id)
        elif user_shadow_count == 13:
            # For Task Draft
            return ndb.Key('UserShadow13', user_id)
        elif user_shadow_count == 14:
            # For Route Draft
            return ndb.Key('UserShadow14', user_id)
        elif user_shadow_count == 15:
            # For Linked Task
            return ndb.Key('UserShadow15', user_id)
        elif user_shadow_count == USER_SHADOW_COUNT_FOR_FORM_PARENT:
            # For Form
            return ndb.Key('UserShadow{}'.format(USER_SHADOW_COUNT_FOR_FORM_PARENT), user_id)
        elif user_shadow_count == USER_SHADOW_COUNT_FOR_FORM_SUBMISSION_PARENT:
            # For FormSubmission
            return ndb.Key('UserShadow{}'.format(USER_SHADOW_COUNT_FOR_FORM_SUBMISSION_PARENT), user_id)
        elif user_shadow_count == USER_SHADOW_COUNT_FOR_OAUTH_FLOW_PARENT:
            # For OAUTH flow
            return ndb.Key('UserShadow{}'.format(USER_SHADOW_COUNT_FOR_OAUTH_FLOW_PARENT), user_id)
        elif user_shadow_count == USER_SHADOW_COUNT_FOR_ROUTE_PLANNING_SNAPSHOT_METADATA:
            # For Route Planning Snapshot
            return ndb.Key('UserShadow{}'.format(USER_SHADOW_COUNT_FOR_ROUTE_PLANNING_SNAPSHOT_METADATA), user_id)
        elif user_shadow_count == USER_SHADOW_COUNT_FOR_ITEMS_TEMPLATE_PARENT:
            # For Items Template
            return ndb.Key('UserShadow{}'.format(USER_SHADOW_COUNT_FOR_ITEMS_TEMPLATE_PARENT), user_id)
        elif user_shadow_count == USER_SHADOW_COUNT_FOR_EXTERNAL_ITEMS:
            # For Items
            return ndb.Key('UserShadow{}'.format(USER_SHADOW_COUNT_FOR_EXTERNAL_ITEMS), user_id)
        elif user_shadow_count == USER_SHADOW_COUNT_FOR_SELF_SCHEDULING_BOOKING_PARENT:
            # For Self Scheduling Booking
            return ndb.Key('UserShadow{}'.format(USER_SHADOW_COUNT_FOR_SELF_SCHEDULING_BOOKING_PARENT), user_id)
        elif user_shadow_count == USER_SHADOW_COUNT_FOR_SELF_SCHEDULING_BOOKING_SLOT_PARENT:
            # For Self Scheduling Booking Slot
            return ndb.Key('UserShadow{}'.format(USER_SHADOW_COUNT_FOR_SELF_SCHEDULING_BOOKING_SLOT_PARENT), user_id)
        elif user_shadow_count == USER_SHADOW_COUNT_FOR_SELF_SCHEDULING_BOOKED_SLOT_PARENT:
            # For Self Scheduling Booked Slot
            return ndb.Key('UserShadow{}'.format(USER_SHADOW_COUNT_FOR_SELF_SCHEDULING_BOOKED_SLOT_PARENT), user_id)
        elif user_shadow_count == USER_SHADOW_COUNT_FOR_CHECKLIST_PARENT:
            # For CheckList
            return ndb.Key('UserShadow{}'.format(USER_SHADOW_COUNT_FOR_CHECKLIST_PARENT), user_id)
        elif user_shadow_count == USER_SHADOW_COUNT_FOR_TASK_CHECKLIST_PARENT:
            # For Task CheckList
            return ndb.Key('UserShadow{}'.format(USER_SHADOW_COUNT_FOR_TASK_CHECKLIST_PARENT), user_id)
        elif user_shadow_count == USER_SHADOW_COUNT_FOR_ASYNC_TASK_JOB_REFERENCE_PARENT:
            # For Async Task Job Reference
            return ndb.Key('UserShadow{}'.format(USER_SHADOW_COUNT_FOR_ASYNC_TASK_JOB_REFERENCE_PARENT), user_id)
        elif user_shadow_count == USER_SHADOW_COUNT_FOR_SELF_SCHEDULING_BOOKING_SLOT_RULE_PARENT:
            # For Booking Slot Rule
            return ndb.Key('UserShadow{}'.format(USER_SHADOW_COUNT_FOR_SELF_SCHEDULING_BOOKING_SLOT_RULE_PARENT), user_id)
        elif user_shadow_count == USER_SHADOW_COUNT_FOR_MOVERS_SUITE_VENDOR_CONNECT:
            # For Booking Slot Rule
            return ndb.Key('UserShadow{}'.format(USER_SHADOW_COUNT_FOR_MOVERS_SUITE_VENDOR_CONNECT), user_id)
        elif user_shadow_count == USER_SHADOW_COUNT_FOR_ORDER_PARENT:
            # For Order
            return ndb.Key('UserShadow{}'.format(USER_SHADOW_COUNT_FOR_ORDER_PARENT), user_id)
        elif user_shadow_count == USER_SHADOW_COUNT_FOR_STATUS_PRIORITIES:
            # For Status Priorities
            return ndb.Key('UserShadow{}'.format(USER_SHADOW_COUNT_FOR_STATUS_PRIORITIES), user_id)
        elif user_shadow_count == USER_SHADOW_COUNT_FOR_FORM_REMINDER_PARENT:
            # For Form Reminder
            return ndb.Key('UserShadow{}'.format(USER_SHADOW_COUNT_FOR_FORM_REMINDER_PARENT), user_id)
        elif user_shadow_count == USER_SHADOW_COUNT_FOR_MASTER_ITEMS:
            # For Master Items
            return ndb.Key('UserShadow{}'.format(USER_SHADOW_COUNT_FOR_MASTER_ITEMS_PARENT), user_id)
        elif user_shadow_count == USER_SHADOW_COUNT_FOR_ITEMS_LIST_PARENT:
            # For Items List
            return ndb.Key('UserShadow{}'.format(USER_SHADOW_COUNT_FOR_ITEMS_LIST_PARENT), user_id)
        elif user_shadow_count == USER_SHADOW_COUNT_FOR_CUSTOM_WEBHOOKS_PARENT:
            # For Custom Webhooks
            return ndb.Key('UserShadow{}'.format(USER_SHADOW_COUNT_FOR_CUSTOM_WEBHOOKS_PARENT), user_id)
        elif user_shadow_count == USER_SHADOW_COUNT_FOR_ACTION_CRON_CONFIG:
            # For Action Config
            return ndb.Key('UserShadow{}'.format(USER_SHADOW_COUNT_FOR_ACTION_CRON_CONFIG), user_id)
        elif user_shadow_count == USER_SHADOW_COUNT_FOR_ACTION_CRON_CONFIG_STATS:
            # For Action Config Stats
            return ndb.Key('UserShadow{}'.format(USER_SHADOW_COUNT_FOR_ACTION_CRON_CONFIG_STATS), user_id)
        elif user_shadow_count == USER_SHADOW_COUNT_FOR_CREW_AVAILABILITY_REQUEST_PARENT:
            # For Crew Availability Request
            return ndb.Key('UserShadow{}'.format(USER_SHADOW_COUNT_FOR_CREW_AVAILABILITY_REQUEST_PARENT), user_id)
        elif user_shadow_count == USER_SHADOW_COUNT_FOR_ASYNC_TASK_ROUTE_JOB_PARENT:
            # For Async Task Route Request
            return ndb.Key('UserShadow{}'.format(USER_SHADOW_COUNT_FOR_ASYNC_TASK_ROUTE_JOB_PARENT), user_id)
        elif user_shadow_count == USER_SHADOW_COUNT_FOR_ASYNC_TASK_ROUTE_JOB_REFERENCE_PARENT:
            # For Async Task Route Reference
            return ndb.Key('UserShadow{}'.format(USER_SHADOW_COUNT_FOR_ASYNC_TASK_ROUTE_JOB_REFERENCE_PARENT), user_id)
        elif user_shadow_count == USER_SHADOW_COUNT_FOR_CUSTOMER_TEMPLATE_PARENT:
            # For Customer Template Request
            return ndb.Key('UserShadow{}'.format(USER_SHADOW_COUNT_FOR_CUSTOMER_TEMPLATE_PARENT), user_id)
        elif user_shadow_count == USER_SHADOW_COUNT_FOR_TASK_QUERY:
            # For task queries request
            return ndb.Key('UserShadow{}'.format(USER_SHADOW_COUNT_FOR_TASK_QUERY), user_id)
        elif user_shadow_count == USER_SHADOW_COUNT_FOR_TASK_GROUP_QUERY:
            # For task queries request
            return ndb.Key('UserShadow{}'.format(USER_SHADOW_COUNT_FOR_TASK_GROUP_QUERY), user_id)
        elif user_shadow_count == USER_SHADOW_COUNT_FOR_COMPANY_DEFAULT_GROUP:
            # For task queries request
            return ndb.Key('UserShadow{}'.format(USER_SHADOW_COUNT_FOR_COMPANY_DEFAULT_GROUP), user_id)
        elif user_shadow_count == USER_SHADOW_COUNT_FOR_BOOKING_TASK_QUERY:
            # For task queries request
            return ndb.Key('UserShadow{}'.format(USER_SHADOW_COUNT_FOR_BOOKING_TASK_QUERY), user_id)
        elif user_shadow_count == USER_SHADOW_COUNT_FOR_BOOKING_OBJECT_RULES:
            # For task queries request
            return ndb.Key('UserShadow{}'.format(USER_SHADOW_COUNT_FOR_BOOKING_OBJECT_RULES), user_id)
        else:
            # Default Key
            return ndb.Key('UserShadow', user_id)

    @classmethod
    def get_entity_permission_group(cls, entity_id, is_company=False):
        if not entity_id:
            logging.error('entity_id not found')
            raise IncorrectParameterFormat

        logging.info('entity_id: {}'.format(entity_id))
        entity_permission_group = ''
        if not is_company:
            entity_permission_groups = UserPermission.get_entity_permission_groups(entity_id)
            for permission_group in entity_permission_groups:
                if permission_group.get('status'):
                    entity_permission_group = permission_group.get('title')
                    logging.info('Permission group of entity is {}'.format(entity_permission_group))
        else:
            logging.info('Permission group of entity is COMPANY')
            entity_permission_group = 'COMPANY'

        if not entity_permission_group:
            # A very rare case where a logged in user has no permission group. In that case we need to consider
            # him a Field Crew
            logging.info('Permission group not found for entity. Considering him Field Crew')
            entity_permission_group = 'Field Crew'

        return entity_permission_group
    

    @classmethod
    def get_entity_permission_group_name_and_id_for_time_reporting_feature(cls, entity_id, is_company=False,
                                                                           company_id=None, company_profile=None):

        # is_time_reporting_feature_enabled = cls.check_if_feature_is_enabled(TIME_REPORTING_FEATURE_NAME,
        #                                                                     company_id, company_profile)
        # remove-for temp testing
        is_time_reporting_feature_enabled = False
        if not is_time_reporting_feature_enabled:
            logging.info('Time reporting feature is disabled. Using default permission group i.e. field crew')
            logged_in_entity_permission_group = PermissionGroups.FIELD_CREW
            logged_in_entity_permission_group_id = UserPermissionGroups.DEFAULT_PERMISSION_GROUP_ID
        else:
            logged_in_entity_permission_group = cls.get_entity_permission_group(entity_id, is_company)
            logged_in_entity_permission_group_id = UserPermissionGroups.get_permission_id_using_permission_group_title(
                logged_in_entity_permission_group)
            if logged_in_entity_permission_group == 'COMPANY':
                logging.info('Logged in user has Company level access. Considering ADMIN permissions for him.')
                logged_in_entity_permission_group = PermissionGroups.ADMIN
                logged_in_entity_permission_group_id = UserPermissionGroups.ADMIN_PERMISSION_GROUP_ID

        return logged_in_entity_permission_group, logged_in_entity_permission_group_id, is_time_reporting_feature_enabled


    @classmethod
    def delete_task_status(cls, task_id, company_id, task_status_type, force_delete=False):
        task = Task.objects.get(pk=task_id)
        if not task:
            logging.info('Task not found')
            return

        # get all task statuses
        shadow = get_shadow_key_from_task_key(task.id, task.owner)
        shadow_key = shadow.id
        task_statuses = TaskStatusData.objects.filter(Q(task_shadow=shadow.id)).order_by('-time').all()
        time_for_status_query = cls.get_time_for_status_query(task_statuses, task)

        # get latest status, which was reported after task RESCHEDULED or NOTSTARTED
        status_to_be_deleted = TaskStatusData.objects.filter(Q(type=task_status_type) & 
                                                             Q(time__gt=time_for_status_query) &
                                                             Q(task_shadow=shadow_key)).order_by('-time').get()
        if not status_to_be_deleted:
            logging.info('Status not found')
            return
        if not force_delete and not statuses_meta_data.meta_data[status_to_be_deleted.type]['is_deletable']:
            logging.info('Can not delete status reported by ARRIVY')
            return

        setattr(status_to_be_deleted, 'is_active', False)
        status_to_be_deleted.save()

