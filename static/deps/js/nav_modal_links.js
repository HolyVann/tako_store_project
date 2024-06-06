// Get the modal
var navModal = document.getElementById("navModal");

// Get the button that opens the modal
var navBtn = document.getElementById("navModalBtn");

// Get the <span> element that closes the modal
var span = document.getElementsByClassName("close-nav")[0];

// When the user clicks on the button, open the modal
navBtn.onclick = function() {
  navModal.style.display = "block";

  document.body.style.overflow = "hidden";
}

// When the user clicks on <span> (x), close the modal
span.onclick = function() {
  navModal.style.display = "none";

  document.body.style.overflow = "";
}

// When the user clicks anywhere outside of the modal, close it
window.onclick = function(event) {
  if (event.target == navModal) {
    navModal.style.display = "none";
  }
}
