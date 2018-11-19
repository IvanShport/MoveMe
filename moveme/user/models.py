from django.contrib.auth.models import User
from django.db import models
from django.conf import settings
import os
 
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):

        return self.user.username
