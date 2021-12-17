from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

# Create your models here.
class Tips_catgory(models.Model):
  title = models.CharField(max_length=100)
  description = models.TextField(max_length=250)
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  
class Tips(models.Model):
  Name = models.CharField(max_length=100)
  title = models.CharField(max_length=100)
  description = models.TextField(max_length=250)
  catgory = models.ForeignKey(Tips_catgory, on_delete=models.CASCADE)
  

# def __str__(self):
#   return self.name

def get_absolute_url(self):
  return reverse('tips-catgory_details', kwargs={'pk': self.id})