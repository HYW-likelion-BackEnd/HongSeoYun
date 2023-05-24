from django import forms
from .models import Todo

class TodoForm(forms.ModelForm):
    class Mate:
        model = Todo
        fields = ('title', 'description', 'important')