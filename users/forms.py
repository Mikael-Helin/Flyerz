from django import forms
from .models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.core.validators import MinLengthValidator # https://docs.djangoproject.com/en/5.1/ref/validators/#built-in-validators

class UserRegistrationForm(UserCreationForm):

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
    )

    password1 = forms.CharField(
        label='Password',
        widget=forms.PasswordInput(attrs={'placeholder': 'Enter your password.'}),
        error_messages={
            'min_length': 'Your password must contain at least 8 characters.'
        },
    )

    password2 = forms.CharField(
        label='Password confirmation',
        widget=forms.PasswordInput(attrs={'placeholder': 'Enter your password again.'}),
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

class UserUpdateForm(UserChangeForm):
    password = None # Hide the password field from the form

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
        widget=forms.TextInput(attrs={'placeholder': 'Enter your username.'})
    )

    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'placeholder': 'Enter your email address.'}),
    )

    first_name = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={'placeholder': 'Enter your first name.'}),
    )

    last_name = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={'placeholder': 'Enter your last name.'}),
    )

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'profile_picture']
