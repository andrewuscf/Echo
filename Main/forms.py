from django import forms
from Main.models import Track


class AddTrackForm(forms.Form):
    class Meta:
        model = Track
        fields = ('name',)