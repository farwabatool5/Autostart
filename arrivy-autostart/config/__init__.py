# """
# This configuration file loads environment's specific config settings for the
# application. It takes precedence over the config located in the boilerplate
# package.
# """
# import os
# import urllib
# from urlparse import urlunsplit

# DEV = os.environ['SERVER_SOFTWARE'].startswith('Dev')
# if "SERVER_SOFTWARE" in os.environ:
#     if os.environ['SERVER_SOFTWARE'].startswith('Dev'):
#         print ("Starting Localhost in Debug Mode")
#         from localhost import config
#     elif os.environ['SERVER_SOFTWARE'].startswith('Google'):
#         if os.environ['APPLICATION_ID'].endswith('arrivy-sandbox'):
#             from sandbox import config
#         else:
#             from production import config
#     else:
#         raise ValueError("Environment undetected")
# else:
#     from testing import config


# def events_version(token, events):
#     qs = urllib.urlencode({'token': token})
#     host = os.getenv('HTTP_HOST')
#     scheme = 'https' if config['environment'] in ['production', 'sandbox'] else 'http'
#     version = os.getenv('CURRENT_VERSION_ID').split('.')[0]
#     version = 'dev' if version == 'None' else version
#     for event in events.values():
#         event['topic'] = '%s-%s' % (event['topic'], version)
#         subscriptions = event.get('subscriptions', [])
#         event['subscriptions'] = [
#                 ('%s-%s' % (n, version), urlunsplit([scheme, host, e, qs, '']))
#                 for n, e in subscriptions]
#     return events


