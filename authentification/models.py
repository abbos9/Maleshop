from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class UserModel(models.Model):
    username = models.CharField(max_length=50, null=True, blank=True)
    password = models.CharField(max_length=25, null=True, blank=True)

    craeted_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) :
        return f"{self.username}"
    
    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'
        unique_together = ['username']
