from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.models import User

class UserLoginForm(forms.Form):
    username = forms.CharField(label="Username or Email", max_length=254)
    password = forms.CharField(label="Password", widget=forms.PasswordInput)

    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get('username')
        password = cleaned_data.get('password')

        if username and password:
            # Attempt to authenticate with username first
            user = authenticate(username=username, password=password)
            if not user:
                # If username authentication fails, try to authenticate with email
                try:
                    user_obj = User.objects.get(email=username)
                    user = authenticate(username=user_obj.username, password=password)
                except User.DoesNotExist:
                    pass

            if not user:
                raise forms.ValidationError("Invalid login credentials")

        return cleaned_data



from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True, label='Электронная почта', help_text='Введите действующий адрес электронной почты.')
    phone = forms.CharField(max_length=15, required=True, label='Телефон', help_text='Введите ваш номер телефона.')

    class Meta:
        model = User
        fields = ("username", "email", "phone", "password1", "password2")
        labels = {
            'username': 'Имя пользователя',
            'password1': 'Пароль',
            'password2': 'Подтверждение пароля',
        }
        help_texts = {
            'username': 'Введите уникальное имя пользователя.',
            'password1': 'Пароль должен содержать не менее 8 символов.',
            'password2': 'Введите тот же пароль, что и выше, для подтверждения.',
        }

def register(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('accounts:login')  # Redirect to login page after successful registration
    else:
        form = RegistrationForm()
    return render(request, 'accounts/register.html', {'form': form})


class PasswordResetRequestForm(forms.Form):
    email = forms.EmailField(label='Электронная почта', max_length=254, widget=forms.EmailInput(attrs={'class': 'form-control'}))

class PasswordResetConfirmForm(forms.Form):
    otp_code = forms.CharField(label='Код подтверждения', max_length=6, widget=forms.TextInput(attrs={'class': 'form-control'}))
    new_password = forms.CharField(label='Новый пароль', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
