
from apps.common.managers import GetOrNoneManager,AliveQuerySet
from django.db import models
from uuid import uuid4
# Create your models here.

class BaseModel(models.Model):
    
    id = models.UUIDField(default=uuid4,primary_key=True,editable=False)


    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)

    deleted_at = models.DateTimeField(null=True,blank=True)


    #Для работы со всеми обьектами
    objects = GetOrNoneManager()
    #Для работы с не удаленными обьектами
    alive_objects = AliveQuerySet()