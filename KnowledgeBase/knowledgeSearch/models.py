from django.db import models
from datetime import datetime 
# Create your models here.

class Article(models.Model):
    title = models.TextField()
    body = models.TextField()

class Contact(models.Model):
    name = models.TextField()
    expertise = models.TextField()
    number = models.IntegerField()

class Ticket(models.Model):
    submitTime = models.DateTimeField(default=datetime.now, blank=True)
    number = models.IntegerField()
    notes = models.TextField()
    