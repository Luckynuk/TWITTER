from django import forms 
from .models import Display
class Display_Form(forms.ModelForm):
    class Meta:
        model = Display 
        fields = '__all__'