from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import UserRegisterForm, UserLoginForm
from django.http import JsonResponse

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False  # Отключить активность пользователя до подтверждения
            user.save()
            messages.success(request, 'Ваш аккаунт был создан! Пожалуйста, подтвердите ваш email.')
            return JsonResponse({'message': 'Пожалуйста, подтвердите ваш email для завершения регистрации.'})
        else:
            return JsonResponse({'errors': form.errors}, status=400)
    else:
        form = UserRegisterForm()
    return render(request, 'accounts/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = UserLoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('profille:glav')  # Перенаправление в личный кабинет в приложении profille
    else:
        form = UserLoginForm()
    return render(request, 'accounts/login.html', {'form': form})

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