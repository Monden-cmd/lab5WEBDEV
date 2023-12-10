from django.db import models

class MyModel(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)