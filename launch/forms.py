# landing/forms.py

from django import forms
from .models import Feedback, Waitlist


class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ["name", "email", "message"]


class WaitlistForm(forms.ModelForm):
    class Meta:
        model = Waitlist
        fields = ["email"]