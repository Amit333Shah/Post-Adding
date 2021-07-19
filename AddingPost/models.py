from typing import Text
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class PostText(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    text=models.TextField(max_length=10000)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return ((self.user),(self.created_at))

      




