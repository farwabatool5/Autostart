def convert_taskstatus_to_type(text):
    if text == 'NOTSTARTED':
        return TaskStatusType.NOTSTARTED
    elif text == 'ENROUTE':
        return TaskStatusType.ENROUTE
    elif text == 'STARTED':
        return TaskStatusType.STARTED
    elif text == 'COMPLETE':
        return TaskStatusType.COMPLETE
    elif text == 'CANCELLED':
        return TaskStatusType.CANCELLED
    elif text == 'EXCEPTION':
        return TaskStatusType.EXCEPTION
    elif text == 'PREPARING':
        return TaskStatusType.PREPARING
    elif text == 'READYFORPICKUP':
        return TaskStatusType.READYFORPICKUP
    elif text == 'CONFIRMED':
        return TaskStatusType.CONFIRMED
    elif text == 'RESCHEDULED':
        return TaskStatusType.RESCHEDULED
    elif text == 'CUSTOMER_EXCEPTION':
        return TaskStatusType.CUSTOMER_EXCEPTION
    elif text == 'BOOKING_CANCELLED':
        return TaskStatusType.BOOKING_CANCELLED
    elif text == 'RECOMMENDED':
        return TaskStatusType.RECOMMENDED
    elif text == 'CUSTOM':
        return TaskStatusType.CUSTOM
    elif text == 'CUSTOMER_SIGNATURE':
        return TaskStatusType.CUSTOMER_SIGNATURE
    elif text == 'ARRIVING':
        return TaskStatusType.ARRIVING
    elif text == 'REMINDER':
        return TaskStatusType.REMINDER
    elif text == 'REVIEW_REMINDER':
        return TaskStatusType.REVIEW_REMINDER
    elif text == 'LATE':
        return TaskStatusType.LATE
    elif text == 'PREDICTED_LATE':
        return TaskStatusType.PREDICTED_LATE
    elif text == 'NOSHOW':
        return TaskStatusType.NOSHOW
    elif text == 'EXTRA_TIME':
        return TaskStatusType.EXTRA_TIME
    elif text == 'SEEN_BY_CUSTOMER':
        return TaskStatusType.SEEN_BY_CUSTOMER
    elif text == 'FILE_ANNOTATED':
        return TaskStatusType.FILE_ANNOTATED
    elif text == 'CREW_ASSIGNED':
        return TaskStatusType.CREW_ASSIGNED
    elif text == 'CREW_REMOVED':
        return TaskStatusType.CREW_REMOVED
    elif text == 'EQUIPMENT_ASSIGNED':
        return TaskStatusType.EQUIPMENT_ASSIGNED
    elif text == 'EQUIPMENT_REMOVED':
        return TaskStatusType.EQUIPMENT_REMOVED
    elif text == 'ON_HOLD':
        return TaskStatusType.ON_HOLD
    elif text == 'MOVING_TO_STORAGE':
        return TaskStatusType.MOVING_TO_STORAGE
    elif text == 'IN_STORAGE':
        return TaskStatusType.IN_STORAGE
    elif text == 'OUT_OF_STORAGE':
        return TaskStatusType.OUT_OF_STORAGE
    elif text == 'IN_TRANSIT':
        return TaskStatusType.IN_TRANSIT
    elif text == 'PICKING_UP':
        return TaskStatusType.PICKING_UP
    elif text == 'MILESTONE':
        return TaskStatusType.MILESTONE
    elif text == 'ARRIVED':
        return TaskStatusType.ARRIVED
    elif text == 'DEPARTED':
        return TaskStatusType.DEPARTED
    elif text == 'AUTO_START_PENDING':
        return TaskStatusType.AUTO_START_PENDING
    elif text == 'AUTO_START':
        return TaskStatusType.AUTO_START
    elif text == 'AUTO_COMPLETE_PENDING':
        return TaskStatusType.AUTO_COMPLETE_PENDING
    elif text == 'AUTO_COMPLETE':
        return TaskStatusType.AUTO_COMPLETE
    elif text == 'RETURNED':
        return TaskStatusType.RETURNED
    elif text == 'ORDER':
        return TaskStatusType.ORDER
    elif text == 'SKIP':
        return TaskStatusType.SKIP
    elif text == 'SUBSCRIBED':
        return TaskStatusType.SUBSCRIBED
    elif text == 'UNSUBSCRIBED':
        return TaskStatusType.UNSUBSCRIBED
    elif text == 'HELP':
        return TaskStatusType.HELP
    elif text == 'LAUNCH_DOCUMENT':
        return TaskStatusType.LAUNCH_DOCUMENT
    elif text == 'MANUAL_NOTIFICATION':
        return TaskStatusType.MANUAL_NOTIFICATION
    elif text == 'CHECKINVENTORY':
        return TaskStatusType.CHECKINVENTORY
    elif text == 'CHECKSUPPLIES':
        return TaskStatusType.CHECKSUPPLIES
    elif text == 'RESEND_TASK_CONFIRMATION':
        return TaskStatusType.RESEND_TASK_CONFIRMATION
    elif text == 'FORM_COMPLETE':
        return TaskStatusType.FORM_COMPLETE
    elif text == 'FORM_ATTACH':
        return TaskStatusType.FORM_ATTACH
    elif text == 'FORM_SUBMIT':
        return TaskStatusType.FORM_SUBMIT
    elif text == 'TASK_ACCEPTED':
        return TaskStatusType.TASK_ACCEPTED
    elif text == 'TASK_REJECTED':
        return TaskStatusType.TASK_REJECTED
    elif text == 'DAY_START':
        return TaskStatusType.DAY_START
    elif text == 'DAY_COMPLETE':
        return TaskStatusType.DAY_COMPLETE
    elif text == 'CLOCK_IN':
        return TaskStatusType.CLOCK_IN
    elif text == 'CLOCK_OUT':
        return TaskStatusType.CLOCK_OUT
    elif text == 'PROCESS_PAYMENT':
        return TaskStatusType.PROCESS_PAYMENT
    elif text == 'FORM_REMINDER':
        return TaskStatusType.FORM_REMINDER
    elif text == 'INVOICE_GENERATED':
        return TaskStatusType.INVOICE_GENERATED
    elif text == 'PAYMENT_MADE':
        return TaskStatusType.PAYMENT_MADE
    elif text == 'CLOSED':
        return TaskStatusType.CLOSED
    elif text == 'INTEGRATION':
        return TaskStatusType.INTEGRATION
    elif text == 'OPT_IN_MESSAGE_SENT':
        return TaskStatusType.OPT_IN_MESSAGE_SENT
    elif text == 'CONSENT_PENDING':
        return TaskStatusType.CONSENT_PENDING
    else:
        return TaskStatusType.CUSTOM


