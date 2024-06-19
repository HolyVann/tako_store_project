from django.db import models
from goods.models import Products, Variants
from users.models import User


class OrderitemQueryset(models.QuerySet):

  def total_price(self):
    return sum(cart.products_price() for cart in self)

  def total_quantity(self):
    if self:
      return sum(cart.quantity for cart in self)
    return 0


class Order(models.Model):

  status = (
    ('Принят', 'Принят',),
    ('В обработке', 'В обработке',),
    ('Подтвержден', 'Подтвержден',),
    ('Заказ в сборке', 'Заказ в сборке',),
    ('Ожидание отправки', 'Ожидание отправки',),
    ('Доставляется', 'Доставляется',),
    ('Готов к получению', 'Готов к получению',),
    ('Отменен', 'Отменен',),
    ('Возврат', 'Возврат',),
  )

  user = models.ForeignKey(to=User, on_delete=models.SET_DEFAULT, blank=True, null=True, verbose_name='Пользователь', default=None)
  created_timestamp = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания заказа')
  phone_number = models.CharField(max_length=20, verbose_name='Номер телефона')
  email = models.CharField(max_length=50, verbose_name='Email')
  requires_delivery = models.BooleanField(default=False, verbose_name="Трубуется доставка")
  delivery_address = models.TextField(null=True, blank=True, verbose_name='Адрес доставки')
  payment_on_get = models.BooleanField(default=False, verbose_name='Оплата при получении')
  is_paid = models.BooleanField(default=False, verbose_name='Оплачено')
  status = models.CharField(max_length=50, choices=status, default=status[0][0], verbose_name='Статус заказа')
  comment = models.CharField(max_length=150, blank=True, null=True, verbose_name='Комментарий к заказу')


  class Meta:
    db_table = 'order'
    verbose_name = 'Заказ'
    verbose_name_plural = 'Заказы'


  def __str__(self):
    return f'Заказ № {self.pk}'


class OrderItem(models.Model):
  order = models.ForeignKey(to=Order, on_delete=models.CASCADE, verbose_name='Заказ')
  product_variant = models.ForeignKey(to=Variants, on_delete=models.SET_DEFAULT, null=True, verbose_name='Продукт', default=None)
  name = models.CharField(max_length=150, verbose_name='Название')
  price = models.DecimalField(max_digits=7, decimal_places=2, verbose_name='Цена')
  quantity = models.PositiveIntegerField(default=0, verbose_name='Количество')
  created_timestamp = models.DateTimeField(auto_now_add=True, verbose_name='Дата продажи')


  class Meta:
    db_table = 'order_item'
    verbose_name = 'Проданный товар'
    verbose_name_plural = 'Проданные товары'

  objects = OrderitemQueryset.as_manager()

  def products_price(self):
    return round(self.price*self.quantity, 2)

  def __str__(self):
    return f'Товар {self.name} | Заказ № {self.order.pk}'
