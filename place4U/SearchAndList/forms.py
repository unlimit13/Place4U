from django import forms
from .models import searchedTag

class searchedTagForm(forms.Form):
    input_tag = forms.CharField(max_length=100)
    input_location = forms.CharField(max_length=100)
    
class likethresholdForm(forms.Form):
    input_threshold = forms.IntegerField()
    