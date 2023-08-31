from django.db import models
from django.contrib.postgres.fields import ArrayField

from application.files import *
import logging

class StatusTriggerName:
    ALWAYS = 'ALWAYS'
    FORM_COMPLETE = 'FORM_COMPLETE'
    FORM_SAVE = 'FORM_SAVE'
    STATUS = 'STATUS'

    @classmethod
    def get_all_status_trigger_names(cls):
        return [cls.ALWAYS, cls.FORM_COMPLETE, cls.FORM_SAVE, cls.STATUS]

class StatusTriggerType:
    ALWAYS = 1000
    FORM_COMPLETE = 1001
    FORM_SAVE = 1002
    STATUS = 1003

    @classmethod
    def get_all_status_trigger_types(cls):
        return [cls.ALWAYS, cls.FORM_COMPLETE, cls.FORM_SAVE, cls.STATUS]
    
def convert_status_trigger_type_to_status_trigger_name(status_trigger_type):
    if status_trigger_type == StatusTriggerType.ALWAYS:
        return StatusTriggerName.ALWAYS
    elif status_trigger_type == StatusTriggerType.FORM_COMPLETE:
        return StatusTriggerName.FORM_COMPLETE
    elif status_trigger_type == StatusTriggerType.FORM_SAVE:
        return StatusTriggerName.FORM_SAVE
    elif status_trigger_type == StatusTriggerType.STATUS:
        return StatusTriggerName.STATUS
    

class TimeReportRecipientCategoryType:
    REPORTER = 1000
    ALL_ASSIGNEES = 1001
    MANUALLY_SELECTED_ASSIGNEES = 1002

    @classmethod
    def get_all_time_report_recipient_category_types(cls):
        return [cls.REPORTER, cls.ALL_ASSIGNEES, cls.MANUALLY_SELECTED_ASSIGNEES]

class TimeReportCategoryType:
    TRAVEL_HOURS = 1000
    WORK_HOURS = 1001
    NON_WORK_HOURS = 1002
    NOT_APPLICABLE = 1003
    RE_ENGAGE_PREVIOUS_STATUS = 1004

def convert_time_report_recipient_category_name_to_time_report_recipient_category_type(
        time_report_recipient_category_name):
    if time_report_recipient_category_name == TimeReportRecipientCategoryName.REPORTER:
        return TimeReportRecipientCategoryType.REPORTER
    elif time_report_recipient_category_name == TimeReportRecipientCategoryName.ALL_ASSIGNEES:
        return TimeReportRecipientCategoryType.ALL_ASSIGNEES
    elif time_report_recipient_category_name == TimeReportRecipientCategoryName.MANUALLY_SELECTED_ASSIGNEES:
        return TimeReportRecipientCategoryType.MANUALLY_SELECTED_ASSIGNEES

def convert_time_report_category_name_to_time_report_category_type(time_report_category_name):
    if time_report_category_name == TimeReportCategoryName.TRAVEL_HOURS:
        return TimeReportCategoryType.TRAVEL_HOURS
    elif time_report_category_name == TimeReportCategoryName.WORK_HOURS:
        return TimeReportCategoryType.WORK_HOURS
    elif time_report_category_name == TimeReportCategoryName.NON_WORK_HOURS:
        return TimeReportCategoryType.NON_WORK_HOURS
    elif time_report_category_name == TimeReportCategoryName.NOT_APPLICABLE:
        return TimeReportCategoryType.NOT_APPLICABLE
    elif time_report_category_name == TimeReportCategoryName.RE_ENGAGE_PREVIOUS_STATUS:
        return TimeReportCategoryType.RE_ENGAGE_PREVIOUS_STATUS

class TimeReportRecipientCategoryName:
    REPORTER = 'REPORTER'
    ALL_ASSIGNEES = 'ALL_ASSIGNEES'
    MANUALLY_SELECTED_ASSIGNEES = 'MANUALLY_SELECTED_ASSIGNEES'

    @classmethod
    def get_all_time_report_recipient_category_names(cls):
        return [cls.REPORTER, cls.ALL_ASSIGNEES, cls.MANUALLY_SELECTED_ASSIGNEES]

