# Generated by Django 4.2.11 on 2024-05-13 12:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('favorites', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='favorites',
            options={'verbose_name': 'Избранные', 'verbose_name_plural': 'Избранное'},
        ),
    ]
