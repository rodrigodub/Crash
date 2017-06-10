from django import forms
from .models import HTVector, HTExercise


class VectorFormMTheta(forms.ModelForm):
    class Meta:
        model = HTVector
        fields = ('name', 'm', 'theta', )


class VectorFormXY(forms.ModelForm):
    class Meta:
        model = HTVector
        fields = ('name', 'x', 'y', )


class ExerciseForm(forms.ModelForm):
    class Meta:
        model = HTExercise
        fields = ('book', 'volume', 'chapter', 'page', 'exercise')
