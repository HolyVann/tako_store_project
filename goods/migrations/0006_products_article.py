# Generated by Django 4.2.11 on 2024-05-13 12:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0005_alter_gallery_options_alter_gallery_table'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='article',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Артикул'),
        ),
    ]