# config['events'] = events_version(config['PUBSUB_TOKEN'], {
#     'task-create': {
#         'topic': 'task-create',
#         'subscriptions': [
#             ('task-create-slack-handler', '/api/notifications/slack'),
#             ('task-create-email-handler', '/api/notifications/email'),
#             ('task-create-sms-handler', '/api/notifications/sms'),
#             ('task-create-firebase-handler', '/api/notifications/firebase'),
#             ('task-create-custom-webhook-handler', '/api/notifications/custom-webhook')
#         ]
#     },
#     'task-delete': {
#         'topic': 'task-delete',
#         'subscriptions': [
#             ('task-delete-firebase-handler', '/api/notifications/firebase'),
#             ('task-delete-custom-webhook-handler', '/api/notifications/custom-webhook')
#         ]
#     },
#     'reports-create': {
#         'topic': 'report-create',
#         'subscriptions': [
#             ('report-create-handler', '/api/notifications/report-create')
#         ]
#     },
#     'task-status-create': {
#         'topic': 'task-status-create',
#         'subscriptions': [
#             ('task-status-create-slack-handler', '/api/notifications/slack'),
#             ('task-status-create-email-handler', '/api/notifications/email'),
#             ('task-status-create-sms-handler', '/api/notifications/sms'),
#             ('task-status-create-firebase-handler', '/api/notifications/firebase'),
#             ('task-status-create-sentiment-handler', '/api/tasks/set-status-sentiment'),
#             ('task-status-custom-webhook-handler', '/api/notifications/custom-webhook')
#         ]
#     },
#     'team-notification-response': {
#         'topic': 'team-notification-response',
#         'subscriptions': [
#             ('team-notification-response-email-handler', '/api/notifications/email'),
#             ('team-notification-response-sms-handler', '/api/notifications/sms')
#         ]
#     },
#     'task-rating-create': {
#         'topic': 'task-rating-create',
#         'subscriptions': [
#             ('task-rating-create-email-handler', '/api/notifications/email'),
#             ('task-rating-create-firebase-handler', '/api/notifications/firebase'),
#             ('task-rating-custom-webhook-handler', '/api/notifications/custom-webhook')
#         ]
#     },
#     'task-review-response': {
#             'topic': 'task-review-response',
#             'subscriptions': [
#                 ('task-review-response-email-handler', '/api/notifications/email'),
#                 ('task-review-response-sms-handler', '/api/notifications/sms')
#             ]
#         },
#     'crew-assigned': {
#         'topic': 'crew-assigned',
#         'subscriptions': [
#             ('crew-assigned-email-handler', '/api/notifications/email'),
#             ('crew-assigned-sms-handler', '/api/notifications/sms'),
#             ('crew-assigned-firebase-handler', '/api/notifications/firebase'),
#             ('crew-assigned-custom-webhook-handler', '/api/notifications/custom-webhook'),
#             ('crew-assigned-team-notification-handler', '/api/notifications/team-notification')
#         ]
#     },
#     'crew-removed': {
#         'topic': 'crew-removed',
#         'subscriptions': [
#             ('crew-removed-email-handler', '/api/notifications/email'),
#             ('crew-removed-sms-handler', '/api/notifications/sms'),
#             ('crew-removed-firebase-handler', '/api/notifications/firebase'),
#             ('crew-removed-custom-webhook-handler', '/api/notifications/custom-webhook'),
#             ('crew-removed-team-notification-handler', '/api/notifications/team-notification')
#         ]
#     },
#     'equipment-assigned': {
#         'topic': 'equipment-assigned',
#         'subscriptions': [
#             ('equipment-assigned-email-handler', '/api/notifications/email'),
#             ('equipment-assigned-sms-handler', '/api/notifications/sms'),
#             ('equipment-assigned-firebase-handler', '/api/notifications/firebase'),
#             ('equipment-assigned-custom-webhook-handler', '/api/notifications/custom-webhook')
#         ]
#     },
#     'equipment-removed': {
#         'topic': 'equipment-removed',
#         'subscriptions': [
#             ('equipment-removed-email-handler', '/api/notifications/email'),
#             ('equipment-removed-sms-handler', '/api/notifications/sms'),
#             ('equipment-removed-firebase-handler', '/api/notifications/firebase'),
#             ('equipment-removed-custom-webhook-handler', '/api/notifications/custom-webhook')
#         ]
#     },
#     'task-rescheduled': {
#         'topic': 'task-rescheduled',
#         'subscriptions': [
#             ('task-rescheduled-firebase-handler', '/api/notifications/firebase'),
#             ('task-rescheduled-email-handler', '/api/notifications/email'),
#             ('task-rescheduled-sms-handler', '/api/notifications/sms'),
#             ('task-rescheduled-custom-webhook-handler', '/api/notifications/custom-webhook')
#         ]
#     },
#     'task-group-changed': {
#         'topic': 'task-group-changed',
#         'subscriptions': [
#             ('task-group-changed-custom-webhook-handler', '/api/notifications/custom-webhook')
#         ]
#     },
#     'task-template-extra-fields-update': {
#         'topic': 'task-template-extra-fields-update',
#         'subscriptions': [
#             ('task-template-extra-fields-update-custom-webhook-handler', '/api/notifications/custom-webhook')
#         ]
#     },
#     'task-primary-address-update': {
#         'topic': 'task-primary-address-update',
#         'subscriptions': [
#             ('task-primary-address-update-custom-webhook-handler', '/api/notifications/custom-webhook')
#         ]
#     },
#     'task-additional-addresses-update': {
#         'topic': 'task-additional-addresses-update',
#         'subscriptions': [
#             ('task-additional-addresses-update-custom-webhook-handler', '/api/notifications/custom-webhook')
#         ]
#     },
#     'firebase-retry': {
#         'topic': 'firebase-retry',
#         'subscriptions': [
#             ('firebase-retry-handler', '/api/activity/retry'),
#         ]
#     },
#     'review-reminder': {
#         'topic': 'review-reminder',
#         'subscriptions': [
#             ('review-reminder-email-handler', '/api/notifications/email'),
#             ('review-reminder-sms-handler', '/api/notifications/sms'),
#         ]
#     },
#     'task-reminder': {
#         'topic': 'task-reminder',
#         'subscriptions': [
#             ('task-reminder-email-handler', '/api/notifications/email'),
#             ('task-reminder-sms-handler', '/api/notifications/sms'),
#         ]
#     },
#     'nearby-message': {
#         'topic': 'nearby-message',
#         'subscriptions': [
#             ('nearby-message-sms-handler', '/api/notifications/sms'),
#             ('nearby-message-email-handler', '/api/notifications/email'),
#             ('nearby-message-slack-handler', '/api/notifications/slack'),
#             ('nearby-message-firebase-handler', '/api/notifications/firebase'),
#             ('nearby-message-custom-webhook-handler', '/api/notifications/custom-webhook')
#         ]
#     },
#     'task-delay': {
#         'topic': 'task-delay',
#         'subscriptions': [
#             ('task-delay-email-handler', '/api/notifications/email'),
#             ('task-delay-firebase-handler', '/api/notifications/firebase'),
#             ('task-delay-custom-webhook-handler', '/api/notifications/custom-webhook')
#         ]
#     },
#     'custom-webhook-retry': {
#         'topic': 'custom-webhook-retry',
#         'subscriptions': [
#             ('custom-webhook-retry-handler', '/api/notifications/custom-webhook-retry')
#         ]
#     },
#     'team-notification': {
#         'topic': 'team-notification',
#         'subscriptions': [
#             ('team-notification-email-handler', '/api/notifications/email'),
#             ('team-notification-sms-handler', '/api/notifications/sms'),
#         ]
#     },
#     'reporting-event': {
#         'topic': 'reporting-event',
#         'subscriptions': [
#             ('reporting-bigquery-handler', '/api/reporting/bigquery-publish')
#         ]
#     },
#     'worker-request-notification': {
#         'topic': 'worker-request-notification',
#         'subscriptions': [
#             ('worker-request-notification-email-handler', '/api/notifications/email'),
#             ('worker-request-notification-sms-handler', '/api/notifications/sms'),
#         ]
#     },
#     'worker-request-entity-response-notification': {
#         'topic': 'worker-request-entity-response-notification',
#         'subscriptions': [
#             ('worker-request-entity-response-notification-email-handler', '/api/notifications/email'),
#             ('worker-request-entity-response-notification-sms-handler', '/api/notifications/sms'),
#         ]
#     },
#     'route-optimizer-service-webhook-notification': {
#         'topic': 'route-optimizer-service-webhook-notification',
#         'subscriptions': [
#             ('route-optimizer-service-webhook-notification-handler',
#              '/api/notifications/route-optimizer-service-webhook')
#         ]
#     }
# })
