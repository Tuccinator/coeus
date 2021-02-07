from django.db import models

class Settings(models.Model):
    settings_type = models.CharField(max_length=30)
    settings_value = models.CharField(max_length=255)