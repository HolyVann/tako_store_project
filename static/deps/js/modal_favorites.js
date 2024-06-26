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

document.addEventListener("click", event => {
    if (event.target.matches(".favoritesMessage")) {
        favoritesModal.style.display = "flex";
        document.body.style.overflow = "hidden";
    }
}, false);

