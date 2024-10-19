from django import forms
from .models import Contact

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'profession', 'tel_number', 'email_address', 'address']

        # Modify the widgets
        widgets = {
            'address': forms.TextInput(attrs={'class': 'form-control'}),  # Use TextInput for a smaller box
        }
