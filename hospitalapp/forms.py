from django import forms
from .models import Floresta

class Florestaform(forms.ModelForm):
    class Meta:
        model = Floresta
        fields = '__all__'