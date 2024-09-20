from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('confirm-email/', views.confirm_email, name='confirm_email'),
    path('password-reset/', views.password_reset_request, name='password_reset_request'),
    path('password_reset_confirm/', views.password_reset_confirm, name='password_reset_confirm'),
]
