from django import forms
from django.forms.widgets import HiddenInput
from .models import Player


class PlayerUpdateForm(forms.ModelForm):
    class Meta:
        model = Player
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget = HiddenInput()
        self.fields['S1E1'].widget.attrs.update(
            {'class': 'form-control', 'style': ' background-color: #FFFFFF; color: #000000;'})
        self.fields['S1E2'].widget.attrs.update(
            {'class': 'form-control', 'style': ' background-color: #FFFFFF; color: #000000;'})
        self.fields['S1E3'].widget.attrs.update(
            {'class': 'form-control', 'style': ' background-color: #FFFFFF; color: #000000;'})
        self.fields['S1E4'].widget.attrs.update(
            {'class': 'form-control', 'style': ' background-color: #FFFFFF; color: #000000;'})
        self.fields['S1E5'].widget.attrs.update(
            {'class': 'form-control', 'style': ' background-color: #FFFFFF; color: #000000;'})
        self.fields['S1E6'].widget.attrs.update(
            {'class': 'form-control', 'style': ' background-color: #FFFFFF; color: #000000;'})
        self.fields['S1E7'].widget.attrs.update(
            {'class': 'form-control', 'style': ' background-color: #FFFFFF; color: #000000;'})
        self.fields['S1E8'].widget.attrs.update(
            {'class': 'form-control', 'style': ' background-color: #FFFFFF; color: #000000;'})
        self.fields['S1E9'].widget.attrs.update(
            {'class': 'form-control', 'style': ' background-color: #FFFFFF; color: #000000;'})
        self.fields['S1E10'].widget.attrs.update(
            {'class': 'form-control', 'style': ' background-color: #FFFFFF; color: #000000;'})
        self.fields['S1E11'].widget.attrs.update(
            {'class': 'form-control', 'style': ' background-color: #FFFFFF; color: #000000;'})
        self.fields['S1E12'].widget.attrs.update(
            {'class': 'form-control', 'style': ' background-color: #FFFFFF; color: #000000;'})
