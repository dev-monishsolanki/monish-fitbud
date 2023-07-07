from django.db import models

# Create your models here.
class contact(models.Model):
    number=models.IntegerField(primary_key=True)
    name=models.CharField(max_length=30)