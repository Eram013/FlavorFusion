from django import forms
from .models import user2  

class RegistrationForm(forms.ModelForm):
    confirm_password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = user2
        fields = ['username', 'email', 'password', 'confirm_password']
    
    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password and confirm_password and password != confirm_password:
            raise forms.ValidationError("Passwords do not match.")

class LoginForm(forms.Form):
    username = forms.CharField(max_length=50,
    widget=forms.TextInput(attrs={
        'placeholder': '👤 Username',
        'required': 'required',
        'style':'width: 100%; padding: 15px; border: 2px solid grey; border-radius: 5px; font-size: 14px; transition: border 0.3s; outline: none;'
    })
    )
    password = forms.CharField(
    widget=forms.PasswordInput(attrs={
        'placeholder': '🔒 Password',
        'required': 'required',
        'style':'width: 100%; padding: 15px; border: 2px solid grey; border-radius: 5px; font-size: 14px; transition: border 0.3s; outline: none;'
    })
    )

