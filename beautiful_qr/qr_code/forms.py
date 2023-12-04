from django import forms
from .models import QR


class QRForm(forms.ModelForm):
    class Meta:
        model = QR
        fields = ("link", "image")
