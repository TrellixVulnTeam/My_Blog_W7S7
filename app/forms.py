from django import forms
from .models import comment


class commentForm(forms.Form):
    class Meta:
        model=comment
        fields=('name','email','body')