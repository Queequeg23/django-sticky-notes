from django import forms
from .models import Note


# ModelForm is a helper that can inspect a model and build
# form fields that correspond to the model’s fields.
class NoteForm(forms.ModelForm):
    '''
    Define a  NoteForm class inheriting from forms.ModelForm
    '''
    # Defines config. for NoteForm not attributes themselves
    class Meta:
        model = Note
        fields = ['title', 'content']