class TimeReportCategoryName:
    TRAVEL_HOURS = 'TRAVEL_HOURS'
    WORK_HOURS = 'WORK_HOURS'
    NON_WORK_HOURS = 'NON_WORK_HOURS'
    NOT_APPLICABLE = 'NOT_APPLICABLE'
    RE_ENGAGE_PREVIOUS_STATUS = 'RE_ENGAGE_PREVIOUS_STATUS'

    @classmethod
    def get_all_time_report_category_names(cls):
        return [cls.TRAVEL_HOURS, cls.WORK_HOURS, cls.NON_WORK_HOURS, cls.NOT_APPLICABLE, cls.RE_ENGAGE_PREVIOUS_STATUS]


DEFAULT_TIME_REPORTING_SETTINGS_ON_THE_BASIS_OF_TASK_STATUS_TYPE = {
    TaskStatusType.ENROUTE: {
        'enable_time_reporting': True,
        'mark_assignees_as': convert_taskstatus_to_text(TaskStatusType.CLOCK_IN),
        'time_reporting_applies_to': TimeReportRecipientCategoryName.ALL_ASSIGNEES,
        'categorize_reported_time_as': TimeReportCategoryName.TRAVEL_HOURS
    },
    TaskStatusType.STARTED: {
        'enable_time_reporting': True,
        'mark_assignees_as': convert_taskstatus_to_text(TaskStatusType.CLOCK_IN),
        'time_reporting_applies_to': TimeReportRecipientCategoryName.ALL_ASSIGNEES,
        'categorize_reported_time_as': TimeReportCategoryName.WORK_HOURS
    },
    TaskStatusType.AUTO_START: {
        'enable_time_reporting': True,
        'mark_assignees_as': convert_taskstatus_to_text(TaskStatusType.CLOCK_IN),
        'time_reporting_applies_to': TimeReportRecipientCategoryName.ALL_ASSIGNEES,
        'categorize_reported_time_as': TimeReportCategoryName.WORK_HOURS
    },
    TaskStatusType.COMPLETE: {
        'enable_time_reporting': True,
        'mark_assignees_as': convert_taskstatus_to_text(TaskStatusType.CLOCK_OUT),
        'time_reporting_applies_to': TimeReportRecipientCategoryName.ALL_ASSIGNEES,
        'categorize_reported_time_as': TimeReportCategoryName.NOT_APPLICABLE
    },
    TaskStatusType.AUTO_COMPLETE: {
        'enable_time_reporting': True,
        'mark_assignees_as': convert_taskstatus_to_text(TaskStatusType.CLOCK_OUT),
        'time_reporting_applies_to': TimeReportRecipientCategoryName.ALL_ASSIGNEES,
        'categorize_reported_time_as': TimeReportCategoryName.NOT_APPLICABLE
    },
    TaskStatusType.DAY_START: {
        'enable_time_reporting': True,
        'mark_assignees_as': convert_taskstatus_to_text(TaskStatusType.CLOCK_IN),
        'time_reporting_applies_to': TimeReportRecipientCategoryName.ALL_ASSIGNEES,
        'categorize_reported_time_as': TimeReportCategoryName.WORK_HOURS
    },
    TaskStatusType.DAY_COMPLETE: {
        'enable_time_reporting': True,
        'mark_assignees_as': convert_taskstatus_to_text(TaskStatusType.CLOCK_OUT),
        'time_reporting_applies_to': TimeReportRecipientCategoryName.ALL_ASSIGNEES,
        'categorize_reported_time_as': TimeReportCategoryName.NOT_APPLICABLE
    },
    TaskStatusType.CLOCK_IN: {
        'enable_time_reporting': True,
        'mark_assignees_as': convert_taskstatus_to_text(TaskStatusType.CLOCK_IN),
        'time_reporting_applies_to': TimeReportRecipientCategoryName.ALL_ASSIGNEES,
        'categorize_reported_time_as': TimeReportCategoryName.WORK_HOURS
    },
    TaskStatusType.CLOCK_OUT: {
        'enable_time_reporting': True,
        'mark_assignees_as': convert_taskstatus_to_text(TaskStatusType.CLOCK_OUT),
        'time_reporting_applies_to': TimeReportRecipientCategoryName.ALL_ASSIGNEES,
        'categorize_reported_time_as': TimeReportCategoryName.NOT_APPLICABLE
    }
}


