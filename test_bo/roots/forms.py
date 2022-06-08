from django import forms

from .models import Roots


class RootsForm (forms.ModelForm):
    class Meta:
        model = Roots
        fields = ('a', 'b', 'c',)
