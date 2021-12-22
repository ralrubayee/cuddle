from django.db import models
from django.urls import reverse
from datetime import date
from django.contrib.auth.models import User

AGE = (
  ("0-3","newborn"),
  ("3-6","baby"),
  ("6-9","baby"),
  ("9-12","baby"),
  ("12-24","toddler")
)


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


  def __str__(self):
    return self.name

  # def get_absolute_url(self):
  #   return reverse('tips_detail', kwargs={'tips_detail': self.id})
  
class Milestone(models.Model):
  age = models.CharField(
    max_length=5,
    choices=AGE,
    default=AGE[0][0]
  )
  date = models.DateField('milestone date')
  title = models.CharField(max_length=100)
  description = models.TextField(max_length=250)
  user = models.ForeignKey(User, on_delete=models.CASCADE)

  def __str__(self):
    return self.name
 
  class Meta:
    ordering = ['-date']

  def __str__(self):
    return f"{self.get_age_display()} on {self.date}"

class Photo(models.Model):
  url = models.CharField(max_length=250)
  milestone = models.OneToOneField(Milestone, on_delete=models.CASCADE)

  def __str__(self):
    return f"Photo for Baby_id: {self.milestone_id} @{self.url}"

def get_absolute_url(self):
  return reverse('tips-catgory_details', kwargs={'pk': self.id})