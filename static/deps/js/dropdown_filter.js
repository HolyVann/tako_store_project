/* When the user clicks on the button,
toggle between hiding and showing the dropdown content */
function myFunction() {
  document.getElementById("myDropdown").classList.toggle("show");
  document.getElementById('filterSvg').classList.toggle('filter-transform');
}


// Close the dropdown menu if the user clicks outside of it
window.onclick = function(event) {

  if (!event.target.matches('.dropbtn')) {
    var dropdowns = document.getElementsByClassName("dropdown-filter__content");
    var i;
    for (i = 0; i < dropdowns.length; i++) {
      var openDropdown = dropdowns[i];
      if (openDropdown.classList.contains('show')) {
        openDropdown.classList.remove('show');
      }
    }
  }
}


function priceFilter() {
  document.getElementById("priceFilter").classList.toggle("show");
  document.getElementById('filterPriceSvg').classList.toggle('filter-transform');
}


function openDescription() {
  document.getElementById("description").classList.toggle("show");
  document.getElementById('descriptionSvg').classList.toggle('filter-transform');
}
