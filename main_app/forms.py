from django.forms import ModelForm
from .models import Tips

class TipsForm(ModelForm):
  class Meta:
    model = Tips
    fields = ['Name', 'title', 'description']

