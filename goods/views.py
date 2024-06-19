from django.shortcuts import render
from goods.models import Products, Gallery, Brands, Sizes, Variants
from django.core.paginator import Paginator
from goods.utils import q_search
from carts.models import Cart
from django.db.models import F



def catalog(request):
    order_by = request.GET.get('order_by', None)
    page = request.GET.get('page', 1)
    query = request.GET.get('q', None)
    price_from = request.GET.get('price_from', None)
    price_to = request.GET.get('price_to', None)

    if price_from or price_to:
        filter_price = True
    else:
        filter_price = False

    page_filter = 'По умолчанию'

    if query:
        goods = q_search(query)
        page_title = ''
    elif price_from or price_to:
        goods = Products.objects.all().annotate(discount_price=(F("price")-F("price")*F("discount")/100))
        page_title = 'Каталог'
        if price_to and price_from:
            goods = goods.filter(discount_price__gte=price_from).filter(discount_price__lte=price_to)
            if not goods:
                goods = Products.objects.all().order_by('-is_new')
            elif order_by and order_by != 'default':
                if order_by == 'price':
                    goods = goods.order_by('discount_price')
                    page_filter = 'По возрастанию цены'
                elif order_by == '-price':
                    goods = goods.order_by('-discount_price')
                    page_filter = 'По убыванию цены'
                else:
                    goods = goods.order_by(order_by)
                    page_filter = 'По величине скидки'
        elif price_from:
            goods = goods.filter(discount_price__gte=price_from)
            if not goods:
                goods = Products.objects.all().order_by('-is_new')
            elif order_by and order_by != 'default':
                if order_by == 'price':
                    goods = goods.order_by('discount_price')
                    page_filter = 'По возрастанию цены'
                elif order_by == '-price':
                    goods = goods.order_by('-discount_price')
                    page_filter = 'По убыванию цены'
                else:
                    goods = goods.order_by(order_by)
                    page_filter = 'По величине скидки'
        elif price_to:
            goods = goods.filter(discount_price__lte=price_to)
            if order_by and order_by != 'default':
                if order_by == 'price':
                    goods = goods.order_by('discount_price')
                    page_filter = 'По возрастанию цены'
                elif order_by == '-price':
                    goods = goods.order_by('-discount_price')
                    page_filter = 'По убыванию цены'
                else:
                    goods = goods.order_by(order_by)
                    page_filter = 'По величине скидки'
    else:
        goods = Products.objects.all().order_by('-is_new')
        page_title = 'Каталог'
        if order_by and order_by != 'default':
            if order_by == 'price':
                goods = Products.objects.all().annotate(discount_price=(F("price")-F("price")*F("discount")/100))
                goods = goods.order_by('discount_price')
                page_filter = 'По возрастанию цены'
            elif order_by == '-price':
                goods = Products.objects.all().annotate(discount_price=(F("price")-F("price")*F("discount")/100))
                goods = goods.order_by('-discount_price')
                page_filter = 'По убыванию цены'
            else:
                goods = Products.objects.all().order_by(order_by)
                page_filter = 'По величине скидки'

    paginator = Paginator(goods, 8)
    current_page = paginator.page(int(page))

    context = {
        'title': "TAKO STORE - Каталог",
        'goods': current_page,
        'page_title': page_title,
        'page_filter': page_filter,
        'filter_price': filter_price,
    }

    return render(request, "goods/catalog.html", context)


