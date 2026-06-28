# landing/forms.py

from django import forms
from .models import Feedback, Waitlist


class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ["name", "email", "message"]
        widgets = {
            # Changes the input type from "email" to "text"
            "email": forms.TextInput(
                attrs={
                    "placeholder": "Enter your email address or Phone numbers",
                }
            ),
        }


class WaitlistForm(forms.ModelForm):
    class Meta:
        model = Waitlist
        fields = ["email"]
        widgets = {
            # Changes the input type from "email" to "text"
            "email": forms.TextInput(
                attrs={
                    "placeholder": "Enter your email address or Phone numbers",
                }
            ),
        }