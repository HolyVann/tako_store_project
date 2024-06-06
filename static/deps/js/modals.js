// Get the modal
var favoritesModal = document.getElementById("favoritesModal");

// Get the button that opens the modal
var favoritesBtn = document.getElementById("favoritesBtn");

// Get the <span> element that closes the modal
var span = document.getElementsByClassName("modal__favorites-close")[0];

// When the user clicks on the button, open the modal
favoritesBtn.onclick = function() {
  favoritesModal.style.display = "flex";
  document.body.style.overflow = "hidden";
}

// When the user clicks on <span> (x), close the modal
span.onclick = function() {
  favoritesModal.style.display = "none";
  document.body.style.overflow = "";
}

// When the user clicks anywhere outside of the modal, close it
window.onclick = function(event) {
  if (event.target == favoritesModal) {
    favoritesModal.style.display = "none";
  }
}



// Get the modal
var modal = document.getElementById("myModal");

// Get the button that opens the modal
var btn = document.getElementById("myBtn");

// Get the <span> element that closes the modal
var span = document.getElementsByClassName("close")[0];

// When the user clicks on the button, open the modal
btn.onclick = function() {
  modal.style.display = "block";
}

// When the user clicks on <span> (x), close the modal
span.onclick = function() {
  modal.style.display = "none";
}

// When the user clicks anywhere outside of the modal, close it
window.onclick = function(event) {
  if (event.target == modal) {
    modal.style.display = "none";
  }
}

// Get the modal
var cartModal = document.getElementById("cartModal");

// Get the button that opens the modal
var cartBtn = document.getElementById("cartBtn");

// Get the <span> element that closes the modal
var span = document.getElementsByClassName("modal__cart-close")[0];

// When the user clicks on the button, open the modal
cartBtn.onclick = function() {
  cartModal.style.display = "flex";
  document.body.style.overflow = "hidden";
}

// When the user clicks on <span> (x), close the modal
span.onclick = function() {
  cartModal.style.display = "none";
  document.body.style.overflow = "";
}

// When the user clicks anywhere outside of the modal, close it
window.onclick = function(event) {
  if (event.target == cartModal) {
    cartModal.style.display = "none";
  }
}
