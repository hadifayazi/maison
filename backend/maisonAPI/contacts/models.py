from django.db import models
from django.utils import timezone


class Contact(models.Model):
    """Model to represent contact"""
    name = models.CharFieldm(max_length=200)
    email = models.EmailField(max_length=100)
    subject = models.CharField(max_length=100)
    message = models.TextField(blank=True)
    contact_date = models.DateTimeField(default=timezone.now)

    def __str__(self) -> str:
        return self.email
