from django.db import models

from Job_Portal.Job_Portal_App.models import User


# Create your models here.
class Resume(models.Model):
    objects = None
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    jot_title = models.CharField(max_length=100)
#     insert cv
