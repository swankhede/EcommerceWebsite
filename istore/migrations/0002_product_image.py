# Generated by Django 3.0.6 on 2021-01-07 09:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('istore', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, upload_to='media'),
        ),
    ]