from django.db import models

class User(models.Model):
    user_id = models.BigAutoField(primary_key=True)


class Entity(models.Model):
    entity_id = models.BigAutoField(primary_key=True)
    # owner = models.BigIntegerField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    is_default = models.BooleanField(default=False)
    name = models.CharField(max_length=255)

