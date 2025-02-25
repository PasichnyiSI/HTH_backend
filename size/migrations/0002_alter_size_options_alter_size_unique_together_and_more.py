# Generated by Django 5.1.5 on 2025-02-07 09:04

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_alter_product_price_per_sq_m_alter_product_slug'),
        ('size', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='size',
            options={},
        ),
        migrations.AlterUniqueTogether(
            name='size',
            unique_together=set(),
        ),
        migrations.AlterField(
            model_name='size',
            name='name',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='size',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
        migrations.AlterField(
            model_name='size',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sizes', to='main.product'),
        ),
    ]
