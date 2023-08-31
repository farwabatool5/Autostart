# from files import *
from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.db.models import Q
import logging
from application.files import *

def convert_permission_group_id_to_permission_group_title(permission_group_id):
    if permission_group_id == UserPermissionGroups.ASSUMED_DEFAULT_PERMISSION_GROUP_ID:
        return PermissionGroups.DEFAULT
    elif permission_group_id == UserPermissionGroups.ADMIN_PERMISSION_GROUP_ID:
        return PermissionGroups.ADMIN
    elif permission_group_id == UserPermissionGroups.SCHEDULER_PERMISSION_GROUP_ID:
        return PermissionGroups.SCHEDULER
    elif permission_group_id == UserPermissionGroups.FIELD_CREW_PERMISSION_GROUP_ID:
        return PermissionGroups.FIELD_CREW
    elif permission_group_id == UserPermissionGroups.LIMITED_ACCESS_PERMISSION_GROUP_ID:
        return PermissionGroups.LIMITED_ACCESS
    elif permission_group_id == UserPermissionGroups.VIEWER_PERMISSION_GROUP_ID:
        return PermissionGroups.VIEWER
    elif permission_group_id == UserPermissionGroups.TEAM_LEAD_PERMISSION_GROUP_ID:
        return PermissionGroups.TEAM_LEAD
    elif permission_group_id == UserPermissionGroups.PROJECT_COORDINATOR_PERMISSION_GROUP_ID:
        return PermissionGroups.PROJECT_COORDINATOR
    elif permission_group_id == UserPermissionGroups.BOOKING_ONLY_PERMISSION_GROUP_ID:
        return PermissionGroups.BOOKING_ONLY
    elif permission_group_id == UserPermissionGroups.CUSTOMER_PERMISSION_GROUP_ID:
        return PermissionGroups.CUSTOMER
    else:
        return None


class PermissionGroupType():
    DEFAULT = 1
    OPTIONAL = 2


