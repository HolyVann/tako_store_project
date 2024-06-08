
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.contrib import auth, messages
from django.urls import reverse
from carts.models import Cart
from users.forms import UserLoginForm, UserRegistrationForm, ProfileForm
from django.contrib.auth.decorators import login_required
from django.db.models import Prefetch
from orders.models import Order, OrderItem


def login(request):

  if request.method == 'POST':
    form = UserLoginForm(data=request.POST)
    if form.is_valid():
      username = request.POST['username']
      password = request.POST['password']
      user = auth.authenticate(username=username, password=password)

      session_key = request.session.session_key

      if user:
        auth.login(request, user)
        # messages.success(request, f'{username}, Добро пожаловать')

        if session_key:
          Cart.objects.filter(session_key=session_key).update(user=user)


        redirect_page = request.POST.get('next', None)
        if redirect_page and redirect_page != reverse('user:logout'):
          return HttpResponseRedirect(request.POST.get('next'))

        return HttpResponseRedirect(reverse('main:index'))
  else:
    form = UserLoginForm()

  title = 'TAKO STORE - Авторизация'
  page_title = 'Авторизация'

  return render(request, 'users/login.html', locals())


def registration(request):

  if request.method == 'POST':
      form = UserRegistrationForm(data=request.POST)
      if form.is_valid():
        form.save()

        session_key = request.session.session_key

        user = form.instance
        auth.login(request, user)

        if session_key:
          Cart.objects.filter(session_key=session_key).update(user=user)

        # messages.success(request, f'{user.username}, Вы успешно зарегестрированы')
        return HttpResponseRedirect(reverse('main:index'))
  else:
      form = UserRegistrationForm()

  title = 'TAKO STORE - Регистрация'
  page_title = 'Регистрация'

  return render(request, 'users/registration.html', locals())


@login_required
def profile(request):

  if request.method == 'POST':
    form = ProfileForm(data=request.POST, instance=request.user, files=request.FILES)
    if form.is_valid():
      form.save()
      # messages.success(request, 'Личные данные обновлены')
      return HttpResponseRedirect(reverse('user:profile'))
  else:
    form = ProfileForm(instance=request.user)

  orders = (
    Order.objects.filter(user=request.user).prefetch_related(
      Prefetch(
        'orderitem_set',
        queryset=OrderItem.objects.select_related('product_variant'),
        )
    ).order_by('-id')
  )

  page_title = 'Профиль'

  title = 'TAKO STORE - Профиль'

  return render(request, 'users/profile.html', locals())


@login_required
def logout(request):
  # messages.success(request, f'{request.user.username}, Вы вышли из аккаунта')
  auth.logout(request)

  return redirect(reverse('main:index'))


def cart(request):

  title = 'TAKO STORE - Корзина'
  page_title = 'Корзина'

  return render(request, "carts/cart.html", locals())
