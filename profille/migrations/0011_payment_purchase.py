# Generated by Django 5.1 on 2024-08-14 11:10

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profille', '0010_purchase_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='payment',
            name='purchase',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='profille.purchase', verbose_name='Покупка'),
        ),
    ]