class Permissions:
    COMPANY                             = 'COMPANY'
    VIEW_SETTING                        = 'VIEW_SETTING'
    VIEW_ACCOUNT_SETTING                = 'VIEW_ACCOUNT_SETTING'
    EDIT_ACCOUNT_SETTING                = 'EDIT_ACCOUNT_SETTING'
    VIEW_PLAN_SETTING                   = 'VIEW_PLAN_SETTING'
    EDIT_PLAN_SETTING                   = 'EDIT_PLAN_SETTING'
    VIEW_CUSTOMER_SETTING               = 'VIEW_CUSTOMER_SETTING'
    EDIT_CUSTOMER_SETTING               = 'EDIT_CUSTOMER_SETTING'
    VIEW_PASSWORD_SETTING               = 'VIEW_PASSWORD_SETTING'
    EDIT_PASSWORD_SETTING               = 'EDIT_PASSWORD_SETTING'
    ADMIN_TASKS                         = 'ADMIN_TASKS'
    ACCESS_API                          = 'ACCESS_API'
    VIEW_ALL_TASKS                      = 'VIEW_ALL_TASKS'
    VIEW_ASSIGNED_TASKS                 = 'VIEW_ASSIGNED_TASKS'
    EDIT_ASSIGNED_TASKS                 = 'EDIT_ASSIGNED_TASKS'
    EDIT_OWN_CREATED_TASK               = 'EDIT_OWN_CREATED_TASK'
    ADD_BOOKING_ONLY_TASK               = 'ADD_BOOKING_ONLY_TASK'
    DELETE_OWN_CREATED_TASK             = 'DELETE_OWN_CREATED_TASK'
    VIEW_CUSTOMER_TASKS                 = 'VIEW_CUSTOMER_TASKS'
    VIEW_FULL_TEAM_MEMBER_DETAILS       = 'VIEW_FULL_TEAM_MEMBER_DETAILS'
    VIEW_LIMITED_TEAM_MEMBER_DETAILS    = 'VIEW_LIMITED_TEAM_MEMBER_DETAILS'
    ADD_TEAM_MEMBER                     = 'ADD_TEAM_MEMBER'
    EDIT_TEAM_MEMBER                    = 'EDIT_TEAM_MEMBER'
    EDIT_TEAM_MEMBER_PERMISSION         = 'EDIT_TEAM_MEMBER_PERMISSION'
    DELETE_TEAM_MEMBER                  = 'DELETE_TEAM_MEMBER'
    VIEW_QR_CODE                        = 'VIEW_QR_CODE'
    ADD_QR_CODE                         = 'ADD_QR_CODE'
    EDIT_QR_CODE                        = 'EDIT_QR_CODE'
    DELETE_QR_CODE                      = 'DELETE_QR_CODE'
    VIEW_CUSTOMER                       = 'VIEW_CUSTOMER'
    ADD_CUSTOMER                        = 'ADD_CUSTOMER'
    EDIT_CUSTOMER                       = 'EDIT_CUSTOMER'
    DELETE_CUSTOMER                     = 'DELETE_CUSTOMER'
    VIEW_OWN_CUSTOMER                   = 'VIEW_OWN_CUSTOMER'
    VIEW_FULL_EQUIPMENT_DETAILS         = 'VIEW_FULL_EQUIPMENT_DETAILS'
    VIEW_LIMITED_EQUIPMENT_DETAILS      = 'VIEW_LIMITED_EQUIPMENT_DETAILS'
    ADD_EQUIPMENT                       = 'ADD_EQUIPMENT'
    EDIT_EQUIPMENT                      = 'EDIT_EQUIPMENT'
    DELETE_EQUIPMENT                    = 'DELETE_EQUIPMENT'
    ADD_TASK                            = 'ADD_TASK'
    ADD_TASK_FILE                       = 'ADD_TASK_FILE'
    EDIT_TASK                           = 'EDIT_TASK'
    DELETE_TASK                         = 'DELETE_TASK'
    ADD_TASK_STATUS                     = 'ADD_TASK_STATUS'
    VIEW_TASK_STATUS                    = 'VIEW_TASK_STATUS'
    EDIT_TASK_STATUS                    = 'EDIT_TASK_STATUS'
    DELETE_TASK_STATUS                  = 'DELETE_TASK_STATUS'
    ADD_TASK_STATUS_ON_OWN_CREATED_TASK = 'ADD_TASK_STATUS_ON_OWN_CREATED_TASK'
    VIEW_TASK_STATUS_ON_OWN_CREATED_TASK = 'VIEW_TASK_STATUS_ON_OWN_CREATED_TASK'
    EDIT_TASK_STATUS_ON_OWN_CREATED_TASK = 'EDIT_TASK_STATUS_ON_OWN_CREATED_TASK'
    DELETE_TASK_STATUS_ON_OWN_CREATED_TASK = 'DELETE_TASK_STATUS_ON_OWN_CREATED_TASK'
    VIEW_REPORTING                      = 'VIEW_REPORTING'
    VIEW_TASK_FULL_DETAILS              = 'VIEW_TASK_FULL_DETAILS'
    VIEW_TASK_LIMITED_DETAILS           = 'VIEW_TASK_LIMITED_DETAILS'
    SHOW_OWN_ACTIVITY_STREAM            = 'SHOW_OWN_ACTIVITY_STREAM'
    SHOW_ALL_ACTIVITY_STREAM            = 'SHOW_ALL_ACTIVITY_STREAM'
    VIEW_TEMPLATE                       = 'VIEW_TEMPLATE'
    ADD_TEMPLATE                        = 'ADD_TEMPLATE'
    EDIT_TEMPLATE                       = 'EDIT_TEMPLATE'
    DELETE_TEMPLATE                     = 'DELETE_TEMPLATE'
    VIEW_RESOURCE_TEMPLATE              = 'VIEW_RESOURCE_TEMPLATE'
    ADD_RESOURCE_TEMPLATE               = 'ADD_RESOURCE_TEMPLATE'
    EDIT_RESOURCE_TEMPLATE              = 'EDIT_RESOURCE_TEMPLATE'
    DELETE_RESOURCE_TEMPLATE            = 'DELETE_RESOURCE_TEMPLATE'
    VIEW_CUSTOMER_TEMPLATE              = 'VIEW_CUSTOMER_TEMPLATE'
    ADD_CUSTOMER_TEMPLATE               = 'ADD_CUSTOMER_TEMPLATE'
    EDIT_CUSTOMER_TEMPLATE              = 'EDIT_CUSTOMER_TEMPLATE'
    DELETE_CUSTOMER_TEMPLATE            = 'DELETE_CUSTOMER_TEMPLATE'
    VIEW_CUSTOM_MESSGAE                 = 'VIEW_CUSTOM_MESSGAE'
    ADD_CUSTOM_MESSGAE                  = 'ADD_CUSTOM_MESSGAE'
    EDIT_CUSTOM_MESSGAE                 = 'EDIT_CUSTOM_MESSGAE'
    DELETE_CUSTOM_MESSGAE               = 'DELETE_CUSTOM_MESSGAE'
    VIEW_TEAM_CONFIRMATION_DATA         = 'VIEW_TEAM_CONFIRMATION_DATA'
    ADD_GROUP                           = 'ADD_GROUP'
    EDIT_GROUP                          = 'EDIT_GROUP'
    DELETE_GROUP                        = 'DELETE_GROUP'
    VIEW_GROUP                          = 'VIEW_GROUP'
    ASSIGN_GROUPS                       = 'ASSIGN_GROUPS'
    ASSIGN_MANAGED_GROUPS               = 'ASSIGN_MANAGED_GROUPS'
    VIEW_ALL_GROUPS_DATA                = 'VIEW_ALL_GROUPS_DATA'
    VIEW_MANAGED_GROUPS_DATA            = 'VIEW_MANAGED_GROUPS_DATA'
    VIEW_ASSIGNED_GROUPS                = 'VIEW_ASSIGNED_GROUPS'
    EDIT_ALL_GROUPS_DATA                = 'EDIT_ALL_GROUPS_DATA'
    EDIT_MANAGED_GROUPS_DATA            = 'EDIT_MANAGED_GROUPS_DATA'
    DELETE_ALL_GROUPS_DATA              = 'DELETE_ALL_GROUPS_DATA'
    DELETE_MANAGED_GROUPS_DATA          = 'DELETE_MANAGED_GROUPS_DATA'
    ADD_TASK_ROUTE                      = 'ADD_TASK_ROUTE'
    EDIT_TASK_ROUTE                     = 'EDIT_TASK_ROUTE'
    DELETE_TASK_ROUTE                   = 'DELETE_TASK_ROUTE'
    VIEW_TASK_ROUTE                     = 'VIEW_TASK_ROUTE'
    ADD_WORKER_REQUEST                  = 'ADD_WORKER_REQUEST'
    EDIT_WORKER_REQUEST                 = 'EDIT_WORKER_REQUEST'
    DELETE_WORKER_REQUEST               = 'DELETE_WORKER_REQUEST'
    VIEW_WORKER_REQUEST                 = 'VIEW_WORKER_REQUEST'
    ADD_EXTERNAL_INTEGRATION            = 'ADD_EXTERNAL_INTEGRATION'
    EDIT_EXTERNAL_INTEGRATION           = 'EDIT_EXTERNAL_INTEGRATION'
    DELETE_EXTERNAL_INTEGRATION         = 'DELETE_EXTERNAL_INTEGRATION'
    VIEW_EXTERNAL_INTEGRATION           = 'VIEW_EXTERNAL_INTEGRATION'
    TRIGGER_EXTERNAL_INTEGRATION_DATA_FETCH = 'TRIGGER_EXTERNAL_INTEGRATION_DATA_FETCH'
    VIEW_TASK_LIST_VIEW_COLUMN_FILTERS  = 'VIEW_TASK_LIST_VIEW_COLUMN_FILTERS'
    RESET_PASSWORD                      = 'RESET_PASSWORD'
    VIEW_FULL_CUSTOMER_DETAILS          = 'VIEW_FULL_CUSTOMER_DETAILS'
    VIEW_LIMITED_CUSTOMER_DETAILS       = 'VIEW_LIMITED_CUSTOMER_DETAILS'
    ADD_DEFAULT_INVENTORY               = 'ADD_DEFAULT_INVENTORY'
    EDIT_DEFAULT_INVENTORY              = 'EDIT_DEFAULT_INVENTORY'
    DELETE_DEFAULT_INVENTORY            = 'DELETE_DEFAULT_INVENTORY'
    VIEW_DEFAULT_INVENTORY              = 'VIEW_DEFAULT_INVENTORY'
    ADD_DEFAULT_SUPPLY                  = 'ADD_DEFAULT_SUPPLY'
    EDIT_DEFAULT_SUPPLY                 = 'EDIT_DEFAULT_SUPPLY'
    DELETE_DEFAULT_SUPPLY               = 'DELETE_DEFAULT_SUPPLY'
    VIEW_DEFAULT_SUPPLY                 = 'VIEW_DEFAULT_SUPPLY'
    ADD_TASK_INVENTORY                  = 'ADD_TASK_INVENTORY'
    EDIT_TASK_INVENTORY                 = 'EDIT_TASK_INVENTORY'
    DELETE_TASK_INVENTORY               = 'DELETE_TASK_INVENTORY'
    VIEW_TASK_INVENTORY                 = 'VIEW_TASK_INVENTORY'
    ADD_TASK_SUPPLY                     = 'ADD_TASK_SUPPLY'
    EDIT_TASK_SUPPLY                    = 'EDIT_TASK_SUPPLY'
    DELETE_TASK_SUPPLY                  = 'DELETE_TASK_SUPPLY'
    VIEW_TASK_SUPPLY                    = 'VIEW_TASK_SUPPLY'
    ADD_TASK_INVENTORY_LABEL            = 'ADD_TASK_INVENTORY_LABEL'
    EDIT_TASK_INVENTORY_LABEL           = 'EDIT_TASK_INVENTORY_LABEL'
    DELETE_TASK_INVENTORY_LABEL         = 'DELETE_TASK_INVENTORY_LABEL'
    VIEW_TASK_INVENTORY_LABEL           = 'VIEW_TASK_INVENTORY_LABEL'
    VIEW_TASK_ROUTE_EDITING             = 'VIEW_TASK_ROUTE_EDITING'
    EDIT_TASK_ROUTE_VIA_ROUTE_EDITING   = 'EDIT_TASK_ROUTE_VIA_ROUTE_EDITING'
    REVERT_TASK_ROUTE                   = 'REVERT_TASK_ROUTE'
    PUBLISH_TASK_ROUTE                  = 'PUBLISH_TASK_ROUTE'
    VIEW_TASK_DRAFT                     = 'VIEW_TASK_DRAFT'
    LOCK_UNLOCK_TASK_SUPPLIES           = 'LOCK_UNLOCK_TASK_SUPPLIES'
    ADD_FORM                            = 'ADD_FORM'
    EDIT_FORM                           = 'EDIT_FORM'
    DELETE_FORM                         = 'DELETE_FORM'
    VIEW_FORM                           = 'VIEW_FORM'
    EDIT_FORM_SUBMISSION                = 'EDIT_FORM_SUBMISSION'
    DELETE_FORM_SUBMISSION              = 'DELETE_FORM_SUBMISSION'
    VIEW_FORM_SUBMISSION                = 'VIEW_FORM_SUBMISSION'
    CAN_UN_LOCK_FORM_SUBMISSION         = 'CAN_UN_LOCK_FORM_SUBMISSION'
    VIEW_FORM_OVERVIEW                  = 'VIEW_FORM_OVERVIEW'
    EDIT_OWN_CREATED_TASK_FORM_SUBMISSION   = 'EDIT_OWN_CREATED_TASK_FORM_SUBMISSION'
    VIEW_OWN_CREATED_TASK_FORM_SUBMISSION   = 'VIEW_OWN_CREATED_TASK_FORM_SUBMISSION'
    DELETE_OWN_CREATED_TASK_FORM_SUBMISSION = 'DELETE_OWN_CREATED_TASK_FORM_SUBMISSION'
    VIEW_LINKED_TASK                    = 'VIEW_LINKED_TASK'
    VIEW_LINKED_TASK_META_DATA          = 'VIEW_LINKED_TASK_META_DATA'
    CAN_GET_OAUTH_FLOW_INFO             = 'CAN_GET_OAUTH_FLOW_INFO'
    EDIT_LINKED_TASK                    = 'EDIT_LINKED_TASK'
    DELETE_LINKED_TASK                  = 'DELETE_LINKED_TASK'
    ADD_SKILL                           = 'ADD_SKILL'
    EDIT_SKILL                          = 'EDIT_SKILL'
    DELETE_SKILL                        = 'DELETE_SKILL'
    VIEW_SKILL                          = 'VIEW_SKILL'
    ADD_ITEM                            = 'ADD_ITEM'
    EDIT_ITEM                           = 'EDIT_ITEM'
    DELETE_ITEM                         = 'DELETE_ITEM'
    VIEW_ITEM                           = 'VIEW_ITEM'
    ADD_BOOKING                         = 'ADD_BOOKING'
    EDIT_BOOKING                        = 'EDIT_BOOKING'
    DELETE_BOOKING                      = 'DELETE_BOOKING'
    VIEW_BOOKING                        = 'VIEW_BOOKING'
    VIEW_CUSTOMER_BOOKINGS              = 'VIEW_CUSTOMER_BOOKINGS'
    ADD_BOOKING_SLOT                    = 'ADD_BOOKING_SLOT'
    EDIT_BOOKING_SLOT                   = 'EDIT_BOOKING_SLOT'
    DELETE_BOOKING_SLOT                 = 'DELETE_BOOKING_SLOT'
    VIEW_BOOKING_SLOT                   = 'VIEW_BOOKING_SLOT'
    ADD_BOOKING_OBJECT_RULE             = 'ADD_BOOKING_OBJECT_RULE'
    EDIT_BOOKING_OBJECT_RULE            = 'EDIT_BOOKING_OBJECT_RULE'
    DELETE_BOOKING_OBJECT_RULE          = 'DELETE_BOOKING_OBJECT_RULE'
    VIEW_BOOKING_OBJECT_RULE            = 'VIEW_BOOKING_OBJECT_RULE'
    ADD_BOOKED_SLOT                     = 'ADD_BOOKED_SLOT'
    EDIT_BOOKED_SLOT                    = 'EDIT_BOOKED_SLOT'
    DELETE_BOOKED_SLOT                  = 'DELETE_BOOKED_SLOT'
    VIEW_BOOKED_SLOT                    = 'VIEW_BOOKED_SLOT'
    ADD_CHECKLIST                       = 'ADD_CHECKLIST'
    EDIT_CHECKLIST                      = 'EDIT_CHECKLIST'
    DELETE_CHECKLIST                    = 'DELETE_CHECKLIST'
    VIEW_CHECKLIST                      = 'VIEW_CHECKLIST'
    VIEW_TASK_CHECKLIST                 = 'VIEW_TASK_CHECKLIST'
    ADD_MASTER_ITEM                     = 'ADD_MASTER_ITEM'
    EDIT_MASTER_ITEM                    = 'EDIT_MASTER_ITEM'
    DELETE_MASTER_ITEM                  = 'DELETE_MASTER_ITEM'
    VIEW_MASTER_ITEM                    = 'VIEW_MASTER_ITEM'
    ADD_ITEMS_LIST                      = 'ADD_ITEMS_LIST'
    EDIT_ITEMS_LIST                     = 'EDIT_ITEMS_LIST'
    DELETE_ITEMS_LIST                   = 'DELETE_ITEMS_LIST'
    VIEW_ITEMS_LIST                     = 'VIEW_ITEMS_LIST'
    CAN_GET_SQUARE_MOBILE_AUTHORIZATION_CODE = 'CAN_GET_SQUARE_MOBILE_AUTHORIZATION_CODE'
    ADD_ORDER                           = 'ADD_ORDER'
    EDIT_ORDER                          = 'EDIT_ORDER'
    DELETE_ORDER                        = 'DELETE_ORDER'
    VIEW_ORDER                          = 'VIEW_ORDER'
    VIEW_INVOICE                        = 'VIEW_INVOICE'
    VIEW_ALL_TASK_INVOICE               = 'VIEW_ALL_TASK_INVOICE'
    VIEW_KISOK_DEVICES                  = 'VIEW_KISOK_DEVICES'
    DELETE_KISOK_DEVICE                 = 'DELETE_KISOK_DEVICE'
    EDIT_KISOK_DEVICE                   = 'EDIT_KISOK_DEVICE'
    CAN_VIEW_MAP_VIEW                   = 'CAN_VIEW_MAP_VIEW'
    CAN_VIEW_REVIEWS                    = 'CAN_VIEW_REVIEWS'
    SHOW_OWN_REVIEWS                    = 'SHOW_OWN_REVIEWS'
    SHOW_ALL_REVIEWS                    = 'SHOW_ALL_REVIEWS'
    ADD_STATUS_PRIORITY                 = 'ADD_STATUS_PRIORITY'
    EDIT_STATUS_PRIORITY                = 'EDIT_STATUS_PRIORITY'
    DELETE_STATUS_PRIORITY              = 'DELETE_STATUS_PRIORITY'
    VIEW_STATUS_PRIORITY                = 'VIEW_STATUS_PRIORITY'
    ADD_CUSTOM_WEBHOOK                  = 'ADD_CUSTOM_WEBHOOK'
    EDIT_CUSTOM_WEBHOOK                 = 'EDIT_CUSTOM_WEBHOOK'
    DELETE_CUSTOM_WEBHOOK               = 'DELETE_CUSTOM_WEBHOOK'
    VIEW_CUSTOM_WEBHOOK                 = 'VIEW_CUSTOM_WEBHOOK'
    ADD_CREW_AVAILABILITY_REQUEST       = 'ADD_CREW_AVAILABILITY_REQUEST'
    EDIT_CREW_AVAILABILITY_REQUEST      = 'EDIT_CREW_AVAILABILITY_REQUEST'
    DELETE_CREW_AVAILABILITY_REQUEST    = 'DELETE_CREW_AVAILABILITY_REQUEST'
    VIEW_CREW_AVAILABILITY_REQUEST      = 'VIEW_CREW_AVAILABILITY_REQUEST'
    ADD_ASSIGNED_CREW_AVAILABILITY_REQUEST    = 'ADD_ASSIGNED_CREW_AVAILABILITY_REQUEST'
    EDIT_ASSIGNED_CREW_AVAILABILITY_REQUEST   = 'EDIT_ASSIGNED_CREW_AVAILABILITY_REQUEST'
    DELETE_ASSIGNED_CREW_AVAILABILITY_REQUEST = 'DELETE_ASSIGNED_CREW_AVAILABILITY_REQUEST'
    VIEW_ASSIGNED_CREW_AVAILABILITY_REQUEST   = 'VIEW_ASSIGNED_CREW_AVAILABILITY_REQUEST'
    UPDATE_CREW_AVAILABILITY_REQUEST_STATUS   = 'UPDATE_CREW_AVAILABILITY_REQUEST_STATUS'
    # the below permission is for UI only to distinguish between field crew and team lead
    CAN_ADD_TIME_REPORTING_STATUSES_FOR_OTHER_ASSIGNEES = 'CAN_ADD_TIME_REPORTING_STATUSES_FOR_OTHER_ASSIGNEES'
    GET_MOVERS_SUITE_ORDER              = 'GET_MOVERS_SUITE_ORDER'
    ADD_ACTION_CRON_CONFIG              = 'ADD_ACTION_CRON_CONFIG'
    EDIT_ACTION_CRON_CONFIG             = 'EDIT_ACTION_CRON_CONFIG'
    DELETE_ACTION_CRON_CONFIG           = 'DELETE_ACTION_CRON_CONFIG'
    VIEW_ACTION_CRON_CONFIG             = 'VIEW_ACTION_CRON_CONFIG'
    ADD_ACTION_CRON_CONFIG_STATUS       = 'ADD_ACTION_CRON_CONFIG_STATUS'
    EDIT_ACTION_CRON_CONFIG_STATUS      = 'EDIT_ACTION_CRON_CONFIG_STATUS'
    DELETE_ACTION_CRON_CONFIG_STATUS    = 'DELETE_ACTION_CRON_CONFIG_STATUS'
    VIEW_ACTION_CRON_CONFIG_STATUS      = 'VIEW_ACTION_CRON_CONFIG_STATUS'
    UPDATE_LIMITED_COMPANY_PROFILE      = 'UPDATE_LIMITED_COMPANY_PROFILE'
    INVOKE_RE_MICRO_SERVICE             = 'INVOKE_RE_MICRO_SERVICE'
    INVOKE_EXPORT_TEAM_MEMBER_SERVICE   = 'INVOKE_EXPORT_TEAM_MEMBER_SERVICE'
    INVOKE_EXPORT_TASK_SERVICE          = 'INVOKE_EXPORT_TASK_SERVICE'
    INVOKE_EXPORT_CUSTOMER_SERVICE      = 'INVOKE_EXPORT_CUSTOMER_SERVICE'
    INVOKE_EXPORT_EXTERNAL_INTEGRATION_SERVICE = 'INVOKE_EXPORT_EXTERNAL_INTEGRATION_SERVICE'
    INVOKE_RE_GEO_ADDRESSES_MICRO_SERVICE      = 'INVOKE_RE_GEO_ADDRESSES_MICRO_SERVICE'
    CAN_SEARCH_TASK                     = 'CAN_SEARCH_TASK'
    CAN_SEARCH_ENTITY                   = 'CAN_SEARCH_ENTITY'
    CAN_SEARCH_CUSTOMER                 = 'CAN_SEARCH_CUSTOMER'
    CAN_SEARCH_RESOURCE                 = 'CAN_SEARCH_RESOURCE'
    ADD_ITEMS_GROUPS                    = 'ADD_ITEMS_GROUPS'
    EDIT_ITEMS_GROUPS                   = 'EDIT_ITEMS_GROUPS'
    DELETE_ITEMS_GROUPS                 = 'DELETE_ITEMS_GROUPS'
    VIEW_ITEMS_GROUPS                   = 'VIEW_ITEMS_GROUPS'

    # TODO: Handle Permissions for other models such as Skill, Template, Group, Default Inventory ,
    #  Default Supply, Task Supply, Task Inventory, Task Inventory Label


