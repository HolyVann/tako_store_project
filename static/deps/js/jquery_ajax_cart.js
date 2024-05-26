// Когда html документ готов (прорисован)
$(document).ready(function () {
    // берем в переменную элемент разметки с id jq-notification для оповещений от ajax
    var successMessage = $("#jq-notification");

    // Ловим собыитие клика по кнопке добавить в корзину
    $(document).on("click", ".add-to-cart-ajax", function (e) {
        // Блокируем его базовое действие
        e.preventDefault();

        // Берем элемент счетчика в значке корзины и берем оттуда значение
        var goodsInCartCount = $("#goods-in-cart-counter");
        var cartCount = parseInt(goodsInCartCount.text() || 0);

        // Получаем id товара из атрибута data-product-id
        var product_id = $(this).data("product-id");

        // Из атрибута href берем ссылку на контроллер django
        var add_to_cart_url = $(this).attr("href");

        // делаем post запрос через ajax не перезагружая страницу
        $.ajax({
            type: "POST",
            url: add_to_cart_url,
            data: {
                product_id: product_id,
                csrfmiddlewaretoken: $("[name=csrfmiddlewaretoken]").val(),
            },
            success: function (data) {
                // Сообщение
                successMessage.html(data.message);
                successMessage.fadeIn(400);
                // // Через 7сек убираем сообщение
                setTimeout(function () {
                    successMessage.fadeOut(400);
                }, 5000);

                // Увеличиваем количество товаров в корзине (отрисовка в шаблоне)
                if (data.exists) {
                    cartCount++;
                    goodsInCartCount.text(cartCount);
                }

                if (cartCount>0) {
                    $("#goods-in-cart-counter").show();
                }

                // Меняем содержимое корзины на ответ от django (новый отрисованный фрагмент разметки корзины)
                var cartItemsContainer = $("#cart-items-container");
                cartItemsContainer.html(data.cart_items_html);

            },

            error: function (data) {
                console.log("Ошибка при добавлении товара в корзину");
            },
        });
    });


    // Ловим собыитие клика по кнопке удалить товар из корзины
    $(document).on("click", ".remove-from-cart", function (e) {
        // Блокируем его базовое действие
        e.preventDefault();

        // Берем элемент счетчика в значке корзины и берем оттуда значение
        var goodsInCartCount = $("#goods-in-cart-counter");
        var cartCount = parseInt(goodsInCartCount.text() || 0);

        // Получаем id корзины из атрибута data-cart-id
        var cart_id = $(this).data("cart-id");
        // Из атрибута href берем ссылку на контроллер django
        var remove_from_cart = $(this).attr("href");

        // делаем post запрос через ajax не перезагружая страницу
        $.ajax({

            type: "POST",
            url: remove_from_cart,
            data: {
                cart_id: cart_id,
                csrfmiddlewaretoken: $("[name=csrfmiddlewaretoken]").val(),
            },
            success: function (data) {
                // Сообщение
                // successMessage.html(data.message);
                // successMessage.fadeIn(400);
                // // Через 7сек убираем сообщение
                // setTimeout(function () {
                //     successMessage.fadeOut(400);
                // }, 5000);

                // Уменьшаем количество товаров в корзине (отрисовка)
                cartCount -= data.quantity_deleted;
                goodsInCartCount.text(cartCount);

                if (cartCount==0) {
                    $("#goods-in-cart-counter").hide();
                }

                // Меняем содержимое корзины на ответ от django (новый отрисованный фрагмент разметки корзины)
                var cartItemsContainer = $("#cart-items-container");
                cartItemsContainer.html(data.cart_items_html);

            },

            error: function (data) {
                console.log("Ошибка при добавлении товара в корзину");
            },
        });
    });


    // Теперь + - количества товара
    // Обработчик события для уменьшения значения
    $(document).on("click", ".decrease-quantity", function () {
        // Берем ссылку на контроллер django из атрибута data-cart-change-url
        var url = $(this).data("cart-change-url");
        // Берем id корзины из атрибута data-cart-id
        var cartID = $(this).data("cart-id");
        // Ищем ближайшеий input с количеством
        var $input = $(this).closest('.cart-product__quantity').find('.product-quantity');
        // Берем значение количества товара
        var currentValue = parseInt($input.val());
        // Если количества больше одного, то только тогда делаем -1
        if (currentValue > 1) {
            $input.val(currentValue - 1);
            // Запускаем функцию определенную ниже
            // с аргументами (id карты, новое количество, количество уменьшилось или прибавилось, url)
            updateCart(cartID, currentValue - 1, -1, url);
        }
    });

    // Обработчик события для увеличения значения
    $(document).on("click", ".increase-quantity", function () {
        // Берем ссылку на контроллер django из атрибута data-cart-change-url
        var url = $(this).data("cart-change-url");
        // Берем id корзины из атрибута data-cart-id
        var cartID = $(this).data("cart-id");
        // Ищем ближайшеий input с количеством
        var $input = $(this).closest('.cart-product__quantity').find('.product-quantity');
        // Берем значение количества товара
        var currentValue = parseInt($input.val());

        $input.val(currentValue + 1);

        // Запускаем функцию определенную ниже
        // с аргументами (id карты, новое количество, количество уменьшилось или прибавилось, url)
        updateCart(cartID, currentValue + 1, 1, url);
    });

    function updateCart(cartID, quantity, change, url) {
        $.ajax({
            type: "POST",
            url: url,
            data: {
                cart_id: cartID,
                quantity: quantity,
                csrfmiddlewaretoken: $("[name=csrfmiddlewaretoken]").val(),
            },

            success: function (data) {
                //  // Сообщение
                // successMessage.html(data.message);
                // successMessage.fadeIn(400);
                //  // Через 7сек убираем сообщение
                // setTimeout(function () {
                //     successMessage.fadeOut(400);
                // }, 5000);

                // Изменяем количество товаров в корзине
                var goodsInCartCount = $("#goods-in-cart-counter");
                var cartCount = parseInt(goodsInCartCount.text() || 0);
                cartCount += change;
                goodsInCartCount.text(cartCount);

                // Меняем содержимое корзины
                var cartItemsContainer = $("#cart-items-container");
                cartItemsContainer.html(data.cart_items_html);


            },
            error: function (data) {
                console.log("Ошибка при добавлении товара в корзину");
            },
        });
    }


    // Берем из разметки элемент по id - оповещения от django
    var notification = $('#notification');
    // И через 7 сек. убираем
    if (notification.length > 0) {
        setTimeout(function () {
            notification.alert('close');
        }, 5000);
    }


    // Обработчик события радиокнопки выбора способа доставки
    $("input[name='requires_delivery']").change(function () {
        var selectedValue = $(this).val();
        // Скрываем или отображаем input ввода адреса доставки
        if (selectedValue === "1") {
            $("#id_delivery_address").show();
        } else {
            $("#id_delivery_address").hide();
        }
    });


    var goodsInCart = $("#goods-in-cart-counter");
    var count = parseInt(goodsInCart.text() || 0);
    if (count > 0) {
        $("#goods-in-cart-counter").show();
    }
    else {
        $("#goods-in-cart-counter").hide();
    }


    $('body').on('click', '#password-show', function(){
        if ($('#id_password').attr('type') == 'password'){
            $(this).addClass('hide-password');
            $('#password-hide').removeClass('hide-password');
            $('#id_password').attr('type', 'text');
        }
        return false;
    });

    $('body').on('click', '#password-hide', function(){
        if ($('#id_password').attr('type') == 'text'){
            $(this).addClass('hide-password');
            $('#password-show').removeClass('hide-password');
            $('#id_password').attr('type', 'password');
        }
        return false;
    });


    $('body').on('click', '#password-show-1', function(){
        if ($('#id_password1').attr('type') == 'password'){
            $(this).addClass('hide-password');
            $('#password-hide-1').removeClass('hide-password');
            $('#id_password1').attr('type', 'text');
        }
        return false;
    });

    $('body').on('click', '#password-hide-1', function(){
        if ($('#id_password1').attr('type') == 'text'){
            $(this).addClass('hide-password');
            $('#password-show-1').removeClass('hide-password');
            $('#id_password1').attr('type', 'password');
        }
        return false;
    });

});
