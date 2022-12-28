from django import forms
from django.forms.widgets import HiddenInput

from .models import Event, Player, Prize


class PlayerUpdateForm(forms.ModelForm):
    class Meta:
        model = Player
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["name"].widget = HiddenInput()
        self.fields["E1"].widget.attrs.update(
            {
                "class": "form-control",
                "style": " background-color: #FFFFFF; color: #000000;",
            }
        )
        self.fields["E2"].widget.attrs.update(
            {
                "class": "form-control",
                "style": " background-color: #FFFFFF; color: #000000;",
            }
        )
        self.fields["E3"].widget.attrs.update(
            {
                "class": "form-control",
                "style": " background-color: #FFFFFF; color: #000000;",
            }
        )
        self.fields["E4"].widget.attrs.update(
            {
                "class": "form-control",
                "style": " background-color: #FFFFFF; color: #000000;",
            }
        )
        self.fields["E5"].widget.attrs.update(
            {
                "class": "form-control",
                "style": " background-color: #FFFFFF; color: #000000;",
            }
        )
        self.fields["E6"].widget.attrs.update(
            {
                "class": "form-control",
                "style": " background-color: #FFFFFF; color: #000000;",
            }
        )
        self.fields["E7"].widget.attrs.update(
            {
                "class": "form-control",
                "style": " background-color: #FFFFFF; color: #000000;",
            }
        )
        self.fields["E8"].widget.attrs.update(
            {
                "class": "form-control",
                "style": " background-color: #FFFFFF; color: #000000;",
            }
        )
        self.fields["E9"].widget.attrs.update(
            {
                "class": "form-control",
                "style": " background-color: #FFFFFF; color: #000000;",
            }
        )
        self.fields["E10"].widget.attrs.update(
            {
                "class": "form-control",
                "style": " background-color: #FFFFFF; color: #000000;",
            }
        )
        self.fields["E11"].widget.attrs.update(
            {
                "class": "form-control",
                "style": " background-color: #FFFFFF; color: #000000;",
            }
        )
        self.fields["E12"].widget.attrs.update(
            {
                "class": "form-control",
                "style": " background-color: #FFFFFF; color: #000000;",
            }
        )


class PrizeUpdateForm(forms.ModelForm):
    class Meta:
        model = Prize
        fields = ("total_prize",)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["total_prize"].widget.attrs.update(
            {
                "class": "form-control",
                "style": " background-color: #FFFFFF; color: #000000;",
            }
        )


class EventUpdateForm(forms.ModelForm):

    event_date = forms.DateField(
        widget=forms.TextInput(attrs={"type": "date"}), required=True
    )

    class Meta:
        model = Event
        fields = "__all__"

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.fields['name'].widget.attrs.update(
    #         {'class': 'form-control', 'style': ' background-color: #FFFFFF; color: #000000;'})
    #     self.fields['event_date'].widget.attrs.update(
    #         {'class': 'datepicker', 'style': ' background-color: #FFFFFF; color: #000000;'})
    #     self.fields['notes'].widget.attrs.update(
    #         {'class': 'form-control', 'style': ' background-color: #FFFFFF; color: #000000;'})


class EventCreateForm(forms.ModelForm):

    event_date = forms.DateField(
        widget=forms.TextInput(attrs={"type": "date"}), required=True
    )

    class Meta:
        model = Event
        fields = "__all__"
