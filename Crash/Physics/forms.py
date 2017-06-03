from django import forms
from .models import HTVector


class VectorFormMTheta(forms.ModelForm):
    class Meta:
        model = HTVector
        fields = ('name', 'm', 'theta', )


class VectorFormXY(forms.ModelForm):
    class Meta:
        model = HTVector
        fields = ('name', 'x', 'y', )