def catalog_category(request, category_slug='all'):
    order_by = request.GET.get('order_by', None)
    page = request.GET.get('page', 1)
    price_from = request.GET.get('price_from', None)
    price_to = request.GET.get('price_to', None)

    if price_from or price_to:
        filter_price = True
    else:
        filter_price = False

    page_filter = 'По умолчанию'


    if category_slug == 'all':
        if price_from or price_to:
            goods = Products.objects.all().annotate(discount_price=(F("price")-F("price")*F("discount")/100))
            page_title = 'Вся одежда'
            title = 'Вся одежда'
            if price_to and price_from:
                goods = goods.filter(discount_price__gte=price_from).filter(discount_price__lte=price_to)
                if not goods:
                    goods = Products.objects.all().order_by('-is_new')
                elif order_by and order_by != 'default':
                    if order_by == 'price':
                        goods = goods.order_by('discount_price')
                        page_filter = 'По возрастанию цены'
                    elif order_by == '-price':
                        goods = goods.order_by('-discount_price')
                        page_filter = 'По убыванию цены'
                    else:
                        goods = goods.order_by(order_by)
                        page_filter = 'По величине скидки'
            elif price_from:
                goods = goods.filter(discount_price__gte=price_from)
                if not goods:
                    goods = Products.objects.all().order_by('-is_new')
                elif order_by and order_by != 'default':
                    if order_by == 'price':
                        goods = goods.order_by('discount_price')
                        page_filter = 'По возрастанию цены'
                    elif order_by == '-price':
                        goods = goods.order_by('-discount_price')
                        page_filter = 'По убыванию цены'
                    else:
                        goods = goods.order_by(order_by)
                        page_filter = 'По величине скидки'
            elif price_to:
                goods = goods.filter(discount_price__lte=price_to)
                if order_by and order_by != 'default':
                    if order_by == 'price':
                        goods = goods.order_by('discount_price')
                        page_filter = 'По возрастанию цены'
                    elif order_by == '-price':
                        goods = goods.order_by('-discount_price')
                        page_filter = 'По убыванию цены'
                    else:
                        goods = goods.order_by(order_by)
                        page_filter = 'По величине скидки'
        else:
            goods = Products.objects.all().order_by('-is_new')
            page_title = 'Вся одежда'
            title = 'Вся одежда'
            if order_by and order_by != 'default':
                if order_by == 'price':
                        goods = Products.objects.all().annotate(discount_price=(F("price")-F("price")*F("discount")/100))
                        goods = goods.order_by('discount_price')
                        page_filter = 'По возрастанию цены'
                elif order_by == '-price':
                        goods = Products.objects.all().annotate(discount_price=(F("price")-F("price")*F("discount")/100))
                        goods = goods.order_by('-discount_price')
                        page_filter = 'По убыванию цены'
                else:
                        goods = Products.objects.all().order_by(order_by)
                        page_filter = 'По величине скидки'
    else:
        if price_from or price_to:
            goods = Products.objects.filter(category__slug=category_slug).annotate(discount_price=(F("price")-F("price")*F("discount")/100)).order_by('-is_new')
            page_title = goods[0].category.name
            title = goods[0].category.name
            if price_to and price_from:
                goods = goods.filter(discount_price__gte=price_from).filter(discount_price__lte=price_to)
                if not goods:
                    goods = Products.objects.filter(category__slug=category_slug).order_by('-is_new')
                elif order_by and order_by != 'default':
                    if order_by == 'price':
                        goods = goods.order_by('discount_price')
                        page_filter = 'По возрастанию цены'
                    elif order_by == '-price':
                        goods = goods.order_by('-discount_price')
                        page_filter = 'По убыванию цены'
                    else:
                        goods = goods.order_by(order_by)
                        page_filter = 'По величине скидки'
            elif price_from:
                goods = goods.filter(discount_price__gte=price_from)
                if not goods:
                    goods = Products.objects.filter(category__slug=category_slug).order_by('-is_new')
                elif order_by and order_by != 'default':
                    if order_by == 'price':
                        goods = goods.order_by('discount_price')
                        page_filter = 'По возрастанию цены'
                    elif order_by == '-price':
                        goods = goods.order_by('-discount_price')
                        page_filter = 'По убыванию цены'
                    else:
                        goods = goods.order_by(order_by)
                        page_filter = 'По величине скидки'
            elif price_to:
                goods = goods.filter(discount_price__lte=price_to)
                if not goods:
                    goods = Products.objects.filter(category__slug=category_slug).order_by('-is_new')
                if order_by and order_by != 'default':
                    if order_by == 'price':
                        goods = goods.order_by('discount_price')
                        page_filter = 'По возрастанию цены'
                    elif order_by == '-price':
                        goods = goods.order_by('-discount_price')
                        page_filter = 'По убыванию цены'
                    else:
                        goods = goods.order_by(order_by)
                        page_filter = 'По величине скидки'
        else:
            goods = Products.objects.filter(category__slug=category_slug).order_by('-is_new')
            page_title = goods[0].category.name
            title = goods[0].category.name
            if order_by and order_by != 'default':
                if order_by == 'price':
                        goods = Products.objects.filter(category__slug=category_slug).annotate(discount_price=(F("price")-F("price")*F("discount")/100))
                        goods = goods.order_by('discount_price')
                        page_filter = 'По возрастанию цены'
                elif order_by == '-price':
                        goods = Products.objects.filter(category__slug=category_slug).annotate(discount_price=(F("price")-F("price")*F("discount")/100))
                        goods = goods.order_by('-discount_price')
                        page_filter = 'По убыванию цены'
                else:
                        goods = Products.objects.filter(category__slug=category_slug).order_by(order_by)
                        page_filter = 'По величине скидки'

    paginator = Paginator(goods, 8)
    current_page = paginator.page(int(page))

    context = {
        'title': f'TAKO STORE - {title}',
        'goods': current_page,
        'slug_url': category_slug,
        'page_title': page_title,
        'page_filter': page_filter,
        'filter_price': filter_price,
    }

    return render(request, "goods/catalog_category.html", context)


