# Generated by Django 4.2.11 on 2024-05-23 08:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_alter_orderitem_product'),
    ]

    operations = [
        migrations.RenameField(
            model_name='orderitem',
            old_name='product',
            new_name='product_variant',
        ),
    ]
