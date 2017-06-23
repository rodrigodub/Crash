from django import forms
from .models import CCTransistor


class TransistorForm(forms.ModelForm):
    class Meta:
        model = CCTransistor
        fields = ('collector', 'emitter', 'base',)


class TransistorFormUpdate(forms.ModelForm):
    class Meta:
        model = CCTransistor
        fields = ('collector', 'base',)