class PermissionGroups:
    DEFAULT             = 'Default Permissions'
    ADMIN               = 'Admin'
    SCHEDULER           = 'Scheduler'
    FIELD_CREW          = 'Field Crew'
    LIMITED_ACCESS      = 'Limited Access'
    VIEWER              = 'Viewer'
    TEAM_LEAD           = 'Team Lead'
    PROJECT_COORDINATOR = 'Project Coordinator'
    BOOKING_ONLY        = 'Booking Only'
    CUSTOMER            = 'Customer'

    @classmethod
    def get_all_permission_groups(cls):
        return [cls.DEFAULT, cls.ADMIN, cls.SCHEDULER, cls.FIELD_CREW, cls.LIMITED_ACCESS, cls.VIEWER, cls.TEAM_LEAD,
                cls.PROJECT_COORDINATOR, cls.BOOKING_ONLY, cls.CUSTOMER]


class UserPermissionGroups:
    ASSUMED_DEFAULT_PERMISSION_GROUP_ID = 1
    ADMIN_PERMISSION_GROUP_ID = 2
    SCHEDULER_PERMISSION_GROUP_ID = 3
    FIELD_CREW_PERMISSION_GROUP_ID = 4
    LIMITED_ACCESS_PERMISSION_GROUP_ID = 5
    VIEWER_PERMISSION_GROUP_ID = 6
    TEAM_LEAD_PERMISSION_GROUP_ID = 7
    PROJECT_COORDINATOR_PERMISSION_GROUP_ID = 8
    BOOKING_ONLY_PERMISSION_GROUP_ID = 9
    CUSTOMER_PERMISSION_GROUP_ID = 51

    DEFAULT_PERMISSION_GROUP_ID = FIELD_CREW_PERMISSION_GROUP_ID

    _setting_permissions = [
        Permissions.VIEW_SETTING,
        Permissions.VIEW_ACCOUNT_SETTING,
        Permissions.EDIT_ACCOUNT_SETTING,
        Permissions.VIEW_PLAN_SETTING,
        Permissions.EDIT_PLAN_SETTING,
        Permissions.VIEW_CUSTOMER_SETTING,
        Permissions.EDIT_CUSTOMER_SETTING,
        Permissions.VIEW_PASSWORD_SETTING,
        Permissions.EDIT_PASSWORD_SETTING,
        Permissions.ADMIN_TASKS,
        Permissions.ADD_EXTERNAL_INTEGRATION,
        Permissions.EDIT_EXTERNAL_INTEGRATION,
        Permissions.VIEW_EXTERNAL_INTEGRATION,
        Permissions.DELETE_EXTERNAL_INTEGRATION
    ]

    _reporting_permissions = [
        Permissions.VIEW_REPORTING
    ]

    _api_permissions = [
        Permissions.ACCESS_API
    ]

    _team_permissions = [
        Permissions.ADD_TEAM_MEMBER,
        Permissions.EDIT_TEAM_MEMBER,
        Permissions.DELETE_TEAM_MEMBER
    ]

    _skills_permissions = [
        Permissions.ADD_SKILL,
        Permissions.EDIT_SKILL,
        Permissions.DELETE_SKILL,
        Permissions.VIEW_SKILL
    ]

    _permission_permissions = [
        Permissions.EDIT_TEAM_MEMBER_PERMISSION,
    ]

    _customer_permissions = [
        Permissions.VIEW_CUSTOMER,
        Permissions.ADD_CUSTOMER,
        Permissions.EDIT_CUSTOMER,
        Permissions.DELETE_CUSTOMER
    ]

    _equipment_permissions = [
        Permissions.ADD_EQUIPMENT,
        Permissions.EDIT_EQUIPMENT,
        Permissions.DELETE_EQUIPMENT
    ]

    _template_permissions = [
        Permissions.VIEW_TEMPLATE,
        Permissions.ADD_TEMPLATE,
        Permissions.EDIT_TEMPLATE,
        Permissions.DELETE_TEMPLATE
    ]

    _resource_template_permissions = [
        Permissions.VIEW_RESOURCE_TEMPLATE,
        Permissions.ADD_RESOURCE_TEMPLATE,
        Permissions.EDIT_RESOURCE_TEMPLATE,
        Permissions.DELETE_RESOURCE_TEMPLATE
    ]

    _customer_template_permissions = [
        Permissions.VIEW_CUSTOMER_TEMPLATE,
        Permissions.ADD_CUSTOMER_TEMPLATE,
        Permissions.EDIT_CUSTOMER_TEMPLATE,
        Permissions.DELETE_CUSTOMER_TEMPLATE
    ]

    _custom_message_permissions = [
        Permissions.VIEW_CUSTOM_MESSGAE,
        Permissions.ADD_CUSTOM_MESSGAE,
        Permissions.EDIT_CUSTOM_MESSGAE,
        Permissions.DELETE_CUSTOM_MESSGAE
    ]

    _task_permissions = [
        Permissions.ADD_TASK,
        Permissions.EDIT_TASK,
        Permissions.DELETE_TASK,
        Permissions.ADD_TASK_FILE
    ]

    _task_permissions_on_own_created_task = [
        Permissions.EDIT_OWN_CREATED_TASK,
        Permissions.DELETE_OWN_CREATED_TASK,
    ]

    _task_status_permissions = [
        Permissions.ADD_TASK_STATUS,
        Permissions.VIEW_TASK_STATUS,
        Permissions.EDIT_TASK_STATUS,
        Permissions.DELETE_TASK_STATUS
    ]

    _task_status_on_own_created_task_permissions = [
        Permissions.ADD_TASK_STATUS_ON_OWN_CREATED_TASK,
        Permissions.VIEW_TASK_STATUS_ON_OWN_CREATED_TASK,
        Permissions.EDIT_TASK_STATUS_ON_OWN_CREATED_TASK,
        Permissions.DELETE_TASK_STATUS_ON_OWN_CREATED_TASK
    ]

    _team_confirmation_permission = [
        Permissions.VIEW_TEAM_CONFIRMATION_DATA
    ]

    _group_permissions = [
        Permissions.ADD_GROUP,
        Permissions.VIEW_GROUP,
        Permissions.EDIT_GROUP,
        Permissions.DELETE_GROUP
    ]

    _group_usage_permissions = [
        Permissions.ASSIGN_GROUPS,
        Permissions.VIEW_ALL_GROUPS_DATA,
        Permissions.EDIT_ALL_GROUPS_DATA,
        Permissions.DELETE_ALL_GROUPS_DATA
    ]

    _task_route_permissions = [
        Permissions.ADD_TASK_ROUTE,
        Permissions.EDIT_TASK_ROUTE,
        Permissions.DELETE_TASK_ROUTE,
        Permissions.VIEW_TASK_ROUTE
    ]

    _worker_request_permissions = [
        Permissions.ADD_WORKER_REQUEST,
        Permissions.EDIT_WORKER_REQUEST,
        Permissions.DELETE_WORKER_REQUEST,
        Permissions.VIEW_WORKER_REQUEST
    ]

    _route_editing_permissions = [
        Permissions.VIEW_TASK_ROUTE_EDITING,
        Permissions.EDIT_TASK_ROUTE_VIA_ROUTE_EDITING,
        Permissions.REVERT_TASK_ROUTE,
        Permissions.PUBLISH_TASK_ROUTE,
        Permissions.VIEW_TASK_DRAFT
        ]

    _default_inventory_permissions = [
        Permissions.ADD_DEFAULT_INVENTORY,
        Permissions.EDIT_DEFAULT_INVENTORY,
        Permissions.DELETE_DEFAULT_INVENTORY,
        Permissions.VIEW_DEFAULT_INVENTORY

    ]

    _default_supply_permissions = [
        Permissions.ADD_DEFAULT_SUPPLY,
        Permissions.EDIT_DEFAULT_SUPPLY,
        Permissions.DELETE_DEFAULT_SUPPLY,
        Permissions.VIEW_DEFAULT_SUPPLY
    ]

    _task_inventory_permissions = [
        Permissions.ADD_TASK_INVENTORY,
        Permissions.EDIT_TASK_INVENTORY,
        Permissions.DELETE_TASK_INVENTORY,
        Permissions.VIEW_TASK_INVENTORY
    ]

    _task_supply_permissions = [
        Permissions.ADD_TASK_SUPPLY,
        Permissions.EDIT_TASK_SUPPLY,
        Permissions.DELETE_TASK_SUPPLY,
        Permissions.VIEW_TASK_SUPPLY
    ]

    _task_inventory_label_permissions = [
        Permissions.ADD_TASK_INVENTORY_LABEL,
        Permissions.EDIT_TASK_INVENTORY_LABEL,
        Permissions.DELETE_TASK_INVENTORY_LABEL,
        Permissions.VIEW_TASK_INVENTORY_LABEL
    ]

    _form_permissions = [
        Permissions.ADD_FORM,
        Permissions.EDIT_FORM,
        Permissions.DELETE_FORM,
        Permissions.VIEW_FORM
    ]

    _form_submission_permissions = [
        Permissions.EDIT_FORM_SUBMISSION,
        Permissions.DELETE_FORM_SUBMISSION,
        Permissions.VIEW_FORM_SUBMISSION,
        Permissions.CAN_UN_LOCK_FORM_SUBMISSION,
        Permissions.VIEW_FORM_OVERVIEW
    ]

    _form_submission_on_own_created_tasks_permissions = [
        Permissions.EDIT_OWN_CREATED_TASK_FORM_SUBMISSION,
        Permissions.DELETE_OWN_CREATED_TASK_FORM_SUBMISSION,
        Permissions.VIEW_OWN_CREATED_TASK_FORM_SUBMISSION,
        Permissions.CAN_UN_LOCK_FORM_SUBMISSION,
        Permissions.VIEW_FORM_OVERVIEW
    ]

    _self_scheduling_booking_permissions = [
        Permissions.ADD_BOOKING,
        Permissions.EDIT_BOOKING,
        Permissions.DELETE_BOOKING,
        Permissions.VIEW_BOOKING
    ]

    _self_scheduling_booking_slot_permissions = [
        Permissions.ADD_BOOKING_SLOT,
        Permissions.EDIT_BOOKING_SLOT,
        Permissions.DELETE_BOOKING_SLOT,
        Permissions.VIEW_BOOKING_SLOT
    ]

    _self_scheduling_booked_slot_permissions = [
        Permissions.ADD_BOOKED_SLOT,
        Permissions.EDIT_BOOKED_SLOT,
        Permissions.DELETE_BOOKED_SLOT,
        Permissions.VIEW_BOOKED_SLOT
    ]

    _checklist_permissions = [
        Permissions.ADD_CHECKLIST,
        Permissions.EDIT_CHECKLIST,
        Permissions.DELETE_CHECKLIST,
        Permissions.VIEW_CHECKLIST
    ]

    _status_priorities_permissions = [
        Permissions.ADD_STATUS_PRIORITY,
        Permissions.EDIT_STATUS_PRIORITY,
        Permissions.DELETE_STATUS_PRIORITY,
        Permissions.VIEW_STATUS_PRIORITY
    ]

    _custom_webhook_permissions = [
        Permissions.ADD_CUSTOM_WEBHOOK,
        Permissions.EDIT_CUSTOM_WEBHOOK,
        Permissions.DELETE_CUSTOM_WEBHOOK,
        Permissions.VIEW_CUSTOM_WEBHOOK
    ]

    _task_checklist_permissions = [
        Permissions.VIEW_TASK_CHECKLIST
    ]

    _task_items_permissions = [
        Permissions.ADD_ITEM,
        Permissions.EDIT_ITEM,
        Permissions.DELETE_ITEM,
        Permissions.VIEW_ITEM
    ]

    _task_items_group_permissions = [
        Permissions.ADD_ITEMS_GROUPS,
        Permissions.EDIT_ITEMS_GROUPS,
        Permissions.DELETE_ITEMS_GROUPS,
        Permissions.VIEW_ITEMS_GROUPS
    ]

    _items_list_permissions = [
        Permissions.ADD_ITEMS_LIST,
        Permissions.EDIT_ITEMS_LIST,
        Permissions.DELETE_ITEMS_LIST,
        Permissions.VIEW_ITEMS_LIST
    ]

    _master_items_permissions = [
        Permissions.ADD_MASTER_ITEM,
        Permissions.EDIT_MASTER_ITEM,
        Permissions.DELETE_MASTER_ITEM,
        Permissions.VIEW_MASTER_ITEM
    ]

    _action_cron_config_permissions = [
        Permissions.ADD_ACTION_CRON_CONFIG,
        Permissions.EDIT_ACTION_CRON_CONFIG,
        Permissions.DELETE_ACTION_CRON_CONFIG,
        Permissions.VIEW_ACTION_CRON_CONFIG
    ]

    _action_cron_config_status_permissions = [
        Permissions.ADD_ACTION_CRON_CONFIG_STATUS,
        Permissions.EDIT_ACTION_CRON_CONFIG_STATUS,
        Permissions.DELETE_ACTION_CRON_CONFIG_STATUS,
        Permissions.VIEW_ACTION_CRON_CONFIG_STATUS
    ]

    _crew_availability_request_permissions = [
        Permissions.ADD_CREW_AVAILABILITY_REQUEST,
        Permissions.EDIT_CREW_AVAILABILITY_REQUEST,
        Permissions.DELETE_CREW_AVAILABILITY_REQUEST,
        Permissions.VIEW_CREW_AVAILABILITY_REQUEST
    ]

    _assigned_crew_availability_request_permissions = [
        Permissions.ADD_ASSIGNED_CREW_AVAILABILITY_REQUEST,
        Permissions.EDIT_ASSIGNED_CREW_AVAILABILITY_REQUEST,
        Permissions.DELETE_ASSIGNED_CREW_AVAILABILITY_REQUEST,
        Permissions.VIEW_ASSIGNED_CREW_AVAILABILITY_REQUEST
    ]

    # Mutually exclusive permission sets
    _task_view_permissions = [
        Permissions.VIEW_ALL_TASKS,
        Permissions.VIEW_ASSIGNED_TASKS
    ]

    _equipment_view_permissions = [
        Permissions.VIEW_FULL_EQUIPMENT_DETAILS,
        Permissions.VIEW_LIMITED_EQUIPMENT_DETAILS
    ]

    _team_view_permissions = [
        Permissions.VIEW_FULL_TEAM_MEMBER_DETAILS,
        Permissions.VIEW_LIMITED_TEAM_MEMBER_DETAILS
    ]

    _activity_stream_permissions = [
        Permissions.SHOW_ALL_ACTIVITY_STREAM,
        Permissions.SHOW_OWN_ACTIVITY_STREAM
    ]

    _task_details_permissions = [
        Permissions.VIEW_TASK_FULL_DETAILS,
        Permissions.VIEW_TASK_LIMITED_DETAILS
    ]

    _task_customer_view_permission = [
        Permissions.VIEW_FULL_CUSTOMER_DETAILS,
        Permissions.VIEW_LIMITED_CUSTOMER_DETAILS
    ]

    _linked_task_permissions = [
        Permissions.VIEW_LINKED_TASK,
        Permissions.EDIT_LINKED_TASK,
        Permissions.DELETE_LINKED_TASK
    ]

    _qr_code_permissions = [
        Permissions.VIEW_QR_CODE,
        Permissions.ADD_QR_CODE,
        Permissions.EDIT_QR_CODE,
        Permissions.DELETE_QR_CODE
    ]

    _booking_object_rule_permissions = [
        Permissions.VIEW_BOOKING_OBJECT_RULE,
        Permissions.ADD_BOOKING_OBJECT_RULE,
        Permissions.EDIT_BOOKING_OBJECT_RULE,
        Permissions.DELETE_BOOKING_OBJECT_RULE
    ]




    _defined_permission_groups = [
        {   # Permissions of DEFAULT group should always reflect FIELD CREW
            'group_id': ASSUMED_DEFAULT_PERMISSION_GROUP_ID,
            'title': PermissionGroups.DEFAULT,
            'description': 'Default Permissions',
            'type': PermissionGroupType.DEFAULT,
            'permission_tokens': _task_status_permissions + _team_confirmation_permission
            + _task_inventory_permissions + _task_supply_permissions + _task_inventory_label_permissions
            + _default_supply_permissions + _default_inventory_permissions
            + _assigned_crew_availability_request_permissions +
            [Permissions.VIEW_ASSIGNED_TASKS, Permissions.ADD_TASK_FILE, Permissions.SHOW_OWN_ACTIVITY_STREAM,
             Permissions.VIEW_TEMPLATE, Permissions.VIEW_TASK_FULL_DETAILS, Permissions.VIEW_FULL_TEAM_MEMBER_DETAILS,
             Permissions.VIEW_FULL_EQUIPMENT_DETAILS, Permissions.VIEW_PASSWORD_SETTING,
             Permissions.EDIT_PASSWORD_SETTING, Permissions.VIEW_TASK_ROUTE, Permissions.LOCK_UNLOCK_TASK_SUPPLIES,
             Permissions.VIEW_LINKED_TASK, Permissions.VIEW_LINKED_TASK_META_DATA, Permissions.VIEW_FORM_SUBMISSION,
             Permissions.EDIT_FORM_SUBMISSION, Permissions.VIEW_BOOKING_SLOT, Permissions.VIEW_BOOKING,
             Permissions.CAN_GET_SQUARE_MOBILE_AUTHORIZATION_CODE, Permissions.CAN_VIEW_REVIEWS,
             Permissions.SHOW_OWN_REVIEWS, Permissions.VIEW_ITEMS_LIST, Permissions.VIEW_MASTER_ITEM,
             Permissions.INVOKE_RE_GEO_ADDRESSES_MICRO_SERVICE, Permissions.VIEW_RESOURCE_TEMPLATE]
        },
        {
            'group_id': ADMIN_PERMISSION_GROUP_ID,
            'title': PermissionGroups.ADMIN,
            'description': 'Has full access to Settings, Tasks, Team, Customers',
            'type': PermissionGroupType.OPTIONAL,
            'permission_tokens': _setting_permissions + _api_permissions + _team_permissions + _permission_permissions
            + _customer_permissions + _equipment_permissions + _task_permissions + _task_status_permissions
            + _reporting_permissions + _template_permissions + _team_confirmation_permission + _group_permissions
            + _group_usage_permissions + _task_route_permissions + _worker_request_permissions
            + _custom_message_permissions + _route_editing_permissions + _default_inventory_permissions
            + _default_supply_permissions + _task_inventory_permissions + _task_supply_permissions
            + _task_inventory_label_permissions + _form_permissions + _form_submission_permissions
            + _skills_permissions + _self_scheduling_booking_permissions + _self_scheduling_booking_slot_permissions
            + _self_scheduling_booked_slot_permissions + _checklist_permissions + _task_checklist_permissions
            + _task_items_permissions + _status_priorities_permissions + _items_list_permissions
            + _master_items_permissions + _custom_webhook_permissions + _action_cron_config_permissions
            + _action_cron_config_status_permissions + _crew_availability_request_permissions + _qr_code_permissions
            + _customer_template_permissions + _task_items_group_permissions + _resource_template_permissions
            + _booking_object_rule_permissions +
            [Permissions.VIEW_ALL_TASKS, Permissions.SHOW_ALL_ACTIVITY_STREAM, Permissions.VIEW_TASK_FULL_DETAILS,
             Permissions.VIEW_FULL_TEAM_MEMBER_DETAILS, Permissions.VIEW_FULL_EQUIPMENT_DETAILS,
             Permissions.EDIT_PASSWORD_SETTING, Permissions.TRIGGER_EXTERNAL_INTEGRATION_DATA_FETCH,
             Permissions.VIEW_TASK_LIST_VIEW_COLUMN_FILTERS, Permissions.RESET_PASSWORD,
             Permissions.VIEW_FULL_CUSTOMER_DETAILS, Permissions.VIEW_LINKED_TASK_META_DATA,
             Permissions.CAN_GET_OAUTH_FLOW_INFO, Permissions.CAN_VIEW_MAP_VIEW,
             Permissions.CAN_GET_SQUARE_MOBILE_AUTHORIZATION_CODE, Permissions.ADD_ORDER, Permissions.EDIT_ORDER,
             Permissions.VIEW_ORDER, Permissions.DELETE_ORDER, Permissions.VIEW_KISOK_DEVICES,
             Permissions.DELETE_KISOK_DEVICE, Permissions.EDIT_KISOK_DEVICE, Permissions.CAN_VIEW_REVIEWS,
             Permissions.SHOW_ALL_REVIEWS, Permissions.GET_MOVERS_SUITE_ORDER,
             Permissions.UPDATE_CREW_AVAILABILITY_REQUEST_STATUS, Permissions.UPDATE_LIMITED_COMPANY_PROFILE,
             Permissions.VIEW_INVOICE, Permissions.INVOKE_RE_MICRO_SERVICE,
             Permissions.INVOKE_EXPORT_TEAM_MEMBER_SERVICE, Permissions.VIEW_ALL_TASK_INVOICE,
             Permissions.INVOKE_EXPORT_TASK_SERVICE, Permissions.INVOKE_EXPORT_CUSTOMER_SERVICE,
             Permissions.INVOKE_EXPORT_EXTERNAL_INTEGRATION_SERVICE, Permissions.INVOKE_RE_GEO_ADDRESSES_MICRO_SERVICE,
             Permissions.CAN_SEARCH_TASK, Permissions.CAN_SEARCH_CUSTOMER, Permissions.CAN_SEARCH_ENTITY,
             Permissions.CAN_SEARCH_RESOURCE]
        },
        {
            'group_id': SCHEDULER_PERMISSION_GROUP_ID,
            'title': PermissionGroups.SCHEDULER,
            'description': 'Has full access to Tasks, Team, Customers',
            'type': PermissionGroupType.OPTIONAL,
            'permission_tokens': _team_permissions + _customer_permissions + _equipment_permissions + _task_permissions
            + _task_status_permissions + _team_confirmation_permission + _reporting_permissions
            + _task_route_permissions + _worker_request_permissions + _route_editing_permissions
            + _task_inventory_permissions + _task_supply_permissions + _task_inventory_label_permissions
            + _default_supply_permissions + _default_inventory_permissions + _linked_task_permissions
            + _form_submission_permissions + _skills_permissions + _self_scheduling_booking_permissions
            + _self_scheduling_booking_slot_permissions + _self_scheduling_booked_slot_permissions
            + _task_items_permissions + _action_cron_config_permissions + _action_cron_config_status_permissions
            + _crew_availability_request_permissions + _booking_object_rule_permissions +
            [Permissions.VIEW_ALL_TASKS, Permissions.SHOW_OWN_ACTIVITY_STREAM, Permissions.VIEW_TEMPLATE,
             Permissions.VIEW_TASK_FULL_DETAILS, Permissions.VIEW_FULL_TEAM_MEMBER_DETAILS,
             Permissions.VIEW_FULL_EQUIPMENT_DETAILS, Permissions.VIEW_GROUP, Permissions.EDIT_GROUP,
             Permissions.VIEW_PASSWORD_SETTING, Permissions.EDIT_PASSWORD_SETTING, Permissions.EDIT_CUSTOM_MESSGAE,
             Permissions.VIEW_CUSTOM_MESSGAE, Permissions.VIEW_EXTERNAL_INTEGRATION,
             Permissions.TRIGGER_EXTERNAL_INTEGRATION_DATA_FETCH, Permissions.VIEW_FULL_CUSTOMER_DETAILS,
             Permissions.VIEW_DEFAULT_INVENTORY, Permissions.VIEW_LINKED_TASK_META_DATA,
             Permissions.ASSIGN_MANAGED_GROUPS, Permissions.VIEW_MANAGED_GROUPS_DATA,
             Permissions.EDIT_MANAGED_GROUPS_DATA, Permissions.VIEW_DEFAULT_INVENTORY,
             Permissions.VIEW_LINKED_TASK_META_DATA, Permissions.DELETE_MANAGED_GROUPS_DATA, Permissions.VIEW_FORM,
             Permissions.VIEW_CHECKLIST, Permissions.VIEW_TASK_CHECKLIST, Permissions.CAN_VIEW_MAP_VIEW,
             Permissions.CAN_GET_SQUARE_MOBILE_AUTHORIZATION_CODE, Permissions.ADD_ORDER, Permissions.EDIT_ORDER,
             Permissions.VIEW_ORDER, Permissions.DELETE_ORDER, Permissions.CAN_VIEW_REVIEWS,
             Permissions.SHOW_ALL_REVIEWS, Permissions.GET_MOVERS_SUITE_ORDER, Permissions.VIEW_ITEMS_LIST,
             Permissions.VIEW_MASTER_ITEM, Permissions.UPDATE_CREW_AVAILABILITY_REQUEST_STATUS,
             Permissions.UPDATE_LIMITED_COMPANY_PROFILE, Permissions.VIEW_INVOICE,
             Permissions.UPDATE_LIMITED_COMPANY_PROFILE, Permissions.INVOKE_RE_MICRO_SERVICE,
             Permissions.INVOKE_EXPORT_TEAM_MEMBER_SERVICE, Permissions.VIEW_ALL_TASK_INVOICE,
             Permissions.INVOKE_EXPORT_TASK_SERVICE, Permissions.VIEW_CUSTOMER_SETTING,
             Permissions.EDIT_CUSTOMER_SETTING, Permissions.INVOKE_EXPORT_CUSTOMER_SERVICE,
             Permissions.INVOKE_EXPORT_EXTERNAL_INTEGRATION_SERVICE, Permissions.INVOKE_RE_GEO_ADDRESSES_MICRO_SERVICE,
             Permissions.CAN_SEARCH_TASK, Permissions.CAN_SEARCH_CUSTOMER, Permissions.CAN_SEARCH_ENTITY,
             Permissions.CAN_SEARCH_RESOURCE, Permissions.VIEW_ITEMS_GROUPS, Permissions.VIEW_RESOURCE_TEMPLATE]
        },
        {
            'group_id': BOOKING_ONLY_PERMISSION_GROUP_ID,
            'title': PermissionGroups.BOOKING_ONLY,
            'description': 'Can edit Booking Tasks created by them',
            'type': PermissionGroupType.OPTIONAL,
            'permission_tokens': _task_status_on_own_created_task_permissions + _team_confirmation_permission
            + _task_inventory_permissions + _task_supply_permissions + _task_inventory_label_permissions
            + _default_supply_permissions + _default_inventory_permissions + _task_permissions_on_own_created_task
            + _task_items_permissions + _form_submission_on_own_created_tasks_permissions + _linked_task_permissions
            + _booking_object_rule_permissions +
            [Permissions.ADD_BOOKING_ONLY_TASK, Permissions.ADD_TASK_FILE, Permissions.VIEW_BOOKED_SLOT,
             Permissions.VIEW_ALL_TASKS, Permissions.VIEW_BOOKING, Permissions.VIEW_CUSTOMER, Permissions.EDIT_CUSTOMER,
             Permissions.VIEW_TASK_ROUTE, Permissions.VIEW_TASK_STATUS, Permissions.VIEW_BOOKING_SLOT,
             Permissions.SHOW_OWN_ACTIVITY_STREAM, Permissions.VIEW_TEMPLATE, Permissions.VIEW_TASK_FULL_DETAILS,
             Permissions.VIEW_FULL_TEAM_MEMBER_DETAILS, Permissions.VIEW_FULL_EQUIPMENT_DETAILS, Permissions.VIEW_GROUP,
             Permissions.VIEW_CUSTOM_MESSGAE, Permissions.VIEW_LINKED_TASK, Permissions.VIEW_LINKED_TASK_META_DATA,
             Permissions.VIEW_DEFAULT_INVENTORY, Permissions.ASSIGN_MANAGED_GROUPS, Permissions.VIEW_MANAGED_GROUPS_DATA,
             Permissions.VIEW_DEFAULT_INVENTORY, Permissions.VIEW_ITEMS_LIST, Permissions.VIEW_MASTER_ITEM,
             Permissions.VIEW_FULL_EQUIPMENT_DETAILS, Permissions.VIEW_FULL_CUSTOMER_DETAILS, Permissions.VIEW_FORM,
             Permissions.VIEW_SKILL, Permissions.VIEW_PASSWORD_SETTING, Permissions.EDIT_PASSWORD_SETTING,
             Permissions.VIEW_EXTERNAL_INTEGRATION, Permissions.TRIGGER_EXTERNAL_INTEGRATION_DATA_FETCH,
             Permissions.VIEW_ALL_TASK_INVOICE, Permissions.INVOKE_EXPORT_EXTERNAL_INTEGRATION_SERVICE,
             Permissions.INVOKE_RE_GEO_ADDRESSES_MICRO_SERVICE, Permissions.CAN_SEARCH_TASK,
             Permissions.VIEW_ITEMS_GROUPS, Permissions.VIEW_RESOURCE_TEMPLATE]
        },
        {  # For now the permissions of PROJECT COORDINATOR are same as of TEAM LEAD. The main differences is
            # that the PROJECT COORDINATOR can edit assigned tasks, view customers, edit customers, add customers,
            # search entities on the basis of skills, view forms, assign managed groups, view assigned groups
            'group_id': PROJECT_COORDINATOR_PERMISSION_GROUP_ID,
            'title': PermissionGroups.PROJECT_COORDINATOR,
            'description': 'Has edit access to assigned tasks and can mark statuses',
            'type': PermissionGroupType.OPTIONAL,
            'permission_tokens': _task_status_permissions + _team_confirmation_permission
            + _task_inventory_permissions + _task_supply_permissions + _task_inventory_label_permissions
            + _default_supply_permissions + _default_inventory_permissions + _task_items_permissions
            + _assigned_crew_availability_request_permissions +
            [Permissions.VIEW_ASSIGNED_TASKS, Permissions.EDIT_ASSIGNED_TASKS, Permissions.ADD_TASK_FILE,
             Permissions.SHOW_OWN_ACTIVITY_STREAM, Permissions.VIEW_TEMPLATE,
             Permissions.ASSIGN_MANAGED_GROUPS, Permissions.VIEW_ASSIGNED_GROUPS,
             Permissions.VIEW_TASK_FULL_DETAILS, Permissions.VIEW_FULL_TEAM_MEMBER_DETAILS,
             Permissions.VIEW_FULL_EQUIPMENT_DETAILS, Permissions.VIEW_PASSWORD_SETTING,
             Permissions.EDIT_PASSWORD_SETTING, Permissions.VIEW_TASK_ROUTE,
             Permissions.LOCK_UNLOCK_TASK_SUPPLIES, Permissions.VIEW_LINKED_TASK,
             Permissions.VIEW_LINKED_TASK_META_DATA, Permissions.EDIT_LINKED_TASK,
             Permissions.VIEW_FORM, Permissions.VIEW_FORM_SUBMISSION, Permissions.VIEW_FORM_OVERVIEW,
             Permissions.EDIT_FORM_SUBMISSION, Permissions.VIEW_BOOKING_SLOT,
             Permissions.VIEW_BOOKING, Permissions.VIEW_SKILL, Permissions.VIEW_CUSTOM_MESSGAE,
             Permissions.VIEW_TASK_CHECKLIST, Permissions.VIEW_FULL_CUSTOMER_DETAILS,
             Permissions.VIEW_CUSTOMER, Permissions.EDIT_CUSTOMER, Permissions.ADD_CUSTOMER,
             Permissions.CAN_ADD_TIME_REPORTING_STATUSES_FOR_OTHER_ASSIGNEES,
             Permissions.CAN_GET_SQUARE_MOBILE_AUTHORIZATION_CODE, Permissions.CAN_VIEW_REVIEWS,
             Permissions.SHOW_OWN_REVIEWS, Permissions.CAN_UN_LOCK_FORM_SUBMISSION,
             Permissions.VIEW_ITEMS_LIST, Permissions.VIEW_MASTER_ITEM, Permissions.VIEW_ALL_TASK_INVOICE,
             Permissions.INVOKE_EXPORT_CUSTOMER_SERVICE, Permissions.INVOKE_RE_GEO_ADDRESSES_MICRO_SERVICE,
             Permissions.CAN_SEARCH_TASK, Permissions.CAN_SEARCH_CUSTOMER, Permissions.VIEW_ITEMS_GROUPS,
             Permissions.VIEW_RESOURCE_TEMPLATE]
        },
        {  # For now the permissions of TEAM LEAD are same as of FIELD CREW. The only difference is that the TEAM LEAD
            # should always be able to see full customer details i.e. wil have VIEW_FULL_CUSTOMER_DETAILS permission
            'group_id': TEAM_LEAD_PERMISSION_GROUP_ID,
            'title': PermissionGroups.TEAM_LEAD,
            'description': 'Has view access to assigned tasks and can mark statuses',
            'type': PermissionGroupType.OPTIONAL,
            'permission_tokens': _task_status_permissions + _team_confirmation_permission
            + _task_inventory_permissions + _task_supply_permissions + _task_inventory_label_permissions
            + _default_supply_permissions + _default_inventory_permissions + _task_items_permissions
            + _assigned_crew_availability_request_permissions +
            [Permissions.VIEW_ASSIGNED_TASKS, Permissions.ADD_TASK_FILE, Permissions.SHOW_OWN_ACTIVITY_STREAM,
             Permissions.VIEW_TEMPLATE, Permissions.VIEW_TASK_FULL_DETAILS,
             Permissions.VIEW_FULL_TEAM_MEMBER_DETAILS, Permissions.VIEW_FULL_EQUIPMENT_DETAILS,
             Permissions.VIEW_PASSWORD_SETTING, Permissions.EDIT_PASSWORD_SETTING, Permissions.VIEW_TASK_ROUTE,
             Permissions.LOCK_UNLOCK_TASK_SUPPLIES, Permissions.VIEW_LINKED_TASK,
             Permissions.VIEW_LINKED_TASK_META_DATA, Permissions.VIEW_FORM_SUBMISSION, Permissions.VIEW_FORM_OVERVIEW,
             Permissions.EDIT_FORM_SUBMISSION, Permissions.VIEW_BOOKING_SLOT,
             Permissions.VIEW_BOOKING, Permissions.VIEW_CUSTOM_MESSGAE,
             Permissions.VIEW_TASK_CHECKLIST, Permissions.VIEW_FULL_CUSTOMER_DETAILS,
             Permissions.CAN_ADD_TIME_REPORTING_STATUSES_FOR_OTHER_ASSIGNEES,
             Permissions.CAN_GET_SQUARE_MOBILE_AUTHORIZATION_CODE, Permissions.CAN_VIEW_REVIEWS,
             Permissions.SHOW_OWN_REVIEWS, Permissions.CAN_UN_LOCK_FORM_SUBMISSION,
             Permissions.VIEW_ITEMS_LIST, Permissions.VIEW_MASTER_ITEM, Permissions.VIEW_ALL_TASK_INVOICE,
             Permissions.INVOKE_RE_GEO_ADDRESSES_MICRO_SERVICE, Permissions.CAN_SEARCH_TASK,
             Permissions.VIEW_ITEMS_GROUPS, Permissions.VIEW_RESOURCE_TEMPLATE]
        },
        {
            'group_id': FIELD_CREW_PERMISSION_GROUP_ID,
            'title': PermissionGroups.FIELD_CREW,
            'description': 'Has view access to assigned tasks and can mark statuses',
            'type': PermissionGroupType.OPTIONAL,
            'permission_tokens': _task_status_permissions + _team_confirmation_permission
            + _task_inventory_permissions + _task_supply_permissions + _task_inventory_label_permissions
            + _default_supply_permissions + _default_inventory_permissions + _task_items_permissions
            + _assigned_crew_availability_request_permissions +
            [Permissions.VIEW_ASSIGNED_TASKS, Permissions.ADD_TASK_FILE, Permissions.SHOW_OWN_ACTIVITY_STREAM,
             Permissions.VIEW_TEMPLATE, Permissions.VIEW_TASK_FULL_DETAILS, Permissions.VIEW_FULL_TEAM_MEMBER_DETAILS,
             Permissions.VIEW_FULL_EQUIPMENT_DETAILS, Permissions.VIEW_PASSWORD_SETTING,
             Permissions.EDIT_PASSWORD_SETTING, Permissions.VIEW_TASK_ROUTE, Permissions.LOCK_UNLOCK_TASK_SUPPLIES,
             Permissions.VIEW_LINKED_TASK, Permissions.VIEW_LINKED_TASK_META_DATA, Permissions.VIEW_FORM_SUBMISSION,
             Permissions.EDIT_FORM_SUBMISSION, Permissions.VIEW_BOOKING_SLOT, Permissions.VIEW_BOOKING,
             Permissions.VIEW_TASK_CHECKLIST, Permissions.CAN_GET_SQUARE_MOBILE_AUTHORIZATION_CODE,
             Permissions.CAN_VIEW_REVIEWS, Permissions.SHOW_OWN_REVIEWS, Permissions.VIEW_CUSTOM_MESSGAE,
             Permissions.CAN_UN_LOCK_FORM_SUBMISSION, Permissions.VIEW_ITEMS_LIST, Permissions.VIEW_MASTER_ITEM,
             Permissions.VIEW_FORM_OVERVIEW,Permissions.VIEW_ALL_TASK_INVOICE,
             Permissions.INVOKE_RE_GEO_ADDRESSES_MICRO_SERVICE, Permissions.CAN_SEARCH_TASK,
             Permissions.VIEW_ITEMS_GROUPS, Permissions.VIEW_RESOURCE_TEMPLATE]
        },
        {
            'group_id': LIMITED_ACCESS_PERMISSION_GROUP_ID,
            'title': PermissionGroups.LIMITED_ACCESS,
            'description': 'Has view access to assigned tasks and can view statuses',
            'type': PermissionGroupType.OPTIONAL,
            'permission_tokens': [Permissions.VIEW_ASSIGNED_TASKS, Permissions.VIEW_TASK_STATUS,
                                  Permissions.VIEW_TASK_LIMITED_DETAILS, Permissions.VIEW_LIMITED_TEAM_MEMBER_DETAILS,
                                  Permissions.VIEW_LIMITED_EQUIPMENT_DETAILS, Permissions.VIEW_TASK_ROUTE,
                                  Permissions.VIEW_PASSWORD_SETTING, Permissions.EDIT_PASSWORD_SETTING,
                                  Permissions.VIEW_FORM_SUBMISSION, Permissions.VIEW_FORM_OVERVIEW,
                                  Permissions.EDIT_FORM_SUBMISSION, Permissions.VIEW_BOOKING_SLOT,
                                  Permissions.VIEW_BOOKING, Permissions.VIEW_TASK_CHECKLIST, Permissions.VIEW_ITEM,
                                  Permissions.VIEW_ITEMS_LIST, Permissions.VIEW_MASTER_ITEM,
                                  Permissions.INVOKE_RE_GEO_ADDRESSES_MICRO_SERVICE, Permissions.CAN_SEARCH_TASK,
                                  Permissions.VIEW_ITEMS_GROUPS]
        },
        {
            'group_id': VIEWER_PERMISSION_GROUP_ID,
            'title': PermissionGroups.VIEWER,
            'description': 'Has full access to Team, and Customers. Has view access to tasks and can mark statuses',
            'type': PermissionGroupType.OPTIONAL,
            'permission_tokens': _team_permissions + _customer_permissions + _equipment_permissions
            + _task_status_permissions + _team_confirmation_permission + _reporting_permissions
            + _worker_request_permissions + _task_inventory_permissions + _task_supply_permissions
            + _task_inventory_label_permissions + _default_supply_permissions + _default_inventory_permissions
            + _form_submission_permissions + _skills_permissions + _self_scheduling_booking_permissions
            + _self_scheduling_booking_slot_permissions + _self_scheduling_booked_slot_permissions
            + _crew_availability_request_permissions + _booking_object_rule_permissions +
            [Permissions.VIEW_ALL_TASKS, Permissions.ADD_TASK_FILE, Permissions.SHOW_OWN_ACTIVITY_STREAM,
             Permissions.VIEW_TEMPLATE, Permissions.VIEW_TASK_FULL_DETAILS, Permissions.VIEW_FULL_TEAM_MEMBER_DETAILS,
             Permissions.VIEW_FULL_EQUIPMENT_DETAILS, Permissions.VIEW_GROUP, Permissions.EDIT_GROUP,
             Permissions.VIEW_PASSWORD_SETTING, Permissions.EDIT_PASSWORD_SETTING, Permissions.EDIT_CUSTOM_MESSGAE,
             Permissions.VIEW_CUSTOM_MESSGAE, Permissions.VIEW_EXTERNAL_INTEGRATION,
             Permissions.VIEW_LINKED_TASK, Permissions.VIEW_FULL_CUSTOMER_DETAILS,
             Permissions.VIEW_DEFAULT_INVENTORY, Permissions.VIEW_LINKED_TASK_META_DATA,
             Permissions.ASSIGN_MANAGED_GROUPS, Permissions.VIEW_MANAGED_GROUPS_DATA,
             Permissions.EDIT_MANAGED_GROUPS_DATA, Permissions.VIEW_DEFAULT_INVENTORY,
             Permissions.VIEW_LINKED_TASK_META_DATA, Permissions.DELETE_MANAGED_GROUPS_DATA, Permissions.VIEW_FORM,
             Permissions.VIEW_CHECKLIST, Permissions.VIEW_TASK_CHECKLIST, Permissions.VIEW_ITEM,
             Permissions.VIEW_TASK_ROUTE, Permissions.CAN_GET_SQUARE_MOBILE_AUTHORIZATION_CODE,
             Permissions.CAN_VIEW_REVIEWS, Permissions.SHOW_ALL_REVIEWS, Permissions.VIEW_ITEMS_LIST,
             Permissions.VIEW_MASTER_ITEM, Permissions.UPDATE_CREW_AVAILABILITY_REQUEST_STATUS,
             Permissions.INVOKE_EXPORT_TEAM_MEMBER_SERVICE, Permissions.VIEW_ALL_TASK_INVOICE,
             Permissions.INVOKE_EXPORT_CUSTOMER_SERVICE, Permissions.INVOKE_EXPORT_EXTERNAL_INTEGRATION_SERVICE,
             Permissions.INVOKE_RE_GEO_ADDRESSES_MICRO_SERVICE, Permissions.CAN_SEARCH_TASK,
             Permissions.CAN_SEARCH_CUSTOMER, Permissions.CAN_SEARCH_ENTITY, Permissions.CAN_SEARCH_RESOURCE,
             Permissions.VIEW_ITEMS_GROUPS, Permissions.VIEW_RESOURCE_TEMPLATE]
        },
        {
            'group_id': CUSTOMER_PERMISSION_GROUP_ID,
            'title': PermissionGroups.CUSTOMER,
            'description': 'Can see his tasks and assigned bookings',
            'type': PermissionGroupType.OPTIONAL,
            'permission_tokens': [Permissions.EDIT_PASSWORD_SETTING, Permissions.VIEW_CUSTOMER_TASKS,
                                  Permissions.VIEW_CUSTOMER_BOOKINGS, Permissions.VIEW_CUSTOMER_TEMPLATE,
                                  Permissions.VIEW_OWN_CUSTOMER]
        }
    ]


    @classmethod
    def get_defined_permission_groups(cls):
        return UserPermissionGroups._defined_permission_groups
    
    @classmethod
    def get_defined_permission_group_ids(cls):
        # -1 indicates CUSTOMER
        defined_permission_group_ids = [-1]
        for default_permission_group in cls.get_defined_permission_groups():
            defined_permission_group_ids.append(default_permission_group.get('group_id'))
        return defined_permission_group_ids
    
    @classmethod
    def get_permission_id_using_permission_group_title(cls, title):
        for group in UserPermissionGroups._defined_permission_groups:
            if group["title"] == title:
                return group["group_id"]


