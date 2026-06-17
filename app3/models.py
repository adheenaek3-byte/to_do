from django.db import models
class tasks(models.Model):
    task=models.CharField(max_length=100)
    deadline=models.DateField()
# Create your models here.
