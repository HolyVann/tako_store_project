window.onscroll = function() {scrollFunction()};

function scrollFunction() {
  if (document.body.scrollTop > 20 || document.documentElement.scrollTop > 20) {
    document.getElementById("main-navbar").style.backgroundColor = "#fff";
    document.getElementById("navModalBtn").style.color = "#000";
    document.getElementById("main-navbar").style.boxShadow = "none";
    document.getElementById("myBtn").style.color = "#000";
    document.getElementById("favoritesBtn").style.color = "#000";
    document.getElementById("cartBtn").style.color = "#000";
    document.getElementById("user-icon").style.color = "#000";
    document.getElementById("goods-in-favorites-counter").style.border = "solid 1px #000";
    document.getElementById("goods-in-cart-counter").style.border = "solid 1px #000";
  } else {
    document.getElementById("main-navbar").style.backgroundColor = "transparent";
    document.getElementById("navModalBtn").style.color = "#fff";
    document.getElementById("main-navbar").style.boxShadow = "rgb(0, 0, 0) 0px 187px 59px -200px inset";
    document.getElementById("myBtn").style.color = "#fff";
    document.getElementById("favoritesBtn").style.color = "#fff";
    document.getElementById("cartBtn").style.color = "#fff";
    document.getElementById("user-icon").style.color = "#fff";
    document.getElementById("goods-in-favorites-counter").style.border = "none";
    document.getElementById("goods-in-cart-counter").style.border = "none";
  }
}
