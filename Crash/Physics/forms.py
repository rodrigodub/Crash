from django import forms
from .models import HTVector, HTExercise, HTData


class VectorForm(forms.ModelForm):
    class Meta:
        model = HTVector
        fields = ('name', 'm', 'theta', 'x', 'y', )


class ExerciseForm(forms.ModelForm):
    class Meta:
        model = HTExercise
        fields = ('book', 'volume', 'chapter', 'page', 'exercise')


class ExerciseDataForm(forms.ModelForm):
    class Meta:
        model = HTData
        fields = ('container', 'variable', 'value', 'unit')
        labels = {'container': 'Exercise', }
        widgets = {'container': forms.HiddenInput(attrs={'readonly':'readonly'})}

