# Generated by Django 5.1.5 on 2025-02-07 12:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('size', '0003_remove_size_price_remove_size_product_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productsize',
            name='price',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
        ),
    ]
