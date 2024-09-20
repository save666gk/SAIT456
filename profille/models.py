from django.db import models
from django.contrib.auth.models import User



class License(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь')
    license_key = models.CharField(max_length=255, verbose_name='Ключ лицензии')
    issue_date = models.DateField(verbose_name='Дата выдачи')
    expiration_date = models.DateField(verbose_name='Дата окончания')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Создано')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Обновлено')

    def __str__(self):
        return self.license_key

    class Meta:
        verbose_name = 'Лицензия'
        verbose_name_plural = 'Лицензии'

class Purchase(models.Model):
    STATUS_CHOICES = [
        ('completed', 'Выполнен'),
        ('in_progress', 'В работе'),
        ('cancelled', 'Отменен'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь')
    product = models.ForeignKey('Product', on_delete=models.CASCADE, verbose_name='Продукт')
    purchase_date = models.DateField(verbose_name='Дата покупки')
    amount = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Сумма')
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='in_progress',  # По умолчанию статус "В работе"
        verbose_name='Статус'
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Создано')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Обновлено')

    def __str__(self):
        return f'Покупка {self.id} от {self.user.username}'

    class Meta:
        verbose_name = 'Покупка'
        verbose_name_plural = 'Покупки'

class Update(models.Model):
    product = models.ForeignKey('Product', on_delete=models.CASCADE, verbose_name='Продукт')
    version = models.CharField(max_length=255, verbose_name='Версия')
    description = models.TextField(verbose_name='Описание')
    release_date = models.DateField(verbose_name='Дата выпуска')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Создано')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Обновлено')

    def __str__(self):
        return self.version

    class Meta:
        verbose_name = 'Обновление'
        verbose_name_plural = 'Обновления'

class Payment(models.Model):
    STATUS_CHOICES = [
        ('completed', 'Выполнен'),
        ('in_progress', 'В работе'),
        ('cancelled', 'Отменен'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь')
    purchase = models.ForeignKey('Purchase', on_delete=models.CASCADE, verbose_name='Покупка', null=True, blank=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Сумма')
    payment_date = models.DateField(verbose_name='Дата платежа')
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='in_progress',  # По умолчанию статус "В работе"
        verbose_name='Статус'
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Создано')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Обновлено')

    def __str__(self):
        return f'Платеж {self.id} от {self.user.username}'

    class Meta:
        verbose_name = 'Платеж'
        verbose_name_plural = 'Платежи'


from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название')
    description = models.TextField(verbose_name='Описание')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена')
    photo = models.ImageField(upload_to='product_photos/', verbose_name='Фотография', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Создано')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Обновлено')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'