def new(request):
    order_by = request.GET.get('order_by', None)
    price_from = request.GET.get('price_from', None)
    price_to = request.GET.get('price_to', None)
    page = request.GET.get('page', 1)

    if price_from or price_to:
        filter_price = True
    else:
        filter_price = False

    page_filter = 'По умолчанию'

    if price_from or price_to:
        goods = Products.objects.filter(is_new=True).annotate(discount_price=(F("price")-F("price")*F("discount")/100))
        page_title = 'Каталог'
        if price_to and price_from:
            goods = goods.filter(discount_price__gte=price_from).filter(discount_price__lte=price_to)
            if not goods:
                goods = Products.objects.filter(is_new=True)
            elif order_by and order_by != 'default':
                if order_by == 'price':
                    goods = goods.order_by('discount_price')
                    page_filter = 'По возрастанию цены'
                elif order_by == '-price':
                    goods = goods.order_by('-discount_price')
                    page_filter = 'По убыванию цены'
                else:
                    goods = goods.order_by(order_by)
                    page_filter = 'По величине скидки'
        elif price_from:
            goods = goods.filter(discount_price__gte=price_from)
            if not goods:
                goods = Products.objects.filter(is_new=True)
            elif order_by and order_by != 'default':
                if order_by == 'price':
                    goods = goods.order_by('discount_price')
                    page_filter = 'По возрастанию цены'
                elif order_by == '-price':
                    goods = goods.order_by('-discount_price')
                    page_filter = 'По убыванию цены'
                else:
                    goods = goods.order_by(order_by)
                    page_filter = 'По величине скидки'
        elif price_to:
            goods = goods.filter(discount_price__lte=price_to)
            if order_by and order_by != 'default':
                if order_by == 'price':
                    goods = goods.order_by('discount_price')
                    page_filter = 'По возрастанию цены'
                elif order_by == '-price':
                    goods = goods.order_by('-discount_price')
                    page_filter = 'По убыванию цены'
                else:
                    goods = goods.order_by(order_by)
                    page_filter = 'По величине скидки'
    else:
        goods = Products.objects.filter(is_new=True)
        if order_by and order_by != 'default':
            if order_by == 'price':
                goods = goods.annotate(discount_price=(F("price")-F("price")*F("discount")/100))
                goods = goods.order_by('discount_price')
                page_filter = 'По возрастанию цены'
            elif order_by == '-price':
                goods = goods.annotate(discount_price=(F("price")-F("price")*F("discount")/100))
                goods = goods.order_by('-discount_price')
                page_filter = 'По убыванию цены'
            else:
                goods = goods.order_by(order_by)
                page_filter = 'По величине скидки'

    paginator = Paginator(goods, 8)
    current_page = paginator.page(int(page))

    context = {
        'title': 'TAKO STORE - Новинки',
        'page_title': 'Новинки',
        'goods': current_page,
        'page_filter': page_filter,
        'filter_price': filter_price,
    }

    return render(request, "goods/new.html", context)