class UserPermission(models.Model):
    # entity_id = ndb.IntegerProperty(required=True)
    entity_id = models.IntegerField(null=False)
    assigned_group_ids = ArrayField(
        base_field=models.IntegerField(),
        blank=True,
        null=True
    )

    @classmethod
    def get_structured_entity_permission_groups(cls, user_permissions):
        active_permission_group_ids = []
        if user_permissions:
            active_permission_group_ids = user_permissions.assigned_group_ids

        marked_permission_groups = []

        for group in UserPermissionGroups.get_defined_permission_groups():
            if group["type"] == PermissionGroupType.DEFAULT:
                continue
            marked_permission_group = dict(
                title=group["title"],
                description=group["description"],
                id=group["group_id"],
                status=False
            )
            if group["group_id"] in active_permission_group_ids:
                marked_permission_group["status"] = True
            marked_permission_groups.append(marked_permission_group)

        return marked_permission_groups
    
    @classmethod
    def get_entity_permission_groups(cls, entity_id):
        return cls.get_structured_entity_permission_groups(UserPermission.objects.filter(entity_id = entity_id).get())

    @classmethod
    def get_entities_by_permission_groups(cls, company_id, permission_group_list):
        permission_groups = filter(lambda user_permission_group: user_permission_group["title"] in permission_group_list
                                   , UserPermissionGroups.get_defined_permission_groups())
        entities_by_group = {}
        user_key = Util.create_user_key(company_id)
        for permission_group in permission_groups:
            # entities = UserPermission.query(UserPermission.assigned_group_ids.IN([permission_group["group_id"]]),
            #                                 ancestor=user_key).fetch()
            entities = UserPermission.objects.filter(assigned_group_ids__contains=[permission_group["group_id"]],
            ancestor=user_key).all()
            entities_by_group[permission_group["title"]] = map(lambda entity: entity.entity_id, entities)

        return entities_by_group