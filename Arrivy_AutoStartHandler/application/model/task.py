from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.db.models import Q
from datetime import datetime
from django.utils import timezone


from application.files import *

# Create your models here.

def get_shadow_key_from_task_key(key, user_id):
    task_shadow = TaskShadow.objects.filter(Q(task_id=key) & Q(owner=user_id)).get()
    return task_shadow

class EntityMissingValue(Exception):
    pass


class statuses_meta_data:
    meta_data = {
        TaskStatusType.NOTSTARTED: {
            'is_terminal': False,
            'is_deletable': False,
            'is_internal': False,
            'is_task_latest_status': True,
            'is_transient': False
        },
        TaskStatusType.ENROUTE: {
            'is_terminal': False,
            'is_deletable': True,
            'is_internal': False,
            'is_task_latest_status': True,
            'is_transient': False
        },
        TaskStatusType.STARTED: {
            'is_terminal': False,
            'is_deletable': True,
            'is_internal': False,
            'is_task_latest_status': True,
            'is_transient': False
        },
        TaskStatusType.COMPLETE: {
            'is_terminal': True,
            'is_deletable': True,
            'is_internal': False,
            'is_task_latest_status': True,
            'is_transient': False
        },
        TaskStatusType.CANCELLED: {
            'is_terminal': True,
            'is_deletable': True,
            'is_internal': False,
            'is_task_latest_status': True,
            'is_transient': False
        },
        TaskStatusType.EXCEPTION: {
            'is_terminal': True,
            'is_deletable': True,
            'is_internal': False,
            'is_task_latest_status': True,
            'is_transient': False
        },
        TaskStatusType.CUSTOM: {
            'is_terminal': False,
            'is_deletable': True,
            'is_internal': True,
            'is_task_latest_status': False,
            'is_transient': False
        },
        TaskStatusType.PREPARING: {
            'is_terminal': False,
            'is_deletable': True,
            'is_internal': False,
            'is_task_latest_status': True,
            'is_transient': False
        },
        TaskStatusType.READYFORPICKUP: {
            'is_terminal': False,
            'is_deletable': True,
            'is_internal': False,
            'is_task_latest_status': True,
            'is_transient': False
        },
        TaskStatusType.CONFIRMED: {
            'is_terminal': False,
            'is_deletable': True,
            'is_internal': False,
            'is_task_latest_status': True,
            'is_transient': False
        },
        TaskStatusType.RESCHEDULED: {
            'is_terminal': False,
            'is_deletable': False,
            'is_internal': True,
            'is_task_latest_status': True,
            'is_transient': False
        },
        TaskStatusType.ARRIVING: {
            'is_terminal': False,
            'is_deletable': False,
            'is_internal': True,
            'is_task_latest_status': True,
            'is_transient': False
        },
        TaskStatusType.LATE: {
            'is_terminal': False,
            'is_deletable': False,
            'is_internal': True,
            'is_task_latest_status': True,
            'is_transient': False
        },
        TaskStatusType.PREDICTED_LATE: {
            'is_terminal': False,
            'is_deletable': False,
            'is_internal': True,
            'is_task_latest_status': True,
            'is_transient': False
        },
        TaskStatusType.NOSHOW: {
            'is_terminal': True,
            'is_deletable': False,
            'is_internal': True,
            'is_task_latest_status': True,
            'is_transient': False
        },
        TaskStatusType.EXTRA_TIME: {
            'is_terminal': False,
            'is_deletable': True,
            'is_internal': False,
            'is_task_latest_status': True,
            'is_transient': False
        },
        TaskStatusType.REMINDER: {
            'is_terminal': False,
            'is_deletable': False,
            'is_internal': True,
            'is_task_latest_status': False,
            'is_transient': False
        },
        TaskStatusType.RECOMMENDED: {
            'is_terminal': True,
            'is_deletable': True,
            'is_internal': False,
            'is_task_latest_status': True,
            'is_transient': False
        },
        TaskStatusType.REVIEW_REMINDER: {
            'is_terminal': False,
            'is_deletable': False,
            'is_internal': True,
            'is_task_latest_status': False,
            'is_transient': False
        },
        TaskStatusType.CUSTOMER_SIGNATURE: {
            'is_terminal': False,
            'is_deletable': True,
            'is_internal': False,
            'is_task_latest_status': True,
            'is_transient': False
        },
        TaskStatusType.CUSTOMER_EXCEPTION: {
            'is_terminal': True,
            'is_deletable': True,
            'is_internal': False,
            'is_task_latest_status': True,
            'is_transient': False
        },
        TaskStatusType.BOOKING_CANCELLED: {
            'is_terminal': True,
            'is_deletable': True,
            'is_internal': False,
            'is_task_latest_status': True,
            'is_transient': False
        },
        TaskStatusType.SEEN_BY_CUSTOMER: {
            'is_terminal': False,
            'is_deletable': False,
            'is_internal': True,
            'is_task_latest_status': False,
            'is_transient': False
        },
        TaskStatusType.FILE_ANNOTATED: {
            'is_terminal': False,
            'is_deletable': False,
            'is_internal': False,
            'is_task_latest_status': False,
            'is_transient': False
        },
        TaskStatusType.CREW_ASSIGNED: {
            'is_terminal': False,
            'is_deletable': False,
            'is_internal': True,
            'is_task_latest_status': False,
            'is_transient': False
        },
        TaskStatusType.CREW_REMOVED: {
            'is_terminal': False,
            'is_deletable': False,
            'is_internal': True,
            'is_task_latest_status': False,
            'is_transient': False
        },
        TaskStatusType.EQUIPMENT_ASSIGNED: {
            'is_terminal': False,
            'is_deletable': False,
            'is_internal': True,
            'is_task_latest_status': False,
            'is_transient': False
        },
        TaskStatusType.EQUIPMENT_REMOVED: {
            'is_terminal': False,
            'is_deletable': False,
            'is_internal': True,
            'is_task_latest_status': False,
            'is_transient': False
        },
        TaskStatusType.ON_HOLD: {
            'is_terminal': False,
            'is_deletable': True,
            'is_internal': False,
            'is_task_latest_status': True,
            'is_transient': False
        },
        TaskStatusType.MOVING_TO_STORAGE: {
            'is_terminal': False,
            'is_deletable': True,
            'is_internal': False,
            'is_task_latest_status': True,
            'is_transient': False
        },
        TaskStatusType.IN_STORAGE: {
            'is_terminal': False,
            'is_deletable': True,
            'is_internal': False,
            'is_task_latest_status': True,
            'is_transient': False
        },
        TaskStatusType.OUT_OF_STORAGE: {
            'is_terminal': False,
            'is_deletable': True,
            'is_internal': False,
            'is_task_latest_status': True,
            'is_transient': False
        },
        TaskStatusType.IN_TRANSIT: {
            'is_terminal': False,
            'is_deletable': True,
            'is_internal': False,
            'is_task_latest_status': True,
            'is_transient': False
        },
        TaskStatusType.PICKING_UP: {
            'is_terminal': False,
            'is_deletable': True,
            'is_internal': False,
            'is_task_latest_status': True,
            'is_transient': False
        },
        TaskStatusType.ARRIVED: {
            'is_terminal': False,
            'is_deletable': False,
            'is_internal': True,
            'is_task_latest_status': False,
            'is_transient': False
        },
        TaskStatusType.DEPARTED: {
            'is_terminal': False,
            'is_deletable': False,
            'is_internal': True,
            'is_task_latest_status': False,
            'is_transient': False
        },
        TaskStatusType.AUTO_START_PENDING: {
            'is_terminal': False,
            'is_deletable': False,
            'is_internal': True,
            'is_task_latest_status': False,
            'is_transient': True
        },
        TaskStatusType.AUTO_START: {
            'is_terminal': False,
            'is_deletable': False,
            'is_internal': True,
            'is_task_latest_status': True,
            'is_transient': False
        },
        TaskStatusType.AUTO_COMPLETE_PENDING: {
            'is_terminal': False,
            'is_deletable': False,
            'is_internal': True,
            'is_task_latest_status': False,
            'is_transient': True
        },
        TaskStatusType.AUTO_COMPLETE: {
            'is_terminal': True,
            'is_deletable': False,
            'is_internal': True,
            'is_task_latest_status': True,
            'is_transient': False
        },
        TaskStatusType.RETURNED: {
            'is_terminal': False,
            'is_deletable': False,
            'is_internal': True,
            'is_task_latest_status': False,
            'is_transient': False
        },
        TaskStatusType.ORDER: {
            'is_terminal': False,
            'is_deletable': True,
            'is_internal': False,
            'is_task_latest_status': False,
            'is_transient': False
        },
        TaskStatusType.SKIP: {
            'is_terminal': True,
            'is_deletable': True,
            'is_internal': False,
            'is_task_latest_status': True,
            'is_transient': False
        },
        TaskStatusType.SUBSCRIBED: {
            'is_terminal': False,
            'is_deletable': False,
            'is_internal': True,
            'is_task_latest_status': False,
            'is_transient': False
        },
        TaskStatusType.UNSUBSCRIBED: {
            'is_terminal': False,
            'is_deletable': False,
            'is_internal': True,
            'is_task_latest_status': False,
            'is_transient': False
        },
        TaskStatusType.HELP: {
            'is_terminal': False,
            'is_deletable': False,
            'is_internal': True,
            'is_task_latest_status': False,
            'is_transient': False
        },
        TaskStatusType.LAUNCH_DOCUMENT: {
            'is_terminal': False,
            'is_deletable': False,
            'is_internal': False,
            'is_task_latest_status': False,
            'is_transient': False
        },
        TaskStatusType.MANUAL_NOTIFICATION: {
            'is_terminal': False,
            'is_deletable': False,
            'is_internal': False,
            'is_task_latest_status': False,
            'is_transient': False
        },
        TaskStatusType.CHECKINVENTORY: {
            'is_terminal': False,
            'is_deletable': False,
            'is_internal': False,
            'is_task_latest_status': False,
            'is_transient': False
        },
        TaskStatusType.CHECKSUPPLIES: {
            'is_terminal': False,
            'is_deletable': False,
            'is_internal': True,
            'is_task_latest_status': False,
            'is_transient': False
        },
        TaskStatusType.RESEND_TASK_CONFIRMATION: {
            'is_terminal': False,
            'is_deletable': False,
            'is_internal': True,
            'is_task_latest_status': True,
            'is_transient': False
        },
        TaskStatusType.FORM_COMPLETE: {
            'is_terminal': False,
            'is_deletable': False,
            'is_internal': False,
            'is_task_latest_status': False,
            'is_transient': False
        },
        TaskStatusType.FORM_ATTACH: {
            'is_terminal': False,
            'is_deletable': True,
            'is_internal': False,
            'is_task_latest_status': False,
            'is_transient': False
        },
        TaskStatusType.FORM_SUBMIT: {
            'is_terminal': False,
            'is_deletable': False,
            'is_internal': False,
            'is_task_latest_status': False,
            'is_transient': False
        },
        TaskStatusType.TASK_ACCEPTED: {
            'is_terminal': False,
            'is_deletable': False,
            'is_internal': False,
            'is_task_latest_status': False,
            'is_transient': False
        },
        TaskStatusType.TASK_REJECTED: {
            'is_terminal': False,
            'is_deletable': False,
            'is_internal': False,
            'is_task_latest_status': False,
            'is_transient': False
        },
        TaskStatusType.DAY_START: {
            'is_terminal': False,
            'is_deletable': True,
            'is_internal': False,
            'is_task_latest_status': True,
            'is_transient': False
        },
        TaskStatusType.DAY_COMPLETE: {
            'is_terminal': False,
            'is_deletable': True,
            'is_internal': False,
            'is_task_latest_status': True,
            'is_transient': False
        },
        TaskStatusType.CLOCK_IN: {
            'is_terminal': False,
            'is_deletable': False,
            'is_internal': False,
            'is_task_latest_status': False,
            'is_transient': False
        },
        TaskStatusType.CLOCK_OUT: {
            'is_terminal': False,
            'is_deletable': False,
            'is_internal': False,
            'is_task_latest_status': False,
            'is_transient': False
        },
        TaskStatusType.PROCESS_PAYMENT: {
            'is_terminal': False,
            'is_deletable': False,
            'is_internal': False,
            'is_task_latest_status': True,
            'is_transient': False
        },
        TaskStatusType.MILESTONE: {
            'is_terminal': False,
            'is_deletable': True,
            'is_internal': False,
            'is_task_latest_status': True,
            'is_transient': False
        },
        TaskStatusType.FORM_REMINDER: {
            'is_terminal': False,
            'is_deletable': False,
            'is_internal': True,
            'is_task_latest_status': False,
            'is_transient': False
        },
        TaskStatusType.INVOICE_GENERATED: {
            'is_terminal': False,
            'is_deletable': False,
            'is_internal': True,
            'is_task_latest_status': True,
            'is_transient': False
        },
        TaskStatusType.PAYMENT_MADE: {
            'is_terminal': False,
            'is_deletable': False,
            'is_internal': True,
            'is_task_latest_status': True,
            'is_transient': False
        },
        TaskStatusType.CLOSED: {
            'is_terminal': False,
            'is_deletable': True,
            'is_internal': False,
            'is_task_latest_status': True,
            'is_transient': False
        },
        TaskStatusType.INTEGRATION: {
            'is_terminal': False,
            'is_deletable': False,
            'is_internal': False,
            'is_task_latest_status': False,
            'is_transient': False
        },
        TaskStatusType.OPT_IN_MESSAGE_SENT: {
            'is_terminal': False,
            'is_deletable': False,
            'is_internal': False,
            'is_task_latest_status': False,
            'is_transient': False
        },
        TaskStatusType.CONSENT_PENDING: {
            'is_terminal': False,
            'is_deletable': False,
            'is_internal': False,
            'is_task_latest_status': False,
            'is_transient': False
        },
    }
    

