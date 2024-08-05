from django import forms
from .models import Contact


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ["gmail", "name", "subject", "message"]
        widgets = {
            "gmail": forms.EmailInput(
                attrs={"class": "gmail-input", "placeholder": "Gmail"}
            ),
            "name": forms.TextInput(
                attrs={"class": "name-input", "placeholder": "Name"}
            ),
            "subject": forms.TextInput(
                attrs={"class": "subject-input", "placeholder": "Subject"}
            ),
            "message": forms.Textarea(
                attrs={"class": "message-input", "placeholder": "Message"}
            ),
        }
