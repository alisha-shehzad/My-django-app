from django.db import models

class Employee(models.Model):
    username = models.CharField(max_length=100, unique=True)  # 👈 New field
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)
    def __str__(self):
        return self.username
