from django import forms

class VectorForm(forms.Form):
    vectorInputName = forms.CharField(label="Vector name", max_length=30, required=False)
    vectorMagnitude = forms.FloatField(label="Magnitude", required=False)
    vectorAngle = forms.FloatField(label="Angle", required=False)
    vectorX = forms.FloatField(label="Component x", required=False)
    vectorY = forms.FloatField(label="Component y", required=False)