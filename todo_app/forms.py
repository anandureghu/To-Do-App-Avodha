from .models import ToDo
from django import forms

class UpdateForm(forms.ModelForm):
    class Meta:
        model = ToDo
        fields = ['subject', 'priority', 'date']
        
