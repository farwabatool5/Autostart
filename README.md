# Autostart
Task AutoStart Handler was implemented using Django (Pyhton version: 3.8) and PostregSql.
--> Migrated Areas:
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
    
--> Refactoring Areas:
1. The main refactoring done when fetching the data from the postregSQL (Query for fetching from the Database changed at all points).
2. In models construction, syntax changes were performed with respect to the PostregSql.
3. To make relationship between models Foreign keys were used. Similarly, to make each tuple unique within model, primary key was used.
   
--> Issues Faced:
1. Circular Dependency was addressed.
2. There's no direct execution of Ancestor Parent concept in PostregSQL, that we were using NDB for fast query searching. This issue needs to solve if we move with SQL.
