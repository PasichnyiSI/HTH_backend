# Generated by Django 5.1.5 on 2025-02-18 10:09

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0001_initial'),
        ('orders', '0003_order_total_price_alter_order_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='checkoutdetail',
            name='order',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='orders.order'),
        ),
    ]
