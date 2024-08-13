from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from profille.models import Product, Update


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
    user_purchases = Purchase.objects.filter(user=request.user).order_by('-purchase_date')
    return render(request, 'bay.html', {'purchases': user_purchases})

@login_required
def drova(request):
    updates = Update.objects.all()  # Отображаем
    return render(request, 'drova.html', {'updates': updates})

@login_required
def oplata(request):
    return render(request, 'oplata.html')

from django.conf import settings  # Для доступа к настройкам, таким как DEFAULT_FROM_EMAIL
from django.contrib.auth.decorators import login_required  # Для защиты представления от неавторизованного доступа
from django.core.mail import send_mail  # Для отправки писем
from django.shortcuts import get_object_or_404, render, redirect  # Для получения объектов, рендеринга шаблонов и редиректов
from django.utils import timezone  # Для работы с временными метками
from django.template.loader import render_to_string  # Для рендеринга HTML шаблонов в строку
from django.utils.html import strip_tags  # Для удаления HTML тегов из строки

import logging  # Для логирования, если требуется отладка

# Импорт модели Product и формы PurchaseForm
from .models import Product, Purchase
from .forms import PurchaseForm
import logging

logger = logging.getLogger(__name__)
@login_required
def buy_product(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    if request.method == 'POST':
        form = PurchaseForm(request.POST)
        if form.is_valid():
            # Создание записи о покупке
            purchase = Purchase.objects.create(
                user=request.user,
                product=product,
                purchase_date=timezone.now(),
                amount=product.price
            )

            # Подготовка данных для email
            subject = 'Подтверждение покупки'  # Определяем subject
            context = {
                'user': request.user,
                'product': product,
                'purchase': purchase,
                'name': form.cleaned_data.get('name'),
                'email': form.cleaned_data.get('email'),
                'phone': form.cleaned_data.get('phone')
            }

            logger.debug(f'Email context: {context}')  # Логируем контекст

            html_message = render_to_string('purchase_email.html', context)
            plain_message = strip_tags(html_message)
            from_email = 'danilka_1971@mail.ru'
            to_email = 'danilka_1971@mail.ru'

            # Отправка email
            send_mail(subject, plain_message, from_email, [to_email], html_message=html_message)

            return redirect('profille:success_page')
    else:
        form = PurchaseForm(initial={'product_id': product_id})

    return render(request, 'prof.html', {'product': product, 'form': form})

@login_required
def success_page(request):
    return render(request, 'success_page.html')


from django.core.mail import send_mail
from django.http import HttpResponse

def send_test_email(request):
    subject = 'Тестовое письмо'
    message = 'Это тестовое письмо для проверки настроек SMTP.'
    from_email = 'danilka_1971@mail.ru'
    recipient_list = ['danilka_1971@mail.ru']  # Замените на ваш email

    try:
        send_mail(subject, message, from_email, recipient_list)
        return HttpResponse('Письмо успешно отправлено.')
    except Exception as e:
        return HttpResponse(f'Ошибка при отправке письма: {str(e)}')



