from django.http import JsonResponse
from django.shortcuts import redirect
from carts.models import Cart
from goods.models import Products, Variants
from django.template.loader import render_to_string
from carts.utils import get_user_carts


def cart_add_modal(request):
    product_id = request.POST.get("product_id")

    # product = Products.objects.get(id=product_id)
    product_variant = Variants.objects.get(id=product_id)

    exists = False

    if request.user.is_authenticated:
        carts = Cart.objects.filter(user=request.user, product_variant=product_variant)

        if not carts.exists():
            Cart.objects.create(user=request.user, product_variant=product_variant, quantity=1)

            exists = True

    else:
        carts = Cart.objects.filter(session_key=request.session.session_key,product_variant=product_variant)

        if not carts.exists():
            Cart.objects.create(session_key=request.session.session_key, product_variant=product_variant, quantity=1)

            exists = True

    user_cart = get_user_carts(request)

    if exists:
        message = f'''<img src="{ product_variant.product.image.url }"/>
        <div class="jq-container"> <div>Добавлено в корзину</div> <div>{product_variant.product} { product_variant.size.name }</div></div>'''
    else:
        message = f'''<img src="{ product_variant.product.image.url }"/>
        <div class="jq-container"> <div>В корзине</div> <div>{product_variant.product} { product_variant.size.name }</div> </div>'''

    if user_cart.exists():
        cart_items_html = render_to_string(
            "carts/includes/cart_product_modal.html",
            {"carts": user_cart},
            request=request,
        )

    response_data = {
        'product': 'product132',
        "message": message,
        "cart_items_html": cart_items_html,
        'exists': exists,
    }

    return JsonResponse(response_data)


def cart_change_modal(request):
    cart_id = request.POST.get("cart_id")
    quantity = request.POST.get("quantity")

    cart = Cart.objects.get(id=cart_id)

    cart.quantity = quantity
    cart.save()
    updated_quantity = cart.quantity


    cart = get_user_carts(request)

    cart_items_html = render_to_string(
        "carts/includes/cart_product_modal.html", {"carts": cart}, request=request
    )

    response_data = {
        "message": "Количество изменено",
        "cart_items_html": cart_items_html,
        "quantity": updated_quantity,
    }

    return JsonResponse(response_data)


def cart_remove_modal(request):
    cart_id = request.POST.get("cart_id")

    cart = Cart.objects.get(id=cart_id)
    quantity = cart.quantity
    cart.delete()

    user_cart = get_user_carts(request)

    if user_cart.exists():
        cart_items_html = render_to_string(
            "carts/includes/cart_product_modal.html",
            {"carts": user_cart},
            request=request,
        )
    else:
        cart_items_html = render_to_string("carts/includes/modal_cart_empty.html")

    response_data = {
        "cart_items_html": cart_items_html,
        "quantity_deleted": quantity,
    }

    return JsonResponse(response_data)


def cart_change(request):
    cart_id = request.POST.get("cart_id")
    quantity = request.POST.get("quantity")

    cart = Cart.objects.get(id=cart_id)

    cart.quantity = quantity
    cart.save()
    updated_quantity = cart.quantity

    cart = get_user_carts(request)

    cart_items_html = render_to_string(
        "carts/includes/cart_product.html", {"carts": cart}, request=request
    )

    response_data = {
        "message": "Количество изменено",
        "cart_items_html": cart_items_html,
        "quantity": updated_quantity,
    }

    return JsonResponse(response_data)


def cart_remove(request):
    cart_id = request.POST.get("cart_id")

    cart = Cart.objects.get(id=cart_id)
    quantity = cart.quantity
    cart.delete()

    user_cart = get_user_carts(request)

    if user_cart.exists():
        cart_items_html = render_to_string(
            "carts/includes/cart_product.html",
            {"carts": user_cart},
            request=request,
        )
    else:
        cart_items_html = render_to_string("carts/includes/modal_cart_empty.html")

    response_data = {
        "message": "Товар удален из корзины",
        "cart_items_html": cart_items_html,
        "quantity_deleted": quantity,
    }

    return JsonResponse(response_data)
