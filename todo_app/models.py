from django.db import models
import datetime

# Create your models here.
class ToDo(models.Model):
    def __str__(self):
        return self.subject
    subject = models.CharField(max_length=100)
    priority = models.IntegerField()
    date = models.DateField(default=datetime.date.today)