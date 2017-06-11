from django import forms
from .models import CCTransistor


class TransistorForm(forms.ModelForm):
    class Meta:
        model = CCTransistor

