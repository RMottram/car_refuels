from django import forms
from .models import RefuelSession

class RefuelForm(forms.ModelForm):
    class Meta:
        model = RefuelSession
        fields = ['date', 'fuel_type', 'pence_per_litre', 'litres_filled']