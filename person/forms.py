from django import forms
from .models import Person


class Person_Create(forms.ModelForm):
    class Meta:
        model = Person
        fields = [
            'name',
            'surname',
            'age',
            'image',
        ]
