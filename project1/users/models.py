from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):

    STATUS = [
        ('user', 'User'),
        ('superuser', 'SuperUser'),
    ]

    status = models.CharField(max_length=32, choices=STATUS, default='user')
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.username
