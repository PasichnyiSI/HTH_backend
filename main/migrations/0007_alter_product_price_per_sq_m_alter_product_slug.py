# Generated by Django 5.1.5 on 2025-02-07 08:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_remove_product_price_product_price_per_sq_m'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='price_per_sq_m',
            field=models.DecimalField(decimal_places=2, help_text='Ціна за 1 кв.м', max_digits=10),
        ),
        migrations.AlterField(
            model_name='product',
            name='slug',
            field=models.SlugField(unique=True),
        ),
    ]
