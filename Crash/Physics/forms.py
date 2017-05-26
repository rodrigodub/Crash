from django import forms
from .models import HTVector

class VectorForm(forms.ModelForm):
    # name = forms.CharField(label="Vector name", max_length=30, required=False)
    # m = forms.FloatField(label="Magnitude", required=False)
    # theta = forms.FloatField(label="Angle", required=False)
    # x = forms.FloatField(label="Component x", required=False)
    # y = forms.FloatField(label="Component y", required=False)

    class Meta:
        model = HTVector
        fields = ('name', 'm', 'theta', 'x', 'y',)