class Status(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=255)
    description = models.TextField(null=True)
    TYPE_CHOICES = [
        TaskStatusType.ENROUTE,
        TaskStatusType.STARTED,
        TaskStatusType.COMPLETE,
        TaskStatusType.CANCELLED,
        TaskStatusType.EXCEPTION,
        TaskStatusType.PREPARING,
        TaskStatusType.READYFORPICKUP,
        TaskStatusType.CONFIRMED,
        TaskStatusType.CUSTOMER_EXCEPTION,
        TaskStatusType.BOOKING_CANCELLED,
        TaskStatusType.RECOMMENDED,
        TaskStatusType.CUSTOMER_SIGNATURE,
        TaskStatusType.EXTRA_TIME,
        TaskStatusType.ON_HOLD,
        TaskStatusType.MOVING_TO_STORAGE,
        TaskStatusType.IN_STORAGE,
        TaskStatusType.OUT_OF_STORAGE,
        TaskStatusType.IN_TRANSIT,
        TaskStatusType.PICKING_UP,
        TaskStatusType.ORDER,
        TaskStatusType.SKIP,
        TaskStatusType.LAUNCH_DOCUMENT,
        TaskStatusType.CHECKINVENTORY,
        TaskStatusType.CHECKSUPPLIES,
        TaskStatusType.TASK_REJECTED,
        TaskStatusType.TASK_ACCEPTED,
        TaskStatusType.DAY_START,
        TaskStatusType.DAY_COMPLETE,
        TaskStatusType.CLOCK_IN,
        TaskStatusType.CLOCK_OUT,
        TaskStatusType.PROCESS_PAYMENT,
        TaskStatusType.MILESTONE,
        TaskStatusType.INVOICE_GENERATED,
        TaskStatusType.PAYMENT_MADE,
        TaskStatusType.CLOSED,
        TaskStatusType.INTEGRATION
    ]
    type = models.IntegerField(choices=[(x, x) for x in TYPE_CHOICES])
    # integration_info_json = models.JSONField()

    DEFAULT_STATUSES = [
        {
            'type_id': TaskStatusType.ENROUTE,
            'type': convert_taskstatus_to_text(TaskStatusType.ENROUTE),
            'title': 'On our way',
            'color': '#6aa3d7',
            'description': 'On the way to the job/customer location',
            'visible_to_customer': True,
            'enable_time_reporting': DEFAULT_TIME_REPORTING_SETTINGS_ON_THE_BASIS_OF_TASK_STATUS_TYPE.get(
                TaskStatusType.ENROUTE).get('enable_time_reporting'),
            'mark_assignees_as': DEFAULT_TIME_REPORTING_SETTINGS_ON_THE_BASIS_OF_TASK_STATUS_TYPE.get(
                TaskStatusType.ENROUTE).get('mark_assignees_as'),
            'time_reporting_applies_to': DEFAULT_TIME_REPORTING_SETTINGS_ON_THE_BASIS_OF_TASK_STATUS_TYPE.get(
                TaskStatusType.ENROUTE).get('time_reporting_applies_to'),
            'categorize_reported_time_as': DEFAULT_TIME_REPORTING_SETTINGS_ON_THE_BASIS_OF_TASK_STATUS_TYPE.get(
                TaskStatusType.ENROUTE).get('categorize_reported_time_as')
        },
        {
            'type_id': TaskStatusType.STARTED,
            'type': convert_taskstatus_to_text(TaskStatusType.STARTED),
            'title': 'Start',
            'color': '#2ee7fb',
            'description': 'The task has been started.',
            'visible_to_customer': True,
            'enable_time_reporting': DEFAULT_TIME_REPORTING_SETTINGS_ON_THE_BASIS_OF_TASK_STATUS_TYPE.get(
                TaskStatusType.STARTED).get('enable_time_reporting'),
            'mark_assignees_as': DEFAULT_TIME_REPORTING_SETTINGS_ON_THE_BASIS_OF_TASK_STATUS_TYPE.get(
                TaskStatusType.STARTED).get('mark_assignees_as'),
            'time_reporting_applies_to': DEFAULT_TIME_REPORTING_SETTINGS_ON_THE_BASIS_OF_TASK_STATUS_TYPE.get(
                TaskStatusType.STARTED).get('time_reporting_applies_to'),
            'categorize_reported_time_as': DEFAULT_TIME_REPORTING_SETTINGS_ON_THE_BASIS_OF_TASK_STATUS_TYPE.get(
                TaskStatusType.STARTED).get('categorize_reported_time_as')
        },
        {
            'type_id': TaskStatusType.COMPLETE,
            'type': convert_taskstatus_to_text(TaskStatusType.COMPLETE),
            'title': 'Complete',
            'color': '#5fe23f',
            'description': 'Mark a task as complete.',
            'visible_to_customer': True,
            'enable_time_reporting': DEFAULT_TIME_REPORTING_SETTINGS_ON_THE_BASIS_OF_TASK_STATUS_TYPE.get(
                TaskStatusType.COMPLETE).get('enable_time_reporting'),
            'mark_assignees_as': DEFAULT_TIME_REPORTING_SETTINGS_ON_THE_BASIS_OF_TASK_STATUS_TYPE.get(
                TaskStatusType.COMPLETE).get('mark_assignees_as'),
            'time_reporting_applies_to': DEFAULT_TIME_REPORTING_SETTINGS_ON_THE_BASIS_OF_TASK_STATUS_TYPE.get(
                TaskStatusType.COMPLETE).get('time_reporting_applies_to'),
            'categorize_reported_time_as': DEFAULT_TIME_REPORTING_SETTINGS_ON_THE_BASIS_OF_TASK_STATUS_TYPE.get(
                TaskStatusType.COMPLETE).get('categorize_reported_time_as')
        },
        {
            'type_id': TaskStatusType.CANCELLED,
            'type': convert_taskstatus_to_text(TaskStatusType.CANCELLED),
            'require_notes': True,
            'title': 'Cancel',
            'color': '#ea583d',
            'description': 'Task has been cancelled.',
            'visible_to_customer': True
        },
        {
            'type_id': TaskStatusType.EXCEPTION,
            'type': convert_taskstatus_to_text(TaskStatusType.EXCEPTION),
            'require_notes': True,
            'title': 'Exception',
            'color': '#fd8b86',
            'description': 'There has been an exception in the job.',
            'visible_to_customer': True
        },
        {
            'type_id': TaskStatusType.PREPARING,
            'type': convert_taskstatus_to_text(TaskStatusType.PREPARING),
            'require_estimate': True,
            'title': 'Preparing',
            'color': '#ff9608',
            'description': 'Preparing.',
            'visible_to_customer': True
        },
        {
            'type_id': TaskStatusType.EXTRA_TIME,
            'type': convert_taskstatus_to_text(TaskStatusType.EXTRA_TIME),
            'require_estimate': True,
            'title': 'Extra Time',
            'color': '#29B6F6',
            'description': 'Require extra time to finish the task',
            'visible_to_customer': False
        },
        {
            'type_id': TaskStatusType.READYFORPICKUP,
            'type': convert_taskstatus_to_text(TaskStatusType.READYFORPICKUP),
            'title': 'Ready for Pickup',
            'color': '#7b85d6',
            'description': 'Ready for pickup.',
            'visible_to_customer': True
        },
        {
            'type_id': TaskStatusType.CONFIRMED,
            'type': convert_taskstatus_to_text(TaskStatusType.CONFIRMED),
            'title': 'Confirm',
            'color': '#4cc791',
            'description': 'Customer has confirmed the appointment.',
            'visible_to_customer': True
        },
        {
            'type_id': TaskStatusType.CUSTOMER_EXCEPTION,
            'type': convert_taskstatus_to_text(TaskStatusType.CUSTOMER_EXCEPTION),
            'title': 'Customer Exception',
            'color': '#fd8b86',
            'description': 'There has been an exception on the customer end.',
            'visible_to_customer': True
        },
        {
            'type_id': TaskStatusType.BOOKING_CANCELLED,
            'type': convert_taskstatus_to_text(TaskStatusType.BOOKING_CANCELLED),
            'title': 'Booking Cancelled',
            'color': '#fd8b86',
            'description': 'Booking has been cancelled',
            'visible_to_customer': True
        },
        {
            'type_id': TaskStatusType.CUSTOMER_SIGNATURE,
            'type': convert_taskstatus_to_text(TaskStatusType.CUSTOMER_SIGNATURE),
            'title': 'Customer Signature',
            'color': '#964646',
            'visible_to_customer': True,
            'require_signature': True,
            'description': 'Ask for customer signature.'
        },
        {
            'type_id': TaskStatusType.ON_HOLD,
            'type': convert_taskstatus_to_text(TaskStatusType.ON_HOLD),
            'title': 'On hold',
            'color': '#F57C00',
            'description': 'The Task is on hold',
            'visible_to_customer': True
        },
        {
            'type_id': TaskStatusType.MOVING_TO_STORAGE,
            'type': convert_taskstatus_to_text(TaskStatusType.MOVING_TO_STORAGE),
            'title': 'Moving to Storage',
            'color': '#039BE5',
            'description': 'Moving to Storage',
            'visible_to_customer': True
        },
        {
            'type_id': TaskStatusType.IN_STORAGE,
            'type': convert_taskstatus_to_text(TaskStatusType.IN_STORAGE),
            'title': 'In Storage',
            'color': '#81D4FA',
            'description': 'In Storage',
            'visible_to_customer': True
        },
        {
            'type_id': TaskStatusType.OUT_OF_STORAGE,
            'type': convert_taskstatus_to_text(TaskStatusType.OUT_OF_STORAGE),
            'title': 'Out of Storage',
            'color': '#039BE5',
            'description': 'Out of Storage',
            'visible_to_customer': True
        },
        {
            'type_id': TaskStatusType.IN_TRANSIT,
            'type': convert_taskstatus_to_text(TaskStatusType.IN_TRANSIT),
            'title': 'In transit',
            'color': '#607D8B',
            'description': 'Is in transit',
            'visible_to_customer': True
        },
        {
            'type_id': TaskStatusType.PICKING_UP,
            'type': convert_taskstatus_to_text(TaskStatusType.PICKING_UP),
            'title': 'Picking Up',
            'color': '#5E35B1',
            'description': 'Picking up',
            'visible_to_customer': True
        },
        {
            'type_id': TaskStatusType.ORDER,
            'type': convert_taskstatus_to_text(TaskStatusType.ORDER),
            'title': 'Order',
            'color': '#EFBDAA',
            'description': 'Ask for the status of products/items of a task.',
            'visible_to_customer': False
        },
        {
            'type_id': TaskStatusType.SKIP,
            'type': convert_taskstatus_to_text(TaskStatusType.SKIP),
            'title': 'Skip',
            'color': '#DB9797',
            'description': 'Skip the current task.',
            'visible_to_customer': True
        },
        {
            'type_id': TaskStatusType.DAY_START,
            'type': convert_taskstatus_to_text(TaskStatusType.DAY_START),
            'title': 'Day Start',
            'color': '#13b3c5',
            'description': 'For task spanning multiple days, indicate the start of work of each day.',
            'visible_to_customer': True,
            'enable_time_reporting': DEFAULT_TIME_REPORTING_SETTINGS_ON_THE_BASIS_OF_TASK_STATUS_TYPE.get(
                TaskStatusType.DAY_START).get('enable_time_reporting'),
            'mark_assignees_as': DEFAULT_TIME_REPORTING_SETTINGS_ON_THE_BASIS_OF_TASK_STATUS_TYPE.get(
                TaskStatusType.DAY_START).get('mark_assignees_as'),
            'time_reporting_applies_to': DEFAULT_TIME_REPORTING_SETTINGS_ON_THE_BASIS_OF_TASK_STATUS_TYPE.get(
                TaskStatusType.DAY_START).get('time_reporting_applies_to'),
            'categorize_reported_time_as': DEFAULT_TIME_REPORTING_SETTINGS_ON_THE_BASIS_OF_TASK_STATUS_TYPE.get(
                TaskStatusType.DAY_START).get('categorize_reported_time_as')
        },
        {
            'type_id': TaskStatusType.DAY_COMPLETE,
            'type': convert_taskstatus_to_text(TaskStatusType.DAY_COMPLETE),
            'title': 'Day Complete',
            'color': '#2dbb0a',
            'description': 'For task spanning multiple days, indicate the completeness of work of each day.',
            'visible_to_customer': True,
            'enable_time_reporting': DEFAULT_TIME_REPORTING_SETTINGS_ON_THE_BASIS_OF_TASK_STATUS_TYPE.get(
                TaskStatusType.DAY_COMPLETE).get('enable_time_reporting'),
            'mark_assignees_as': DEFAULT_TIME_REPORTING_SETTINGS_ON_THE_BASIS_OF_TASK_STATUS_TYPE.get(
                TaskStatusType.DAY_COMPLETE).get('mark_assignees_as'),
            'time_reporting_applies_to': DEFAULT_TIME_REPORTING_SETTINGS_ON_THE_BASIS_OF_TASK_STATUS_TYPE.get(
                TaskStatusType.DAY_COMPLETE).get('time_reporting_applies_to'),
            'categorize_reported_time_as': DEFAULT_TIME_REPORTING_SETTINGS_ON_THE_BASIS_OF_TASK_STATUS_TYPE.get(
                TaskStatusType.DAY_COMPLETE).get('categorize_reported_time_as')
        },
        {
            'type_id': TaskStatusType.CLOCK_IN,
            'type': convert_taskstatus_to_text(TaskStatusType.CLOCK_IN),
            'title': 'Clock In',
            'color': '#29c7f2',
            'description': 'To indicate the Clock In time for office and warehouse workers.',
            'visible_to_customer': False,
            'enable_time_reporting': DEFAULT_TIME_REPORTING_SETTINGS_ON_THE_BASIS_OF_TASK_STATUS_TYPE.get(
                TaskStatusType.CLOCK_IN).get('enable_time_reporting'),
            'mark_assignees_as': DEFAULT_TIME_REPORTING_SETTINGS_ON_THE_BASIS_OF_TASK_STATUS_TYPE.get(
                TaskStatusType.CLOCK_IN).get('mark_assignees_as'),
            'time_reporting_applies_to': DEFAULT_TIME_REPORTING_SETTINGS_ON_THE_BASIS_OF_TASK_STATUS_TYPE.get(
                TaskStatusType.CLOCK_IN).get('time_reporting_applies_to'),
            'categorize_reported_time_as': DEFAULT_TIME_REPORTING_SETTINGS_ON_THE_BASIS_OF_TASK_STATUS_TYPE.get(
                TaskStatusType.CLOCK_IN).get('categorize_reported_time_as')
        },
        {
            'type_id': TaskStatusType.CLOCK_OUT,
            'type': convert_taskstatus_to_text(TaskStatusType.CLOCK_OUT),
            'title': 'Clock Out',
            'color': '#32de2c',
            'description': 'To indicate the Clock Out time for office and warehouse workers.',
            'visible_to_customer': False,
            'enable_time_reporting': DEFAULT_TIME_REPORTING_SETTINGS_ON_THE_BASIS_OF_TASK_STATUS_TYPE.get(
                TaskStatusType.CLOCK_OUT).get('enable_time_reporting'),
            'mark_assignees_as': DEFAULT_TIME_REPORTING_SETTINGS_ON_THE_BASIS_OF_TASK_STATUS_TYPE.get(
                TaskStatusType.CLOCK_OUT).get('mark_assignees_as'),
            'time_reporting_applies_to': DEFAULT_TIME_REPORTING_SETTINGS_ON_THE_BASIS_OF_TASK_STATUS_TYPE.get(
                TaskStatusType.CLOCK_OUT).get('time_reporting_applies_to'),
            'categorize_reported_time_as': DEFAULT_TIME_REPORTING_SETTINGS_ON_THE_BASIS_OF_TASK_STATUS_TYPE.get(
                TaskStatusType.CLOCK_OUT).get('categorize_reported_time_as')
        },
        {
            'type_id': TaskStatusType.PROCESS_PAYMENT,
            'type': convert_taskstatus_to_text(TaskStatusType.PROCESS_PAYMENT),
            'title': 'Process Payment',
            'color': '#ea583d',
            'description': 'Start payment processing.',
            'visible_to_customer': True
        },
        {
            'type_id': TaskStatusType.MILESTONE,
            'type': convert_taskstatus_to_text(TaskStatusType.MILESTONE),
            'title': 'Milestone',
            'color': '#4A148C',
            'description': 'To indicate a stage achieved.',
            'visible_to_customer': False
        },
        {
            'type_id': TaskStatusType.INVOICE_GENERATED,
            'type': convert_taskstatus_to_text(TaskStatusType.INVOICE_GENERATED),
            'title': 'Invoice Generated',
            'color': '#ea553d',
            'description': 'Start invoice generation.',
            'visible_to_customer': True
        },
        {
            'type_id': TaskStatusType.PAYMENT_MADE,
            'type': convert_taskstatus_to_text(TaskStatusType.PAYMENT_MADE),
            'title': 'PAYMENT_MADE',
            'color': '#006400',
            'description': 'To make a payment.',
            'visible_to_customer': True
        },
        {
            'type_id': TaskStatusType.CLOSED,
            'type': convert_taskstatus_to_text(TaskStatusType.CLOSED),
            'title': 'Closed',
            'color': '#BB3924',
            'description': 'To close a task',
            'visible_to_customer': True
        },
        {
            'type_id': TaskStatusType.INTEGRATION,
            'type': convert_taskstatus_to_text(TaskStatusType.INTEGRATION),
            'title': 'Integration',
            'color': '#FFF176',
            'description': 'Initiate an Integration Action',
            'visible_to_customer': False
        },
    ]

    TYPE_CHOICES = [
        (id, id) for id in UserPermissionGroups.get_defined_permission_group_ids()
    ]
    permission_group_id = models.IntegerField(choices=TYPE_CHOICES,
                                              default=UserPermissionGroups.DEFAULT_PERMISSION_GROUP_ID)
    
    STATUS_TRIGGER_CHOICES = (
        StatusTriggerType.ALWAYS,
        StatusTriggerType.FORM_COMPLETE,
        StatusTriggerType.FORM_SAVE, 'FORM_SAVE',
        StatusTriggerType.STATUS, 'STATUS',
    )
    status_trigger = models.IntegerField(choices=[(x, x) for x in STATUS_TRIGGER_CHOICES], 
                                         default=StatusTriggerType.ALWAYS)


    def serialize(self):
        permission_group = None
        if self.permission_group_id == -1:
            permission_group = 'Customer'
        else:
            for group in UserPermissionGroups.get_defined_permission_groups():
                if self.permission_group_id == group.get('group_id'):
                    permission_group = group.get('title')
                    break
        
        logging.info("Entity Permission Group: {}".format(permission_group))

        return dict(
            id=self.id,
            owner=self.owner,
            created=self.created.isoformat() if self.created else None,
            updated=self.updated.isoformat() if self.updated else None,
            type_id=self.type,
            type=convert_taskstatus_to_text(self.type),
            title=self.title,
            description=self.description,
            permission_group=permission_group,
            status_trigger=convert_status_trigger_type_to_status_trigger_name(self.status_trigger) if self.status_trigger else
            convert_status_trigger_type_to_status_trigger_name(StatusTriggerType.ALWAYS),
        )

    

