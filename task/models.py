from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    def __str__(self):
        return self.first_name+" "+ self.last_name


class Task(models.Model):
    title = models.CharField(max_length = 40)
    description = models.CharField(max_length =200)
    completed = models.BooleanField(default=False ,blank=True,null=True)

    def __str__(self):
        return self.title
    