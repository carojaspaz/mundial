from django import forms
from .models import Player


class PlayerCreateForm(forms.ModelForm):
    class Meta:
        model = Player
        # Excluye el campo de selección del formulario
        exclude = ('selection',)


class PlayerUpdateForm(forms.ModelForm):
    class Meta:
        model = Player
        # Excluye el campo de selección del formulario
        exclude = ('selection',)