def sale(request):
    order_by = request.GET.get('order_by', None)
    price_from = request.GET.get('price_from', None)
    price_to = request.GET.get('price_to', None)

    if price_from or price_to:
        filter_price = True
    else:
        filter_price = False

    page_filter = 'По умолчанию'

    if price_from or price_to:
        goods = Products.objects.filter(discount__gt=0).annotate(discount_price=(F("price")-F("price")*F("discount")/100))
        page_title = 'Каталог'
        if price_to and price_from:
            goods = goods.filter(discount_price__gte=price_from).filter(discount_price__lte=price_to)
            if not goods:
                goods = Products.objects.filter(discount__gt=0)
            elif order_by and order_by != 'default':
                if order_by == 'price':
                    goods = goods.order_by('discount_price')
                    page_filter = 'По возрастанию цены'
                elif order_by == '-price':
                    goods = goods.order_by('-discount_price')
                    page_filter = 'По убыванию цены'
                else:
                    goods = goods.order_by(order_by)
                    page_filter = 'По величине скидки'
        elif price_from:
            goods = goods.filter(discount_price__gte=price_from)
            if not goods:
                goods = Products.objects.filter(discount__gt=0)
            elif order_by and order_by != 'default':
                if order_by == 'price':
                    goods = goods.order_by('discount_price')
                    page_filter = 'По возрастанию цены'
                elif order_by == '-price':
                    goods = goods.order_by('-discount_price')
                    page_filter = 'По убыванию цены'
                else:
                    goods = goods.order_by(order_by)
                    page_filter = 'По величине скидки'
        elif price_to:
            goods = goods.filter(discount_price__lte=price_to)
            if order_by and order_by != 'default':
                if order_by == 'price':
                    goods = goods.order_by('discount_price')
                    page_filter = 'По возрастанию цены'
                elif order_by == '-price':
                    goods = goods.order_by('-discount_price')
                    page_filter = 'По убыванию цены'
                else:
                    goods = goods.order_by(order_by)
                    page_filter = 'По величине скидки'
    else:
        goods = Products.objects.filter(discount__gt=0)
        if order_by and order_by != 'default':
            if order_by == 'price':
                goods = goods.annotate(discount_price=(F("price")-F("price")*F("discount")/100))
                goods = goods.order_by('discount_price')
                page_filter = 'По возрастанию цены'
            elif order_by == '-price':
                goods = goods.annotate(discount_price=(F("price")-F("price")*F("discount")/100))
                goods = goods.order_by('-discount_price')
                page_filter = 'По убыванию цены'
            else:
                goods = goods.order_by(order_by)
                page_filter = 'По величине скидки'

    page = request.GET.get('page', 1)
    paginator = Paginator(goods, 8)
    current_page = paginator.page(int(page))

    context = {
        'title': 'TAKO STORE - Sale',
        'page_title': 'Sale',
        'goods': current_page,
        'page_filter': page_filter,
        'filter_price': filter_price,
    }

    return render(request, "goods/sale.html", context)


