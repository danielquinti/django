from django.db import models
import datetime
from django.utils import timezone

class Message(models.Model):
    message_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    def __str__(self):
        return self.message_text