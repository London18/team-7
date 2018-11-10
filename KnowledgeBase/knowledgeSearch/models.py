from django.db import models

# Create your models here.

class Article(models.Model):
    title = models.TextField()
    body = models.TextField()

class Contact(models.Model):
    name = models.TextField()
    expertise = models.TextField()
    number = models.IntegerField()
    