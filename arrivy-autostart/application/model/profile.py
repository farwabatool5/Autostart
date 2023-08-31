from django.db import models
from config.common import config
from application.files import *
   
# default time in mins for auto start/complete delay
TASK_AUTO_START_DELAY_TIME = config.get('TASK_AUTO_START_DELAY_TIME_IN_MINUTES')
TASK_AUTO_COMPLETE_DELAY_TIME = config.get('TASK_AUTO_COMPLETE_DELAY_TIME_IN_MINUTES')
DEFAULT_PENDING_REVIEW_REMINDER_ATTEMPTS = config.get('PENDING_REVIEW_REMINDER_ATTEMPTS')
DEFAULT_DAY_TO_START_CALENDER_WEEK_FROM = config.get('DEFAULT_DAY_TO_START_CALENDER_WEEK_FROM')
DEFAULT_DAY_TO_END_CALENDER_WEEK_ON = config.get('DEFAULT_DAY_TO_END_CALENDER_WEEK_ON')
USER_SHARD_COUNT = config.get('USER_SHARD_COUNT')

DEFAULT_PENDING_REVIEW_REMINDER_ATTEMPTS = config.get('PENDING_REVIEW_REMINDER_ATTEMPTS')


def convert_companytype_to_text(type):
    if type == CompanyType.MOVING:
        return 'MOVING'
    elif type == CompanyType.FOODDELIVERY:
        return 'FOODDELIVERY'
    elif type == CompanyType.MAIDSERVICE:
        return 'MAIDSERVICE'
    elif type == CompanyType.DELIVERY:
        return 'DELIVERY'
    elif type == CompanyType.HOMECARE:
        return 'HOMECARE'
    elif type == CompanyType.OTHER:
        return 'OTHER'
    elif type == CompanyType.SERVICE:
        return 'SERVICE'
    elif type == CompanyType.COMMERCIALSERVICES:
        return 'COMMERCIALSERVICES'
    elif type == CompanyType.CONSTRUCTIONS:
        return 'CONSTRUCTIONS'
    elif type == CompanyType.DELIVERYLOGISTICS:
        return 'DELIVERYLOGISTICS'
    elif type == CompanyType.EVENT:
        return 'EVENT'
    elif type == CompanyType.FIELDHEALTHCARE:
        return 'FIELDHEALTHCARE'
    elif type == CompanyType.FIELDSALES:
        return 'FIELDSALES'
    elif type == CompanyType.HOMESERVICES:
        return 'HOMESERVICES'
    elif type == CompanyType.INSPECTIONS:
        return 'INSPECTIONS'
    elif type == CompanyType.INTERNETSERVICEPROVIDER:
        return 'INTERNETSERVICEPROVIDER'
    elif type == CompanyType.SECURITY:
        return 'SECURITY'
    elif type == CompanyType.SOLAR:
        return 'SOLAR'
    elif type == CompanyType.UTILITY:
        return 'UTILITY'
    elif type == CompanyType.ROOFING:
        return 'ROOFING'
    else:
        return 'OTHER'
    
class CompanyType:
    MOVING = 1001
    FOODDELIVERY = 1002
    MAIDSERVICE = 1003
    OTHER = 1004
    DELIVERY = 1005
    HOMECARE = 1006
    SERVICE = 1007
    COMMERCIALSERVICES = 1008
    CONSTRUCTIONS = 1009
    DELIVERYLOGISTICS = 1010
    EVENT = 1011
    FIELDHEALTHCARE = 1012
    FIELDSALES = 1013
    HOMESERVICES = 1014
    INSPECTIONS = 1015
    INTERNETSERVICEPROVIDER = 1016
    SECURITY = 1017
    SOLAR = 1018
    UTILITY = 1019
    ROOFING = 1020


