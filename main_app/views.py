from django.shortcuts import render

from django.http import HttpResponse

# Define the home view
def home(request):
  return HttpResponse('<h1>Hello</h1>')

def about(request):
  return render(request, 'about.html')

def profile(request):
  return render(request, 'profile.html')

# Create your views here.
