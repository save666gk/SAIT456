from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import UserRegisterForm, UserLoginForm, PasswordResetRequestForm
from django.http import JsonResponse

import random
from django.core.mail import send_mail
from django.http import JsonResponse
from .models import EmailVerificationCode, PasswordResetCode

import random
from django.core.mail import send_mail
from django.http import JsonResponse
from .forms import UserRegisterForm

def generate_otp():
    return str(random.randint(100000, 999999))  # Генерация 6-значного кода

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            request.session['registration_data'] = form.cleaned_data
            otp = generate_otp()
            request.session['otp'] = otp

            send_mail(
                'Подтверждение регистрации',
                f'Ваш код подтверждения: {otp}',
                'danilka_1971@mail.ru',
                [form.cleaned_data['email']],
                fail_silently=False,
            )
            return JsonResponse({'message': 'Пожалуйста, введите код, отправленный на вашу почту.'})
        else:
            return JsonResponse({'errors': form.errors}, status=400)
    else:
        form = UserRegisterForm()
    return render(request, 'accounts/register.html', {'form': form})



from django.contrib.auth.models import User
from django.shortcuts import render
from django.http import JsonResponse

def confirm_email(request):
    if request.method == 'POST':
        code = request.POST.get('otp_code')
        saved_otp = request.session.get('otp')

        if code == saved_otp:
            registration_data = request.session.get('registration_data')

            if registration_data:
                user = User.objects.create_user(
                    username=registration_data['username'],
                    password=registration_data['password1'],
                    email=registration_data['email'],
                    first_name=registration_data.get('first_name', ''),
                    last_name=registration_data.get('last_name', ''),
                    is_active=True
                )
                del request.session['registration_data']
                del request.session['otp']

                messages.success(request, 'Ваш email был подтвержден!')
                return JsonResponse({'message': 'Ваш аккаунт активирован!'})
            else:
                return JsonResponse({'message': 'Ошибка при создании аккаунта.'}, status=400)
        else:
            return JsonResponse({'message': 'Неверный код подтверждения.'}, status=400)
    return render(request, 'accounts/confirm_email.html')


from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import UserLoginForm  # Make sure to import the correct form


def login_view(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)  # Only pass data=request.POST
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')

            # Attempt to authenticate with username or email
            user = authenticate(username=username, password=password)
            if not user:
                try:
                    user_obj = User.objects.get(email=username)
                    user = authenticate(username=user_obj.username, password=password)
                except User.DoesNotExist:
                    user = None

            if user is not None:
                login(request, user)
                return redirect('profille:glav')  # Redirect to profile
    else:
        form = UserLoginForm()

    return render(request, 'accounts/login.html', {'form': form})


from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.contrib import messages
from django.http import JsonResponse
from .models import PasswordResetCode
from .forms import PasswordResetRequestForm, PasswordResetConfirmForm
import random

def generate_otp():
    return str(random.randint(100000, 999999))

def password_reset_request(request):
    if request.method == 'POST':
        form = PasswordResetRequestForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            try:
                user = User.objects.get(email=email)
                otp = generate_otp()

                # Сохраняем OTP в модели PasswordResetCode
                PasswordResetCode.objects.create(user=user, code=otp)

                # Отправляем email с кодом
                send_mail(
                    'Сброс пароля',
                    f'Ваш код для сброса пароля: {otp}',
                    'danilka_1971@mail.ru',
                    [email],
                    fail_silently=False,
                )
                messages.success(request, 'Код для сброса пароля был отправлен на вашу почту.')
                return redirect('accounts:password_reset_confirm')  # Исправленный redirect
            except User.DoesNotExist:
                form.add_error('email', 'Пользователь с таким email не найден.')
    else:
        form = PasswordResetRequestForm()

    return render(request, 'accounts/password_reset_request.html', {'form': form})


def password_reset_confirm(request):
    if request.method == 'POST':
        form = PasswordResetConfirmForm(request.POST)
        if form.is_valid():
            otp_code = form.cleaned_data['otp_code']
            new_password = form.cleaned_data['new_password']

            try:
                reset_code = PasswordResetCode.objects.get(code=otp_code)
                user = reset_code.user
                user.set_password(new_password)
                user.save()

                # Обновляем сессию, чтобы пользователь оставался аутентифицированным
                update_session_auth_hash(request, user)

                reset_code.delete()  # Удаляем использованный код
                messages.success(request, 'Ваш пароль был успешно изменен.')
                return redirect('accounts:login')
            except PasswordResetCode.DoesNotExist:
                form.add_error('otp_code', 'Неверный код подтверждения.')
    else:
        form = PasswordResetConfirmForm()

    return render(request, 'accounts/password_reset_confirm.html', {'form': form})



@login_required
def logout_view(request):
    logout(request)
    return redirect('accounts:login')


@login_required
def profile_view(request):
    context = {
        'user_name': request.user.username,
        'user_email': request.user.email,
    }
    return render(request, 'profille:home', context)


