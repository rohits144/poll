from django import forms
from .models import Questions


class CreatePollForm(forms.ModelForm):
    class Meta:
        model = Questions
        fields = ["question", "enabled", "created_by"]

