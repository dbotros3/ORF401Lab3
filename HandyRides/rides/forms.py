from django import forms
from .models import Person


class RideForm(forms.Form):
  search_orig = forms.CharField(label='Search Origination/Destination City', max_length=64, required=False)
  search_dest = forms.CharField(label='Search Destination State', max_length=64, required=False)


class NewRideForm(forms.ModelForm):
  class Meta:
    model = Person
    exclude = []
