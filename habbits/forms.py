from django import forms
from .models import habbit

class HabbitForm(forms.ModelForm):
    class Meta:
        model = habbit
        fields = ['title', 'description']