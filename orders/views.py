from django.forms import ValidationError
from django.shortcuts import redirect, render
from orders.forms import CreateOrderForm
from carts.models import Cart
from orders.models import Order, OrderItem
from django.db import transaction
from django.contrib import messages
from django.contrib.auth.decorators import login_required


@login_required
def checkout(request):

  if request.method == 'POST':
    form = CreateOrderForm(data=request.POST)
    if form.is_valid():
      try:
        with transaction.atomic():
          user = request.user
          cart_items = Cart.objects.filter(user=user)

          if cart_items.exists():
            order = Order.objects.create(
              user = user,
              email = form.cleaned_data['email'],
              phone_number = form.cleaned_data['phone_number'],
              requires_delivery = form.cleaned_data['requires_delivery'],
              delivery_address = form.cleaned_data['delivery_address'],
              payment_on_get = form.cleaned_data['payment_on_get'],
              comment = form.cleaned_data['comment'],
            )

            for cart_item in cart_items:
              product = cart_item.product_variant
              name = cart_item.product_variant.product.name
              price = cart_item.product_variant.product.sell_price()
              quantity = cart_item.quantity

              if product.quantity < quantity:
                raise ValidationError(f'Недостаточное количество товара {name} на складе, в наличии - {product.quantity}')

              OrderItem.objects.create(
                order=order,
                product_variant=product,
                name=name,
                price=price,
                quantity=quantity,
              )

              product.quantity -= quantity
              product.save()

            cart_items.delete()

            messages.success(request, f'Заказ оформлен!')

            return redirect('user:profile')
      except ValidationError as e:
        messages.success(request, ''.join(e))
        return redirect('orders:checkout')
  else:
    initial = {
      'first_name': request.user.first_name,
      'email': request.user.email,
    }

    form = CreateOrderForm(initial=initial)

  context = {
    'title': 'TAKO STORE - Оформление заказа',
    'page_title': 'Оформление заказа',
    'form': form,
  }

  return render(request, 'orders/create_order.html', context=context)
