# Generated by Django 4.2.11 on 2024-03-26 09:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='new',
            field=models.BooleanField(default=None, verbose_name='Новинка'),
        ),
    ]
