from django.db import models
from django.contrib.auth.models import User


class Table(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tables')
	result = models.IntegerField(default=0)


# Create your models here.
