from django import forms

from .models import SingleTournament


class ProfileAddForm(forms.ModelForm):
    """
    Form for adding books in add_book view
    """
    # published_date = forms.CharField(required=True)

    class Meta:
        model = SingleTournament
        fields = (
            "player",
            "image",
            "points",
            "bonus_a",
            "bonus_b",
        )
