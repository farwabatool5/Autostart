from django.db import models
from application.files import *


def convert_event_type_name_to_event_type(event_type_name):
    if event_type_name == 'TASK_CREATED':
        return EventType.TASK_CREATED
    elif event_type_name == 'TASK_STATUS':
        return EventType.TASK_STATUS
    elif event_type_name == 'CREW_ASSIGNED':
        return EventType.CREW_ASSIGNED
    elif event_type_name == 'CREW_REMOVED':
        return EventType.CREW_REMOVED
    elif event_type_name == 'EQUIPMENT_ASSIGNED':
        return EventType.EQUIPMENT_ASSIGNED
    elif event_type_name == 'EQUIPMENT_REMOVED':
        return EventType.EQUIPMENT_REMOVED
    elif event_type_name == 'TASK_NOTE':
        return EventType.TASK_NOTE
    elif event_type_name == 'TASK_RATING':
        return EventType.TASK_RATING
    elif event_type_name == 'TASK_RESCHEDULED':
        return EventType.TASK_RESCHEDULED
    elif event_type_name == 'TASK_DELETED':
        return EventType.TASK_DELETED
    elif event_type_name == 'LATE':
        return EventType.LATE
    elif event_type_name == 'PREDICTED_LATE':
        return EventType.PREDICTED_LATE
    elif event_type_name == 'NOSHOW':
        return EventType.NOSHOW
    elif event_type_name == 'TASK_CUSTOM':
        return EventType.TASK_CUSTOM
    elif event_type_name == 'ARRIVING':
        return EventType.ARRIVING
    elif event_type_name == 'TASK_ACCEPTED':
        return EventType.TASK_ACCEPTED
    elif event_type_name == 'TASK_REJECTED':
        return EventType.TASK_REJECTED
    elif event_type_name == 'TASK_GROUP_CHANGED':
        return EventType.TASK_GROUP_CHANGED
    elif event_type_name == 'TASK_TEMPLATE_CHANGED':
        return EventType.TASK_TEMPLATE_CHANGED
    elif event_type_name == 'TASK_TEMPLATE_EXTRA_FIELDS_UPDATED':
        return EventType.TASK_TEMPLATE_EXTRA_FIELDS_UPDATED
    elif event_type_name == 'TASK_PRIMARY_ADDRESS_UPDATED':
        return EventType.TASK_PRIMARY_ADDRESS_UPDATED
    elif event_type_name == 'TASK_ADDITIONAL_ADDRESSES_UPDATED':
        return EventType.TASK_ADDITIONAL_ADDRESSES_UPDATED
    else:
        return EventType.TASK_CUSTOM

def convert_object_type_name_to_object_type(object_type_name):
    if object_type_name == 'TASK':
        return ObjectType.TASK
    elif object_type_name == 'TASK_STATUS':
        return ObjectType.TASK_STATUS
    elif object_type_name == 'CREW':
        return ObjectType.CREW
    elif object_type_name == 'EQUIPMENT':
        return ObjectType.EQUIPMENT
    elif object_type_name == 'TASK_RATING':
        return ObjectType.TASK_RATING
    else:
        return ObjectType.CUSTOM

def convert_object_type_name_to_object_type(object_type_name):
    if object_type_name == 'TASK':
        return ObjectType.TASK
    elif object_type_name == 'TASK_STATUS':
        return ObjectType.TASK_STATUS
    elif object_type_name == 'CREW':
        return ObjectType.CREW
    elif object_type_name == 'EQUIPMENT':
        return ObjectType.EQUIPMENT
    elif object_type_name == 'TASK_RATING':
        return ObjectType.TASK_RATING
    else:
        return ObjectType.CUSTOM


class ObjectType:
    TASK = 1000
    TASK_STATUS = 1001
    CREW = 1002
    EQUIPMENT = 1003
    TASK_RATING = 1004
    CUSTOM = 1100


