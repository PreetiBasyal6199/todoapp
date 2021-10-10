from django import forms
from django.db.models.base import Model
from django  import forms
from .models import todoList

class todoForm(forms.ModelForm):
    class Meta:
        model=todoList
        fields='__all__'
