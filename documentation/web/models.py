from django.db import models

# Create your models here.

class doc(models.Model):
    date = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=255)
    documentation = models.TextField()