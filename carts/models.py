from django.db import models
from users.models import User
from goods.models import Products, Variants


class CartQueryset(models.QuerySet):

  def total_price(self):
    return sum(cart.products_sell_price() for cart in self)


  def total_quantity(self):
    if self:
      return sum(cart.quantity for cart in self)
    return 0



class Cart(models.Model):

  user = models.ForeignKey(to=User, on_delete=models.CASCADE, blank=True, null=True, verbose_name='Пользователь')
  quantity = models.PositiveSmallIntegerField(default=0, verbose_name='Количество')
  session_key = models.CharField(max_length=32, null=True,blank=True)
  created_timestamp = models.DateTimeField(auto_now_add=True, verbose_name='Дата добавления')
  product_variant = models.ForeignKey(to=Variants, on_delete=models.CASCADE, verbose_name='Продукт')


  class Meta:
    db_table = 'cart'
    verbose_name = 'Корзины'
    verbose_name_plural = 'Корзины'


  objects = CartQueryset().as_manager()

  def products_price(self):
    return round(self.product_variant.product.price*self.quantity, 2)

  def products_sell_price(self):
    return round(self.product_variant.product.sell_price()*self.quantity, 2)


  def __str__(self):
    if self.user:
      return f'Корзина {self.user.username} | Товар {self.product_variant} | Количество {self.quantity}'

    return f'Анонимная корзина | Товар {self.product_variant} | Количество {self.quantity}'
