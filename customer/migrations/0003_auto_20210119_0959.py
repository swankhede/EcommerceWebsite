# Generated by Django 3.0.6 on 2021-01-19 09:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('istore', '0009_products_reviews'),
        ('customer', '0002_cart_product_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='product_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='istore.products'),
        ),
    ]
