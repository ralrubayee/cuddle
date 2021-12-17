from django.contrib.auth.models import User
from django.shortcuts import redirect,render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .models import Tips_catgory ,Tips
from .forms import TipsForm
from django.contrib.auth.mixins import LoginRequiredMixin

from django.contrib.auth.views import LoginView


# Define the home view
def signup(request):
  error_message = ''
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      return redirect('tips-catgory')
    else:
      error_message = 'Invalid sign up - try again'
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'signup.html', context)



class Home(LoginView):
  template_name = 'home.html'

def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

@login_required
def profile(request):
  return render(request, 'profile.html')

@login_required
def tips(request):
  tipsCatgory = Tips_catgory.objects.all()
  return render(request, 'tips/tips-catgory.html', {'tipsCatgory': tipsCatgory})

@login_required
def tips_detail(request, Tips_catgory_id):
  catgory = Tips_catgory.objects.get(id=Tips_catgory_id)
  tips_form = TipsForm()
  return render(request, 'tips/detail.html',  {
    'tipsCatgory':catgory,
    'tips':tips_form
    })



class TipCreate(CreateView):
  model = Tips
  fields = '__all__'
  success_url = '/tips-catgory/'

class TipUpdate (LoginRequiredMixin ,UpdateView):
  model = Tips
  fields = ['Name','title' , 'description','catgory']
  success_url = '/tips-catgory/'

class TipDelete(LoginRequiredMixin, DeleteView):
  model = Tips
  success_url = '/tips-catgory/'


