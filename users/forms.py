from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.core.validators import MinLengthValidator # https://docs.djangoproject.com/en/5.1/ref/validators/#built-in-validators

User = get_user_model() # googlede error message to this response https://stackoverflow.com/questions/17873855/manager-isnt-available-user-has-been-swapped-for-pet-person
class UserRegisterForm(UserCreationForm):

    username = forms.CharField(
        validators=[
            MinLengthValidator(
                3, 
                message='Your username must contain at least 3 characters.'
            ),
        ],
        error_messages={
            'unique': 'A user with that username already exists.',
        },
        widget=forms.TextInput(attrs={'placeholder': 'Enter your username.'}) # https://docs.djangoproject.com/en/5.1/ref/forms/widgets/#django.forms.Widget.attrs
    )
    
    email = forms.EmailField(
        label='Email',
        widget=forms.EmailInput(attrs={'placeholder': 'Enter your email address.'}),
        help_text='Enter your email address.',
    )

    password1 = forms.CharField(
        label='Password',
        widget=forms.PasswordInput(attrs={'placeholder': 'Enter your password.'}),
        help_text='Your password must contain at least 8 characters.',
        error_messages={
            'min_length': 'Ensure this value has at least 8 characters.'
        },
    )

    password2 = forms.CharField(
        label='Password confirmation',
        widget=forms.PasswordInput(attrs={'placeholder': 'Enter your password again.'}),
        help_text='Enter the same password as before, for verification.',
        error_messages={
            'min_length': 'Ensure this value has at least 8 characters.'
        },
    )

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('This email is already in use.')
        return email


class LoginForm(forms.Form):
    username = forms.CharField(label="username", max_length=100)
    password = forms.CharField(label="password", max_length=100)



