class Task(models.Model):
    start_datetime = models.DateTimeField()
    unscheduled = models.BooleanField(default=False)
    # similer to entity_ids = ndb.IntegerProperty(repeated=True) in ndb
    entity_ids = ArrayField(
        base_field=models.IntegerField(),
        blank=True,
        null=True
    )
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    template = models.ForeignKey(Template, on_delete=models.CASCADE)
    template_type = models.IntegerField()

    def get_id(self):
        return self.id

    # @ndb.transactional()
    def update_status(self, status_type, status_title, parent, **kwargs):
        # Don't set internal_statuses as latest status on task
        if statuses_meta_data.meta_data[status_type]['is_task_latest_status']:
            task_shadow = TaskShadow.fetch_by_task(self)
            task_shadow.status = status_type
            task_shadow.status_title = status_title

            if kwargs.get('extra_fields') and kwargs.get('extra_fields').get('visible_to_customer') and statuses_meta_data.meta_data[status_type]['is_task_latest_status']:
                task_shadow.customer_status_type = status_type
                task_shadow.customer_status_title = status_title

            # task_shadow.put()
            task_shadow.save()

        if 'time' not in kwargs:
            kwargs['time'] = datetime.now().astimezone(timezone.utc)

        self.status = status_type
        self.status_title = status_title
        task_status = TaskStatusData.create(type=status_type, task_shadow=parent, **kwargs)
        return task_status