def product(request, product_slug, size_slug=None):
    product = Products.objects.get(slug=product_slug)
    goods = Products.objects.exclude(id=product.id).order_by('?')[:4]

    if size_slug:
        size = Sizes.objects.get(slug=size_slug)
        product_variant = Variants.objects.get(product=product, size=size)
        if request.user.is_authenticated:
            user_cart = Cart.objects.filter(user=request.user, product_variant=product_variant)
            if user_cart:
                product_in_cart = True
        else:
            user_cart = Cart.objects.filter(session_key=request.session.session_key, product_variant=product_variant)
            if user_cart:
                product_in_cart = True
        product_variants = product.variants.all()
        title = f"TAKO STORE - {product.name}, {product.article}"
        images = Gallery.objects.filter(product__slug=product_slug)

        return render(request, "goods/product_size.html", locals())

    product_variants = product.variants.all()

    title = f"TAKO STORE - {product.name}, {product.article}"

    images = Gallery.objects.filter(product__slug=product_slug)

    return render(request, "goods/product.html", locals())


def brands(request):
    brands = Brands.objects.all()

    title = f"TAKO STORE - Все бренды"
    page_title = 'Все бренды'

    return render(request, 'goods/all_brands.html', locals())


def brands_catalog(request, brand_slug):
    order_by = request.GET.get('order_by', None)
    price_from = request.GET.get('price_from', None)
    price_to = request.GET.get('price_to', None)

    if price_from or price_to:
        filter_price = True
    else:
        filter_price = False

    page_filter = 'По умолчанию'

    if price_from or price_to:
        goods = Products.objects.filter(brand__slug=brand_slug).annotate(discount_price=(F("price")-F("price")*F("discount")/100))
        page_title = 'Каталог'
        if price_to and price_from:
            goods = goods.filter(discount_price__gte=price_from).filter(discount_price__lte=price_to)
            if not goods:
                goods = Products.objects.filter(brand__slug=brand_slug)
            elif order_by and order_by != 'default':
                if order_by == 'price':
                    goods = goods.order_by('discount_price')
                    page_filter = 'По возрастанию цены'
                elif order_by == '-price':
                    goods = goods.order_by('-discount_price')
                    page_filter = 'По убыванию цены'
                else:
                    goods = goods.order_by(order_by)
                    page_filter = 'По величине скидки'
        elif price_from:
            goods = goods.filter(discount_price__gte=price_from)
            if not goods:
                goods = Products.objects.filter(brand__slug=brand_slug)
            elif order_by and order_by != 'default':
                if order_by == 'price':
                    goods = goods.order_by('discount_price')
                    page_filter = 'По возрастанию цены'
                elif order_by == '-price':
                    goods = goods.order_by('-discount_price')
                    page_filter = 'По убыванию цены'
                else:
                    goods = goods.order_by(order_by)
                    page_filter = 'По величине скидки'
        elif price_to:
            goods = goods.filter(discount_price__lte=price_to)
            if order_by and order_by != 'default':
                if order_by == 'price':
                    goods = goods.order_by('discount_price')
                    page_filter = 'По возрастанию цены'
                elif order_by == '-price':
                    goods = goods.order_by('-discount_price')
                    page_filter = 'По убыванию цены'
                else:
                    goods = goods.order_by(order_by)
                    page_filter = 'По величине скидки'
    else:
        goods = Products.objects.filter(brand__slug=brand_slug)
        if order_by and order_by != 'default':
            goods = goods.annotate(discount_price=(F("price")-F("price")*F("discount")/100))
            if order_by == 'price':
                goods = goods.order_by('discount_price')
                page_filter = 'По возрастанию цены'
            elif order_by == '-price':
                goods = goods.order_by('-discount_price')
                page_filter = 'По убыванию цены'
            else:
                goods = goods.order_by(order_by)
                page_filter = 'По величине скидки'

    slug_url = brand_slug
    brand_name =  goods[0].brand.name
    title = f"TAKO STORE - {brand_name}"
    page_title = f'{brand_name}'

    return render(request, 'goods/brand_catalog.html', locals())
