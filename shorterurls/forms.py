from django import forms


class ShortForm(forms.Form):
    yoururl = forms.URLField(
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Your URL"
        })
    )
