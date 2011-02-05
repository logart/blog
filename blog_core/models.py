from django.db import models

# Create your models here.
class Blog_records(models.Model):
    title = models.CharField(max_length=256)
    number = models.IntegerField(blank=False, null=False, unique=True)
