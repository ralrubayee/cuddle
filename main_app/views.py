from django.contrib.auth.models import User
from django.shortcuts import redirect,render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .models import Tips_catgory ,Tips, Milestone ,Photo
import uuid
import boto3
from .forms import TipsForm
from django.contrib.auth.mixins import LoginRequiredMixin

from django.contrib.auth.views import LoginView

S3_BASE_URL = 'https://s3.us-east-2.amazonaws.com/'
BUCKET = 'my-cuddle-app'


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

def profile(request):
  milestone = Milestone.objects.filter(user=request.user)
  return render(request, 'profile/profile.html',
   {'milestone': milestone})


def about(request):
  return render(request, 'about.html')
  
@login_required
def milestone_detail(request, milestone_id):
  milestone = Milestone.objects.get(id=milestone_id)
  return render(request, 'profile/milestone_detail.html', {'milestone': milestone})

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
    'tips_form':tips_form
    })

@login_required
def add_tip(request, Tips_catgory_id):
  form = TipsForm(request.POST)
  if form.is_valid():
    new_tip = form.save(commit=False)
    new_tip.catgory_id = Tips_catgory_id
    new_tip.save()
  return redirect("tips-catgory")


@login_required
def add_photo(request, milestone_id):
  photo_file = request.FILES.get('photo-file', None)
  if photo_file:
    s3 = boto3.client('s3')
    key = uuid.uuid4().hex + photo_file.name[photo_file.name.rfind('.'):]
    try:
      s3.upload_fileobj(photo_file, BUCKET, key)
      url = f"{S3_BASE_URL}{BUCKET}/{key}"
      photo = Photo(url=url, milestone_id=milestone_id)
      milestone_photo = Photo.objects.filter(milestone_id=milestone_id)
      if milestone_photo.first():
        milestone_photo.first().delete()
      photo.save()
    except Exception as err:
      print('An error occurred uploading file to S3: %s' % err)
  return redirect('profile') 


class MilestoneCreate(LoginRequiredMixin, CreateView):
  model = Milestone
  fields = '__all__'
  success_url = '/profile/'

  def form_valid(self, form):
    form.instance.user = self.request.user
    return super().form_valid(form)

class TipUpdate(LoginRequiredMixin ,UpdateView):
  model = Tips
  fields = ['Name','title','description','catgory']
  success_url = '/tips-catgory/'


class TipDelete(LoginRequiredMixin, DeleteView):
  model = Tips
  success_url = '/tips-catgory/'


