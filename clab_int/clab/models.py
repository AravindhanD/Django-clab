from django.db import models
import uuid
from django.contrib.auth.models import User
# Create your models here.
class Account(models.Model):
     account_name  = models.CharField(max_length=100)
     account_id = models.CharField(max_length=17)
     App_secret_token = models.UUIDField(default=uuid.uuid4)



class Meta:
        db_table = 'models'

def __str__(self):
        return f"{self.name}"


class Destination(models.Model):
    account = models.ForeignKey(Account, on_delete=models.CASCADE, related_name='destinations')
    name = models.CharField(max_length=100)



class Meta:
        db_table = 'desti'

def __str__(self):
        return f"{self.account}"