class CompanyProfile(models.Model):
    DEFAULT_TEMPLATES = [
        {
            'company_type': CompanyType.FOODDELIVERY,
            'name': convert_companytype_to_text(CompanyType.FOODDELIVERY),
            'statuses': [
                TaskStatusType.ENROUTE,
                TaskStatusType.COMPLETE,
                TaskStatusType.CANCELLED,
                TaskStatusType.EXCEPTION,
            ],
            'disable_auto_start_complete': True,
            'auto_start_delay_time': TASK_AUTO_START_DELAY_TIME,
            'auto_complete_delay_time': TASK_AUTO_COMPLETE_DELAY_TIME
        },
        {
            'company_type': CompanyType.DELIVERY,
            'name': convert_companytype_to_text(CompanyType.DELIVERY),
            'statuses': [
                TaskStatusType.CONFIRMED,
                TaskStatusType.PREPARING,
                TaskStatusType.READYFORPICKUP,
                TaskStatusType.ENROUTE,
                TaskStatusType.COMPLETE,
                TaskStatusType.CANCELLED,
                TaskStatusType.EXCEPTION,
            ],
            'disable_auto_start_complete': True,
            'auto_start_delay_time': TASK_AUTO_START_DELAY_TIME,
            'auto_complete_delay_time': TASK_AUTO_COMPLETE_DELAY_TIME
        },
        {
            'company_type': CompanyType.MOVING,
            'name': convert_companytype_to_text(CompanyType.MOVING),
            'statuses': [
                TaskStatusType.ENROUTE,
                TaskStatusType.STARTED,
                TaskStatusType.COMPLETE,
                TaskStatusType.CANCELLED,
                TaskStatusType.EXCEPTION,
            ],
            'disable_auto_start_complete': True,
            'auto_start_delay_time': TASK_AUTO_START_DELAY_TIME,
            'auto_complete_delay_time': TASK_AUTO_COMPLETE_DELAY_TIME
        },
        {
            'company_type': CompanyType.MAIDSERVICE,
            'name': convert_companytype_to_text(CompanyType.MAIDSERVICE),
            'statuses': [
                TaskStatusType.ENROUTE,
                TaskStatusType.STARTED,
                TaskStatusType.COMPLETE,
                TaskStatusType.CANCELLED,
                TaskStatusType.EXCEPTION,
            ],
            'disable_auto_start_complete': True,
            'auto_start_delay_time': TASK_AUTO_START_DELAY_TIME,
            'auto_complete_delay_time': TASK_AUTO_COMPLETE_DELAY_TIME
        },
        {
            'company_type': CompanyType.HOMECARE,
            'name': convert_companytype_to_text(CompanyType.HOMECARE),
            'statuses': [
                TaskStatusType.ENROUTE,
                TaskStatusType.STARTED,
                TaskStatusType.COMPLETE,
                TaskStatusType.CANCELLED,
                TaskStatusType.EXCEPTION,
            ],
            'disable_auto_start_complete': True,
            'auto_start_delay_time': TASK_AUTO_START_DELAY_TIME,
            'auto_complete_delay_time': TASK_AUTO_COMPLETE_DELAY_TIME
        },
        {
            'company_type': CompanyType.SERVICE,
            'name': convert_companytype_to_text(CompanyType.SERVICE),
            'statuses': [
                TaskStatusType.ENROUTE,
                TaskStatusType.STARTED,
                TaskStatusType.COMPLETE,
                TaskStatusType.CANCELLED,
                TaskStatusType.EXCEPTION,
            ],
            'disable_auto_start_complete': True,
            'auto_start_delay_time': TASK_AUTO_START_DELAY_TIME,
            'auto_complete_delay_time': TASK_AUTO_COMPLETE_DELAY_TIME
        },
        {
            'company_type': CompanyType.OTHER,
            'name': convert_companytype_to_text(CompanyType.OTHER),
            'statuses': [
                TaskStatusType.ENROUTE,
                TaskStatusType.STARTED,
                TaskStatusType.COMPLETE,
                TaskStatusType.CANCELLED,
                TaskStatusType.EXCEPTION,
            ],
            'disable_auto_start_complete': True,
            'auto_start_delay_time': TASK_AUTO_START_DELAY_TIME,
            'auto_complete_delay_time': TASK_AUTO_COMPLETE_DELAY_TIME
        },
        {
            'company_type': CompanyType.DELIVERYLOGISTICS,
            'name': convert_companytype_to_text(CompanyType.DELIVERYLOGISTICS),
            'statuses': [
                TaskStatusType.CONFIRMED,
                TaskStatusType.PREPARING,
                TaskStatusType.READYFORPICKUP,
                TaskStatusType.ENROUTE,
                TaskStatusType.COMPLETE,
                TaskStatusType.CANCELLED,
                TaskStatusType.EXCEPTION,
            ],
            'disable_auto_start_complete': True,
            'auto_start_delay_time': TASK_AUTO_START_DELAY_TIME,
            'auto_complete_delay_time': TASK_AUTO_COMPLETE_DELAY_TIME
        },
        {
            'company_type': CompanyType.COMMERCIALSERVICES,
            'name': convert_companytype_to_text(CompanyType.COMMERCIALSERVICES),
            'statuses': [
                TaskStatusType.ENROUTE,
                TaskStatusType.STARTED,
                TaskStatusType.COMPLETE,
                TaskStatusType.CANCELLED,
                TaskStatusType.EXCEPTION,
            ],
            'disable_auto_start_complete': True,
            'auto_start_delay_time': TASK_AUTO_START_DELAY_TIME,
            'auto_complete_delay_time': TASK_AUTO_COMPLETE_DELAY_TIME
        },
        {
            'company_type': CompanyType.CONSTRUCTIONS,
            'name': convert_companytype_to_text(CompanyType.CONSTRUCTIONS),
            'statuses': [
                TaskStatusType.ENROUTE,
                TaskStatusType.STARTED,
                TaskStatusType.COMPLETE,
                TaskStatusType.CANCELLED,
                TaskStatusType.EXCEPTION,
            ],
            'disable_auto_start_complete': True,
            'auto_start_delay_time': TASK_AUTO_START_DELAY_TIME,
            'auto_complete_delay_time': TASK_AUTO_COMPLETE_DELAY_TIME
        },
        {
            'company_type': CompanyType.EVENT,
            'name': convert_companytype_to_text(CompanyType.EVENT),
            'statuses': [
                TaskStatusType.ENROUTE,
                TaskStatusType.STARTED,
                TaskStatusType.COMPLETE,
                TaskStatusType.CANCELLED,
                TaskStatusType.EXCEPTION,
            ],
            'disable_auto_start_complete': True,
            'auto_start_delay_time': TASK_AUTO_START_DELAY_TIME,
            'auto_complete_delay_time': TASK_AUTO_COMPLETE_DELAY_TIME
        },
        {
            'company_type': CompanyType.FIELDHEALTHCARE,
            'name': convert_companytype_to_text(CompanyType.FIELDHEALTHCARE),
            'statuses': [
                TaskStatusType.ENROUTE,
                TaskStatusType.STARTED,
                TaskStatusType.COMPLETE,
                TaskStatusType.CANCELLED,
                TaskStatusType.EXCEPTION,
            ],
            'disable_auto_start_complete': True,
            'auto_start_delay_time': TASK_AUTO_START_DELAY_TIME,
            'auto_complete_delay_time': TASK_AUTO_COMPLETE_DELAY_TIME
        },
        {
            'company_type': CompanyType.FIELDSALES,
            'name': convert_companytype_to_text(CompanyType.FIELDSALES),
            'statuses': [
                TaskStatusType.ENROUTE,
                TaskStatusType.STARTED,
                TaskStatusType.COMPLETE,
                TaskStatusType.CANCELLED,
                TaskStatusType.EXCEPTION,
            ],
            'disable_auto_start_complete': True,
            'auto_start_delay_time': TASK_AUTO_START_DELAY_TIME,
            'auto_complete_delay_time': TASK_AUTO_COMPLETE_DELAY_TIME
        },
        {
            'company_type': CompanyType.HOMESERVICES,
            'name': convert_companytype_to_text(CompanyType.HOMESERVICES),
            'statuses': [
                TaskStatusType.ENROUTE,
                TaskStatusType.STARTED,
                TaskStatusType.COMPLETE,
                TaskStatusType.CANCELLED,
                TaskStatusType.EXCEPTION,
            ],
            'disable_auto_start_complete': True,
            'auto_start_delay_time': TASK_AUTO_START_DELAY_TIME,
            'auto_complete_delay_time': TASK_AUTO_COMPLETE_DELAY_TIME
        },
        {
            'company_type': CompanyType.INSPECTIONS,
            'name': convert_companytype_to_text(CompanyType.INSPECTIONS),
            'statuses': [
                TaskStatusType.ENROUTE,
                TaskStatusType.STARTED,
                TaskStatusType.COMPLETE,
                TaskStatusType.CANCELLED,
                TaskStatusType.EXCEPTION,
            ],
            'disable_auto_start_complete': True,
            'auto_start_delay_time': TASK_AUTO_START_DELAY_TIME,
            'auto_complete_delay_time': TASK_AUTO_COMPLETE_DELAY_TIME
        },
        {
            'company_type': CompanyType.INTERNETSERVICEPROVIDER,
            'name': convert_companytype_to_text(CompanyType.INTERNETSERVICEPROVIDER),
            'statuses': [
                TaskStatusType.ENROUTE,
                TaskStatusType.STARTED,
                TaskStatusType.COMPLETE,
                TaskStatusType.CANCELLED,
                TaskStatusType.EXCEPTION,
            ],
            'disable_auto_start_complete': True,
            'auto_start_delay_time': TASK_AUTO_START_DELAY_TIME,
            'auto_complete_delay_time': TASK_AUTO_COMPLETE_DELAY_TIME
        },
        {
            'company_type': CompanyType.SECURITY,
            'name': convert_companytype_to_text(CompanyType.SECURITY),
            'statuses': [
                TaskStatusType.ENROUTE,
                TaskStatusType.STARTED,
                TaskStatusType.COMPLETE,
                TaskStatusType.CANCELLED,
                TaskStatusType.EXCEPTION,
            ],
            'disable_auto_start_complete': True,
            'auto_start_delay_time': TASK_AUTO_START_DELAY_TIME,
            'auto_complete_delay_time': TASK_AUTO_COMPLETE_DELAY_TIME
        },
        {
            'company_type': CompanyType.SOLAR,
            'name': convert_companytype_to_text(CompanyType.SOLAR),
            'statuses': [
                TaskStatusType.ENROUTE,
                TaskStatusType.STARTED,
                TaskStatusType.COMPLETE,
                TaskStatusType.CANCELLED,
                TaskStatusType.EXCEPTION,
            ],
            'disable_auto_start_complete': True,
            'auto_start_delay_time': TASK_AUTO_START_DELAY_TIME,
            'auto_complete_delay_time': TASK_AUTO_COMPLETE_DELAY_TIME
        },
        {
            'company_type': CompanyType.UTILITY,
            'name': convert_companytype_to_text(CompanyType.UTILITY),
            'statuses': [
                TaskStatusType.ENROUTE,
                TaskStatusType.STARTED,
                TaskStatusType.COMPLETE,
                TaskStatusType.CANCELLED,
                TaskStatusType.EXCEPTION,
            ],
            'disable_auto_start_complete': True,
            'auto_start_delay_time': TASK_AUTO_START_DELAY_TIME,
            'auto_complete_delay_time': TASK_AUTO_COMPLETE_DELAY_TIME
        },
        {
            'company_type': CompanyType.ROOFING,
            'name': convert_companytype_to_text(CompanyType.ROOFING),
            'statuses': [
                TaskStatusType.ENROUTE,
                TaskStatusType.STARTED,
                TaskStatusType.COMPLETE,
                TaskStatusType.CANCELLED,
                TaskStatusType.EXCEPTION,
            ],
            'disable_auto_start_complete': True,
            'auto_start_delay_time': TASK_AUTO_START_DELAY_TIME,
            'auto_complete_delay_time': TASK_AUTO_COMPLETE_DELAY_TIME
        }

    ]
    TYPE_CHOICES = [
         CompanyType.MOVING,
            CompanyType.DELIVERY,
            CompanyType.FOODDELIVERY,
            CompanyType.MAIDSERVICE,
            CompanyType.HOMECARE,
            CompanyType.SERVICE,
            CompanyType.OTHER,
            CompanyType.COMMERCIALSERVICES,
            CompanyType.CONSTRUCTIONS,
            CompanyType.DELIVERYLOGISTICS,
            CompanyType.EVENT,
            CompanyType.FIELDHEALTHCARE,
            CompanyType.FIELDSALES,
            CompanyType.HOMESERVICES,
            CompanyType.INSPECTIONS,
            CompanyType.INTERNETSERVICEPROVIDER,
            CompanyType.SECURITY,
            CompanyType.SOLAR,
            CompanyType.UTILITY,
            CompanyType.ROOFING]
    # In Django, the choices attribute of a model field is designed to include both 
    # the value and a human-readable label (display text)
    company_type = models.IntegerField(choices=[(x, x) for x in TYPE_CHOICES], default=CompanyType.SERVICE)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    pending_review_reminder_attempts = models.IntegerField(default=DEFAULT_PENDING_REVIEW_REMINDER_ATTEMPTS)

    @classmethod
    def by_user(cls, user_id):
        # NOTE:
        # In future all profiles by default will have trial_expiration_date
        # and this code will be removed
        # return cls.query(cls.owner == user_id)
        return cls.objects.filter(owner=user_id)

    def get_template_based_on_company_type(self, company_type):
        for template in self.DEFAULT_TEMPLATES:
            if template['company_type'] == company_type:
                return template
            
