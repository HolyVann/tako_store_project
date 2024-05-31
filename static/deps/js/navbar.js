window.onscroll = function() {scrollFunction()};

function scrollFunction() {
  if (document.body.scrollTop > 20 || document.documentElement.scrollTop > 20) {
    document.getElementById("navbar").style.boxShadow = "0px 0px 2px #A8A8AE";
    document.getElementById("navModalBtn").style.visibility = "visible";
    document.getElementById("nav-container__down").style.top = "-80px";
  } else {
    document.getElementById("navbar").style.boxShadow = "0px 0px 0px";
    document.getElementById("navModalBtn").style.visibility = "hidden";
    document.getElementById("nav-container__down").style.top = "0";
  }
}