class TaskShadow(models.Model):
    # amcestor: owner_taskId
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    customer_status_title = models.CharField(max_length=255)

    TYPE_CHOICES = [
        TaskStatusType.NOTSTARTED,
        TaskStatusType.ENROUTE,
        TaskStatusType.STARTED,
        TaskStatusType.COMPLETE,
        TaskStatusType.CANCELLED,
        TaskStatusType.EXCEPTION,
        TaskStatusType.PREPARING,
        TaskStatusType.READYFORPICKUP,
        TaskStatusType.CONFIRMED,
        TaskStatusType.RESCHEDULED,
        TaskStatusType.CUSTOM,
        TaskStatusType.CUSTOMER_EXCEPTION,
        TaskStatusType.BOOKING_CANCELLED,
        TaskStatusType.RECOMMENDED,
        TaskStatusType.CUSTOMER_SIGNATURE,
        TaskStatusType.ARRIVING,
        TaskStatusType.REMINDER,
        TaskStatusType.REVIEW_REMINDER,
        TaskStatusType.LATE,
        TaskStatusType.PREDICTED_LATE,
        TaskStatusType.NOSHOW,
        TaskStatusType.SEEN_BY_CUSTOMER,
        TaskStatusType.CREW_ASSIGNED,
        TaskStatusType.CREW_REMOVED,
        TaskStatusType.EQUIPMENT_ASSIGNED,
        TaskStatusType.EQUIPMENT_REMOVED,
        TaskStatusType.EXTRA_TIME,
        TaskStatusType.ON_HOLD,
        TaskStatusType.MOVING_TO_STORAGE,
        TaskStatusType.IN_STORAGE,
        TaskStatusType.OUT_OF_STORAGE,
        TaskStatusType.IN_TRANSIT,
        TaskStatusType.PICKING_UP,
        TaskStatusType.ARRIVED,
        TaskStatusType.DEPARTED,
        TaskStatusType.AUTO_START_PENDING,
        TaskStatusType.AUTO_START,
        TaskStatusType.AUTO_COMPLETE_PENDING,
        TaskStatusType.AUTO_COMPLETE,
        TaskStatusType.RETURNED,
        TaskStatusType.ORDER,
        TaskStatusType.SKIP,
        TaskStatusType.SUBSCRIBED,
        TaskStatusType.UNSUBSCRIBED,
        TaskStatusType.HELP,
        TaskStatusType.LAUNCH_DOCUMENT,
        TaskStatusType.MANUAL_NOTIFICATION,
        TaskStatusType.CHECKINVENTORY,
        TaskStatusType.CHECKSUPPLIES,
        TaskStatusType.RESEND_TASK_CONFIRMATION,
        TaskStatusType.FORM_COMPLETE,
        TaskStatusType.FORM_SUBMIT,
        TaskStatusType.FORM_ATTACH,
        TaskStatusType.TASK_REJECTED,
        TaskStatusType.TASK_ACCEPTED,
        TaskStatusType.DAY_START,
        TaskStatusType.DAY_COMPLETE,
        TaskStatusType.CLOCK_IN,
        TaskStatusType.CLOCK_OUT,
        TaskStatusType.PROCESS_PAYMENT,
        TaskStatusType.MILESTONE,
        TaskStatusType.FORM_REMINDER,
        TaskStatusType.INVOICE_GENERATED,
        TaskStatusType.PAYMENT_MADE,
        TaskStatusType.CLOSED,
        TaskStatusType.INTEGRATION,
        TaskStatusType.FILE_ANNOTATED,
        TaskStatusType.OPT_IN_MESSAGE_SENT,
        TaskStatusType.CONSENT_PENDING
    ]
    # In Django, the choices attribute of a model field is designed to include both 
    # the value and a human-readable label (display text)
    status = models.IntegerField(choices=[(x, x) for x in TYPE_CHOICES], default=TaskStatusType.NOTSTARTED)

    STATUS_TYPE_CHOICES = [
        TaskStatusType.NOTSTARTED,
        TaskStatusType.ENROUTE,
        TaskStatusType.STARTED,
        TaskStatusType.COMPLETE,
        TaskStatusType.CANCELLED,
        TaskStatusType.EXCEPTION,
        TaskStatusType.PREPARING,
        TaskStatusType.READYFORPICKUP,
        TaskStatusType.CONFIRMED,
        TaskStatusType.RESCHEDULED,
        TaskStatusType.CUSTOM,
        TaskStatusType.CUSTOMER_EXCEPTION,
        TaskStatusType.BOOKING_CANCELLED,
        TaskStatusType.RECOMMENDED,
        TaskStatusType.CUSTOMER_SIGNATURE,
        TaskStatusType.LATE,
        TaskStatusType.NOSHOW,
        TaskStatusType.EXTRA_TIME,
        TaskStatusType.ON_HOLD,
        TaskStatusType.MOVING_TO_STORAGE,
        TaskStatusType.IN_STORAGE,
        TaskStatusType.OUT_OF_STORAGE,
        TaskStatusType.IN_TRANSIT,
        TaskStatusType.PICKING_UP,
        TaskStatusType.ARRIVED,
        TaskStatusType.DEPARTED,
        TaskStatusType.AUTO_START_PENDING,
        TaskStatusType.AUTO_START,
        TaskStatusType.AUTO_COMPLETE_PENDING,
        TaskStatusType.AUTO_COMPLETE,
        TaskStatusType.RETURNED,
        TaskStatusType.ORDER,
        TaskStatusType.SKIP,
        TaskStatusType.RESEND_TASK_CONFIRMATION,
        TaskStatusType.DAY_START,
        TaskStatusType.DAY_COMPLETE,
        TaskStatusType.CLOCK_IN,
        TaskStatusType.CLOCK_OUT,
        TaskStatusType.PROCESS_PAYMENT,
        TaskStatusType.MILESTONE,
        TaskStatusType.FORM_REMINDER,
        TaskStatusType.INVOICE_GENERATED,
        TaskStatusType.PAYMENT_MADE,
        TaskStatusType.CLOSED,
        TaskStatusType.INTEGRATION,
        TaskStatusType.ARRIVING
    ]
    customer_status_type = models.IntegerField(choices=[(x, x) for x in STATUS_TYPE_CHOICES], default=TaskStatusType.NOTSTARTED)



    @classmethod
    def fetch_by_task(cls, task):
        shadow_key = get_shadow_key_from_task_key(task.id, task.owner)
        task_shadow = shadow_key
        if not task_shadow:
            task_shadow = cls.clone_task(task)
        return task_shadow


