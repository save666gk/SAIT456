from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class UserLoginForm(AuthenticationForm):
    username = forms.CharField(label='Username')
    password = forms.CharField(widget=forms.PasswordInput)


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