def convert_taskstatus_to_text(type):
    if type == TaskStatusType.NOTSTARTED:
        return 'NOTSTARTED'
    elif type == TaskStatusType.ENROUTE:
        return 'ENROUTE'
    elif type == TaskStatusType.STARTED:
        return 'STARTED'
    elif type == TaskStatusType.COMPLETE:
        return 'COMPLETE'
    elif type == TaskStatusType.CANCELLED:
        return 'CANCELLED'
    elif type == TaskStatusType.EXCEPTION:
        return 'EXCEPTION'
    elif type == TaskStatusType.PREPARING:
        return 'PREPARING'
    elif type == TaskStatusType.READYFORPICKUP:
        return 'READYFORPICKUP'
    elif type == TaskStatusType.CONFIRMED:
        return 'CONFIRMED'
    elif type == TaskStatusType.RESCHEDULED:
        return 'RESCHEDULED'
    elif type == TaskStatusType.BOOKING_CANCELLED:
        return 'BOOKING_CANCELLED'
    elif type == TaskStatusType.CUSTOM:
        return 'CUSTOM'
    elif type == TaskStatusType.CUSTOMER_EXCEPTION:
        return 'CUSTOMER_EXCEPTION'
    elif type == TaskStatusType.RECOMMENDED:
        return 'RECOMMENDED'
    elif type == TaskStatusType.CUSTOMER_SIGNATURE:
        return 'CUSTOMER_SIGNATURE'
    elif type == TaskStatusType.ARRIVING:
        return 'ARRIVING'
    elif type == TaskStatusType.REMINDER:
        return 'REMINDER'
    elif type == TaskStatusType.REVIEW_REMINDER:
        return 'REVIEW_REMINDER'
    elif type == TaskStatusType.LATE:
        return 'LATE'
    elif type == TaskStatusType.PREDICTED_LATE:
        return 'PREDICTED_LATE'
    elif type == TaskStatusType.NOSHOW:
        return 'NOSHOW'
    elif type == TaskStatusType.EXTRA_TIME:
        return 'EXTRA_TIME'
    elif type == TaskStatusType.SEEN_BY_CUSTOMER:
        return 'SEEN_BY_CUSTOMER'
    elif type == TaskStatusType.FILE_ANNOTATED:
        return 'FILE_ANNOTATED'
    elif type == TaskStatusType.CREW_ASSIGNED:
        return 'CREW_ASSIGNED'
    elif type == TaskStatusType.CREW_REMOVED:
        return 'CREW_REMOVED'
    elif type == TaskStatusType.EQUIPMENT_ASSIGNED:
        return 'EQUIPMENT_ASSIGNED'
    elif type == TaskStatusType.EQUIPMENT_REMOVED:
        return 'EQUIPMENT_REMOVED'
    elif type == TaskStatusType.ON_HOLD:
        return 'ON_HOLD'
    elif type == TaskStatusType.MOVING_TO_STORAGE:
        return 'MOVING_TO_STORAGE'
    elif type == TaskStatusType.IN_STORAGE:
        return 'IN_STORAGE'
    elif type == TaskStatusType.OUT_OF_STORAGE:
        return 'OUT_OF_STORAGE'
    elif type == TaskStatusType.IN_TRANSIT:
        return 'IN_TRANSIT'
    elif type == TaskStatusType.PICKING_UP:
        return 'PICKING_UP'
    elif type == TaskStatusType.MILESTONE:
        return 'MILESTONE'
    elif type == TaskStatusType.ARRIVED:
        return 'ARRIVED'
    elif type == TaskStatusType.DEPARTED:
        return 'DEPARTED'
    elif type == TaskStatusType.AUTO_START_PENDING:
        return 'AUTO_START_PENDING'
    elif type == TaskStatusType.AUTO_START:
        return 'AUTO_START'
    elif type == TaskStatusType.AUTO_COMPLETE_PENDING:
        return 'AUTO_COMPLETE_PENDING'
    elif type == TaskStatusType.AUTO_COMPLETE:
        return 'AUTO_COMPLETE'
    elif type == TaskStatusType.RETURNED:
        return 'RETURNED'
    elif type == TaskStatusType.ORDER:
        return 'ORDER'
    elif type == TaskStatusType.SKIP:
        return 'SKIP'
    elif type == TaskStatusType.SUBSCRIBED:
        return 'SUBSCRIBED'
    elif type == TaskStatusType.UNSUBSCRIBED:
        return 'UNSUBSCRIBED'
    elif type == TaskStatusType.HELP:
        return 'HELP'
    elif type == TaskStatusType.LAUNCH_DOCUMENT:
        return 'LAUNCH_DOCUMENT'
    elif type == TaskStatusType.MANUAL_NOTIFICATION:
        return 'MANUAL_NOTIFICATION'
    elif type == TaskStatusType.CHECKINVENTORY:
        return 'CHECKINVENTORY'
    elif type == TaskStatusType.CHECKSUPPLIES:
        return 'CHECKSUPPLIES'
    elif type == TaskStatusType.RESEND_TASK_CONFIRMATION:
        return 'RESEND_TASK_CONFIRMATION'
    elif type == TaskStatusType.FORM_COMPLETE:
        return 'FORM_COMPLETE'
    elif type == TaskStatusType.FORM_SUBMIT:
        return 'FORM_SUBMIT'
    elif type == TaskStatusType.FORM_ATTACH:
        return 'FORM_ATTACH'
    elif type == TaskStatusType.TASK_REJECTED:
        return 'TASK_REJECTED'
    elif type == TaskStatusType.TASK_ACCEPTED:
        return 'TASK_ACCEPTED'
    elif type == TaskStatusType.DAY_START:
        return 'DAY_START'
    elif type == TaskStatusType.DAY_COMPLETE:
        return 'DAY_COMPLETE'
    elif type == TaskStatusType.CLOCK_IN:
        return 'CLOCK_IN'
    elif type == TaskStatusType.CLOCK_OUT:
        return 'CLOCK_OUT'
    elif type == TaskStatusType.PROCESS_PAYMENT:
        return 'PROCESS_PAYMENT'
    elif type == TaskStatusType.FORM_REMINDER:
        return 'FORM_REMINDER'
    elif type == TaskStatusType.INVOICE_GENERATED:
        return 'INVOICE_GENERATED'
    elif type == TaskStatusType.PAYMENT_MADE:
        return 'PAYMENT_MADE'
    elif type == TaskStatusType.CLOSED:
        return 'CLOSED'
    elif type == TaskStatusType.INTEGRATION:
        return 'INTEGRATION'
    elif type == TaskStatusType.OPT_IN_MESSAGE_SENT:
        return 'OPT_IN_MESSAGE_SENT'
    elif type == TaskStatusType.CONSENT_PENDING:
        return 'CONSENT_PENDING'
    else:
        return 'CUSTOM'