class TaskStatusData(models.Model):
    # ancestor: taskShadowKey (owner_taskId)
    task_shadow = models.ForeignKey(TaskShadow, on_delete=models.CASCADE)
    time = models.DateTimeField()
    title = models.CharField(max_length=255)
    is_active = models.BooleanField()
    reporter_name = models.CharField(max_length=255)
    reporter_entity_id = models.IntegerField()
    color = models.CharField(max_length=255)
    status = models.IntegerField()
    given = ['type', 'time']
    TYPE_CHOICES = [
        TaskStatusType.NOTSTARTED,
        TaskStatusType.ENROUTE,
        TaskStatusType.STARTED,
        TaskStatusType.COMPLETE,
        TaskStatusType.CANCELLED,
        TaskStatusType.EXCEPTION,
        TaskStatusType.PREPARING,
        TaskStatusType.READYFORPICKUP,
        TaskStatusType.CONFIRMED,
        TaskStatusType.RESCHEDULED,
        TaskStatusType.CUSTOM,
        TaskStatusType.CUSTOMER_EXCEPTION,
        TaskStatusType.BOOKING_CANCELLED,
        TaskStatusType.RECOMMENDED,
        TaskStatusType.CUSTOMER_SIGNATURE,
        TaskStatusType.ARRIVING,
        TaskStatusType.REMINDER,
        TaskStatusType.REVIEW_REMINDER,
        TaskStatusType.LATE,
        TaskStatusType.PREDICTED_LATE,
        TaskStatusType.NOSHOW,
        TaskStatusType.SEEN_BY_CUSTOMER,
        TaskStatusType.CREW_ASSIGNED,
        TaskStatusType.CREW_REMOVED,
        TaskStatusType.EQUIPMENT_ASSIGNED,
        TaskStatusType.EQUIPMENT_REMOVED,
        TaskStatusType.EXTRA_TIME,
        TaskStatusType.ON_HOLD,
        TaskStatusType.MOVING_TO_STORAGE,
        TaskStatusType.IN_STORAGE,
        TaskStatusType.OUT_OF_STORAGE,
        TaskStatusType.IN_TRANSIT,
        TaskStatusType.PICKING_UP,
        TaskStatusType.ARRIVED,
        TaskStatusType.DEPARTED,
        TaskStatusType.AUTO_START_PENDING,
        TaskStatusType.AUTO_START,
        TaskStatusType.AUTO_COMPLETE_PENDING,
        TaskStatusType.AUTO_COMPLETE,
        TaskStatusType.RETURNED,
        TaskStatusType.ORDER,
        TaskStatusType.SKIP,
        TaskStatusType.SUBSCRIBED,
        TaskStatusType.UNSUBSCRIBED,
        TaskStatusType.HELP,
        TaskStatusType.LAUNCH_DOCUMENT,
        TaskStatusType.MANUAL_NOTIFICATION,
        TaskStatusType.CHECKINVENTORY,
        TaskStatusType.CHECKSUPPLIES,
        TaskStatusType.RESEND_TASK_CONFIRMATION,
        TaskStatusType.FORM_COMPLETE,
        TaskStatusType.FORM_ATTACH,
        TaskStatusType.FORM_SUBMIT,
        TaskStatusType.TASK_ACCEPTED,
        TaskStatusType.TASK_REJECTED,
        TaskStatusType.DAY_START,
        TaskStatusType.DAY_COMPLETE,
        TaskStatusType.CLOCK_IN,
        TaskStatusType.CLOCK_OUT,
        TaskStatusType.PROCESS_PAYMENT,
        TaskStatusType.MILESTONE,
        TaskStatusType.FORM_REMINDER,
        TaskStatusType.INVOICE_GENERATED,
        TaskStatusType.PAYMENT_MADE,
        TaskStatusType.CLOSED,
        TaskStatusType.INTEGRATION,
        TaskStatusType.FILE_ANNOTATED,
        TaskStatusType.OPT_IN_MESSAGE_SENT,
        TaskStatusType.CONSENT_PENDING
    ]
    # In Django, the choices attribute of a model field is designed to include both 
    # the value and a human-readable label (display text)
    type = models.IntegerField(choices=[(x, x) for x in TYPE_CHOICES], default=TaskStatusType.NOTSTARTED)
    object_ids = ArrayField(
        base_field=models.IntegerField(),
        blank=True,
        null=True
    )

    @classmethod
    def build(cls, **kv):
        for k, v in kv.items():
            if k in cls.given:
                if not v:
                    raise EntityMissingValue

        if isinstance(kv['type'], str):
            kv['type'] = convert_taskstatus_to_type(kv['type'])

        task_status = TaskStatusData(**kv)
        return task_status

    @classmethod
    def create(cls, **kv):
        task_status = cls.build(**kv)
        task_status.save()
        return task_status

    def get_id(self):
        return self.id


