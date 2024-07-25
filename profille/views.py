from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from profille.models import Product


# Create your views here.
@login_required
def home(request):
    context = {
        'username': request.user.username,
        'email': request.user.email
    }
    return render(request, 'profille/home.html', context)
@login_required
def prof(request):
    products = Product.objects.all()  # Отображаем все продукты
    return render(request, 'prof.html', {'products': products})
@login_required
def glav(request):
    return render(request, 'glav.html')

@login_required
def mybay(request):
    return render(request, 'mybay.html')

@login_required
def bay(request):
    return render(request, 'bay.html')

@login_required
def drova(request):
    return render(request, 'drova.html')

@login_required
def oplata(request):
    return render(request, 'oplata.html')

