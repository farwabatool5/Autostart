# Autostart
For this task, we migrated these functions: def entity_arrival(entity_id),def task_auto_start(request) -> in view.py. And create_task_status(mark_entity_arrived_on_task, task_status, entity_id, is_company) -> in notification_utils.py.
Models Migrated:
1. Event
2. Task Shadow
3. Task
4. Entity
5. CompanyProfile
6. UserPermission
7. TaskStatusData
8. Status
9. Template
10. User
    
Refactoring Areas:

Issues Faced:
