from django.shortcuts import render
from .models import Tips

from django.http import HttpResponse

# Define the home view
def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def profile(request):
  return render(request, 'profile.html')

def tips(request):
  return render(request, 'tips.html')
# Create your views here.
