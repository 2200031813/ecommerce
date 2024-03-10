# app/forms.py
#from django import forms
#from .models import Feedback  # Assuming you have a Feedback model defined in models.py
from django.forms import forms

from CommerceKart.app.models import Feedback


class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ['first_name', 'last_name', 'email', 'country', 'feedback_text']
