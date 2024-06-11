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
