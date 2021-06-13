from django.forms import fields
from Mobiles.models import Payment
from django import forms

class Payment(forms.ModelForm):
    class Meta:
        model = Payment
        fields = '__all__'
        