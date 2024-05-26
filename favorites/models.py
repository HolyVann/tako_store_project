from django.db import models
from users.models import User
from goods.models import Products


class FavoriteQueryset(models.QuerySet):

  def total_quantity(self):
    if self:
      return sum(favorite.quantity for favorite in self)
    return 0


class Favorites(models.Model):

  user = models.ForeignKey(to=User, on_delete=models.CASCADE, blank=True, null=True, verbose_name='Пользователь')
  quantity = models.PositiveSmallIntegerField(default=1, verbose_name='Количество')
  session_key = models.CharField(max_length=32, null=True,blank=True)
  product = models.ForeignKey(to=Products, on_delete=models.CASCADE, verbose_name='Продукт')



  class Meta:
    db_table = 'favorite'
    verbose_name = 'Избранное'
    verbose_name_plural = 'Избранное'


  objects = FavoriteQueryset().as_manager()

  def __str__(self):
    if self.user:
      return f'Избранное {self.user.username} | Товар {self.product.name}'

    return f'Избранное анонимно Товар {self.product.name}'