class TaskStatusType:
    """
    MAKE SURE THIS TYPE DO NOT OVERLAP WITH NotificationTriggerType
    """

    NOTSTARTED = 1001
    ENROUTE = 1002
    STARTED = 1003
    COMPLETE = 1004
    CANCELLED = 1005
    EXCEPTION = 1006
    CUSTOM = 1007
    PREPARING = 1008
    READYFORPICKUP = 1009
    CONFIRMED = 1010
    RESCHEDULED = 1011

    ARRIVING = 1050
    LATE = 1051
    NOSHOW = 1052
    EXTRA_TIME = 1053
    PREDICTED_LATE = 1054

    REMINDER = 1100
    RECOMMENDED = 1102
    REVIEW_REMINDER = 1103
    CUSTOMER_SIGNATURE = 1104
    CUSTOMER_EXCEPTION = 1105
    SEEN_BY_CUSTOMER = 1106
    CREW_ASSIGNED = 1107
    CREW_REMOVED = 1108
    EQUIPMENT_ASSIGNED = 1109
    EQUIPMENT_REMOVED = 1110
    BOOKING_CANCELLED = 1111

    ON_HOLD = 1201
    MOVING_TO_STORAGE = 1202
    IN_STORAGE = 1203
    OUT_OF_STORAGE = 1204
    IN_TRANSIT = 1205
    PICKING_UP = 1206
    MILESTONE = 1207
    CLOSED = 1208

    ARRIVED = 1301
    DEPARTED = 1302
    AUTO_START_PENDING = 1303
    AUTO_START = 1304
    AUTO_COMPLETE_PENDING = 1305
    AUTO_COMPLETE = 1306
    RETURNED = 1307

    ORDER = 1401
    SKIP = 1402

    SUBSCRIBED = 1501
    UNSUBSCRIBED = 1502
    HELP = 1503

    LAUNCH_DOCUMENT = 1504
    MANUAL_NOTIFICATION = 1505
    FILE_ANNOTATED = 1506

    CHECKINVENTORY = 1601
    CHECKSUPPLIES = 1602

    RESEND_TASK_CONFIRMATION = 1701

    TASK_ACCEPTED = 1801
    TASK_REJECTED = 1802

    FORM_COMPLETE = 1901
    FORM_SUBMIT = 1902
    FORM_ATTACH = 1903
    FORM_REMINDER = 1904

    DAY_START = 2000
    DAY_COMPLETE = 2002

    CLOCK_IN = 2101
    CLOCK_OUT = 2102

    PROCESS_PAYMENT = 2200

    INVOICE_GENERATED = 2300
    PAYMENT_MADE = 2301

    INTEGRATION = 2400

    OPT_IN_MESSAGE_SENT = 2500
    CONSENT_PENDING = 2501
