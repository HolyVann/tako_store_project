// Когда html документ готов (прорисован)
$(document).ready(function () {
  // берем в переменную элемент разметки с id jq-notification для оповещений от ajax
  var successMessage = $("#jq-notification");

  // Ловим собыитие клика по кнопке добавить в корзину
  $(document).on("click", ".add-to-favorites-ajax", function (e) {
    // Блокируем его базовое действие
    e.preventDefault();

    // Берем элемент счетчика в значке корзины и берем оттуда значение
    var goodsInFavoritesCount = $("#goods-in-favorites-counter");
    var favoritesCount = parseInt(goodsInFavoritesCount.text() || 0);

    // Получаем id товара из атрибута data-product-id
    var product_id = $(this).data("product-id");

    // Из атрибута href берем ссылку на контроллер django
    var add_to_favorites_url = $(this).attr("href");

    // делаем post запрос через ajax не перезагружая страницу
    $.ajax({
      type: "POST",
      url: add_to_favorites_url,
      data: {
        product_id: product_id,
        csrfmiddlewaretoken: $("[name=csrfmiddlewaretoken]").val(),
      },
      success: function (data) {
        // Сообщение
        successMessage.css('z-index', '6');
        successMessage.html(data.message);
        successMessage.fadeIn(400);
        // Через 7сек убираем сообщение
        setTimeout(function () {
          successMessage.fadeOut(400);
        }, 5000);

        // Увеличиваем количество товаров в корзине (отрисовка в шаблоне)
        if (data.exists) {
          favoritesCount++;
          goodsInFavoritesCount.text(favoritesCount);
        }

        if (favoritesCount>0) {
          $("#goods-in-favorites-counter").show();
        }

        // Меняем содержимое корзины на ответ от django (новый отрисованный фрагмент разметки корзины)
        var favoritesItemsContainer = $("#favorites-items-container");
        favoritesItemsContainer.html(data.favorites_items_html);
      },

      error: function (data) {
        console.log("Ошибка при добавлении товара в корзину");
      },
    });
  });


  // Ловим собыитие клика по кнопке удалить товар из корзины
  $(document).on("click", ".remove-from-favorites", function (e) {
    // Блокируем его базовое действие
    e.preventDefault();

    // Берем элемент счетчика в значке корзины и берем оттуда значение
    var goodsInFavoritesCount = $("#goods-in-favorites-counter");
    var favoritesCount = parseInt(goodsInFavoritesCount.text() || 0);

    // Получаем id корзины из атрибута data-cart-id
    var favorite_id = $(this).data("favorite-id");
    // Из атрибута href берем ссылку на контроллер django
    var remove_from_favorites = $(this).attr("href");

    // делаем post запрос через ajax не перезагружая страницу
    $.ajax({

      type: "POST",
      url: remove_from_favorites,
      data: {
        favorite_id: favorite_id,
        csrfmiddlewaretoken: $("[name=csrfmiddlewaretoken]").val(),
      },
      success: function (data) {
        // Сообщение
        // successMessage.html(data.message);
        // successMessage.fadeIn(400);
        // // Через 7сек убираем сообщение
        // setTimeout(function () {
        //   successMessage.fadeOut(400);
        // }, 5000);

        // Уменьшаем количество товаров в корзине (отрисовка)
        favoritesCount -= data.quantity_deleted;
        goodsInFavoritesCount.text(favoritesCount);

        if (favoritesCount==0) {
          $("#goods-in-favorites-counter").hide();
        }

        // Меняем содержимое корзины на ответ от django (новый отрисованный фрагмент разметки корзины)
        var favoritesItemsContainer = $("#favorites-items-container");
        favoritesItemsContainer.html(data.favorites_items_html);

      },

      error: function (data) {
        console.log("Ошибка при добавлении товара в корзину");
      },
    });
  });


  var goodsInFavorites = $("#goods-in-favorites-counter");
    var count = parseInt(goodsInFavorites.text() || 0);
    if (count > 0) {
        $("#goods-in-favorites-counter").show();
    }
    else {
        $("#goods-in-favorites-counter").hide();
    }
});
