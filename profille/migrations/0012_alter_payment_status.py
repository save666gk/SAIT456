# Generated by Django 5.1 on 2024-08-14 11:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profille', '0011_payment_purchase'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='status',
            field=models.CharField(choices=[('completed', 'Выполнен'), ('in_progress', 'В работе'), ('cancelled', 'Отменен')], default='in_progress', max_length=20, verbose_name='Статус'),
        ),
    ]
