# Generated by Django 4.2.11 on 2024-06-13 17:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0004_alter_order_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('В обработке', 'В обработке'), ('Оформлен', 'Оформлен'), ('Готов к получению', 'Готов к получению')], default='В обработке', max_length=50, verbose_name='Статус заказа'),
        ),
    ]