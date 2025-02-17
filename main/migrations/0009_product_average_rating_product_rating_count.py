# Generated by Django 5.1.5 on 2025-02-16 08:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_alter_product_price_per_sq_m'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='average_rating',
            field=models.DecimalField(decimal_places=1, default=0.0, max_digits=2),
        ),
        migrations.AddField(
            model_name='product',
            name='rating_count',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
