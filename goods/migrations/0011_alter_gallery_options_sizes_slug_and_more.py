# Generated by Django 4.2.11 on 2024-05-22 18:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0010_sizes_variants'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='gallery',
            options={'verbose_name': 'Изображение', 'verbose_name_plural': 'Галерея'},
        ),
        migrations.AddField(
            model_name='sizes',
            name='slug',
            field=models.SlugField(blank=True, max_length=200, null=True, verbose_name='URL'),
        ),
        migrations.AlterField(
            model_name='variants',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='variants', to='goods.products', verbose_name='Продукт'),
        ),
        migrations.AlterField(
            model_name='variants',
            name='size',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='goods.sizes', verbose_name='Размер'),
        ),
    ]
