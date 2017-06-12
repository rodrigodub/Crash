from django import forms
from .models import CCTransistor


class TransistorForm(forms.ModelForm):
    class Meta:
        model = CCTransistor
        fields = ('electrode_in', 'electrode_out', 'gate',)

