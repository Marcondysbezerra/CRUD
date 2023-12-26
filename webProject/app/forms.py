from django import forms
from .models import GeekModel

class GeeksForm(forms.ModelForm):

    class Meta:
        model = GeekModel
        fields = [
            'title',
            'description'
        ]