class EventType:
    TASK_CREATED = 1000
    TASK_STATUS = 1001
    CREW_ASSIGNED = 1002
    CREW_REMOVED = 1003
    EQUIPMENT_ASSIGNED = 1004
    EQUIPMENT_REMOVED = 1005
    TASK_NOTE = 1006
    TASK_RATING = 1007
    TASK_RESCHEDULED = 1008
    TASK_DELETED = 1009

    LATE = 1051
    NOSHOW = 1052
    PREDICTED_LATE = 1053

    TASK_CUSTOM = 1100
    ARRIVING = 1101
    TASK_ACCEPTED = 1102
    TASK_REJECTED = 1103

    TASK_GROUP_CHANGED = 1200
    TASK_TEMPLATE_CHANGED = 1201
    TASK_TEMPLATE_EXTRA_FIELDS_UPDATED = 1202
    TASK_PRIMARY_ADDRESS_UPDATED = 1203
    TASK_ADDITIONAL_ADDRESSES_UPDATED = 1204

class Event(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    EVENT_CHOICES = [
        EventType.TASK_CREATED,
        EventType.TASK_STATUS,
        EventType.CREW_ASSIGNED,
        EventType.CREW_REMOVED,
        EventType.EQUIPMENT_ASSIGNED,
        EventType.EQUIPMENT_REMOVED,
        EventType.TASK_NOTE,
        EventType.TASK_RATING,
        EventType.TASK_RESCHEDULED,
        EventType.TASK_DELETED,
        EventType.LATE,
        EventType.PREDICTED_LATE,
        EventType.NOSHOW,
        EventType.TASK_CUSTOM,
        EventType.ARRIVING,
        EventType.TASK_ACCEPTED,
        EventType.TASK_REJECTED,
        EventType.TASK_GROUP_CHANGED,
        EventType.TASK_TEMPLATE_CHANGED,
        EventType.TASK_TEMPLATE_EXTRA_FIELDS_UPDATED,
        EventType.TASK_PRIMARY_ADDRESS_UPDATED,
        EventType.TASK_ADDITIONAL_ADDRESSES_UPDATED
    ]
    type = models.IntegerField(choices=[(x, x) for x in EVENT_CHOICES], default=EventType.TASK_STATUS)
    object_id = models.IntegerField()
    TYPE_CHOICES = [
        ObjectType.TASK,
        ObjectType.TASK_STATUS,
        ObjectType.CREW,
        ObjectType.EQUIPMENT,
        ObjectType.TASK_RATING
    ]
    object_type = models.IntegerField(choices=[(x, x) for x in TYPE_CHOICES],default=ObjectType.TASK_STATUS)
    subject_id = models.IntegerField()
    SUBJECT_CHOICES = [
        ObjectType.TASK,
        ObjectType.TASK_STATUS,
        ObjectType.CREW,
        ObjectType.EQUIPMENT,
        ObjectType.TASK_RATING,
        ObjectType.CUSTOM
    ]
    subject_type = models.IntegerField(choices=[(x, x) for x in SUBJECT_CHOICES],default=ObjectType.TASK_STATUS)
    object_title = models.CharField(max_length=255)
    message = models.TextField()
    time = models.DateTimeField()
    reporter_id = models.IntegerField()
    reporter_name = models.CharField(max_length=255)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    @classmethod
    def create(cls, **kv):
        kv['type'] = convert_event_type_name_to_event_type(kv['type'])
        kv['object_type'] = convert_object_type_name_to_object_type(kv['object_type'])

        if 'subject_type' in kv:
            kv['subject_type'] = convert_object_type_name_to_object_type(kv['subject_type'])

        event = Event(**kv)
        event.save()
        return event


class TimeReportTriggerMetaData(models.Model):
    template_status_id = models.IntegerField()
    status_id = models.IntegerField()
    task_id = models.IntegerField()
    status_type = models.IntegerField()
    status_title = models.CharField(max_length=255)
    status_time = models.DateTimeField()
    status_time_original_iso_str = models.CharField(max_length=255)