class TemplateType:
    TASK = 1001
    ACTIVITY = 1002

    @classmethod
    def get_all_template_types(cls):
        return [cls.TASK, cls.ACTIVITY]
    
    

QUERY_FILTER_FOR_AUTO_START_COMPLETE = [TemplateType.TASK]


class Template(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    auto_start_delay_time = models.IntegerField(default=15)
    auto_complete_delay_time = models.IntegerField(default=90)
    disable_auto_start_complete = models.BooleanField(default=False)
    statuses = ArrayField(
        base_field=models.IntegerField(),
        blank=True,
        null=True
    )
    mark_enroute_after_complete = models.BooleanField(default=True)
    next_task_info = models.TextField(null=True)

    @classmethod
    def get_by_id(cls, tid, user):
        return Template.objects.get(pk=tid, owner=user)

    def get_statuses(self, get_all_statuses=False,
                     permission_group_id=UserPermissionGroups.DEFAULT_PERMISSION_GROUP_ID):

        # replace Booking Only permission group with scheduler group id to get scheduler available statuses for
        # Booking Only
        if permission_group_id == UserPermissionGroups.BOOKING_ONLY_PERMISSION_GROUP_ID:
            permission_group_id = UserPermissionGroups.SCHEDULER_PERMISSION_GROUP_ID

        status_types = []
        for sid in self.statuses:
            statustype = Status.objects.get(pk=sid)
            if not statustype:
                logging.error('Status not found against status_id: {}'.format(sid))
                continue
            if not get_all_statuses:
                if statustype.permission_group_id != permission_group_id:
                    logging.warning(
                        'Ignoring the status as it is not for given permission group i.e. {0}. status_id is: {1}'.format(
                            convert_permission_group_id_to_permission_group_title(permission_group_id), sid))
                    continue
            
            status = statustype.serialize()
            if status.get('type') == 'COMPLETE':
                # Specifically checking it False to make sure if it is None than return True
                if hasattr(self, 'mark_enroute_after_complete') and self.mark_enroute_after_complete == False:
                    status['mark_enroute_after_complete'] = False
                else:
                    status['mark_enroute_after_complete'] = True
                if hasattr(self, 'next_task_info') and self.next_task_info is not None:
                    status['next_task_info'] = self.next_task_info
                else:
                    status['next_task_info'] = 'Marked COMPLETE. Set ENROUTE for next task.'
            status_types.append(status)

        return status_types
    
