from django.db import models

# Create your models here.
class Tips(models.Model):
  tips_catgory = models.CharField(max_length=100)
  title = models.CharField(max_length=100)
  description = models.TextField(max_length=250)
  