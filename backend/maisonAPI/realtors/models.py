from django.db import models
from datetime import datetime


class Realtor(models.Model):
    """Model representing a real estate agent."""
    name = models.CharField(max_length=100)
    img = models.ImageField(upload_to='photos/%Y/%m/%d')
    bio = models.TextField(blank=True)
    phone = models.CharField(max_length=20)
    email = models.EmailField(max_length=100)
    date_hired = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.name
