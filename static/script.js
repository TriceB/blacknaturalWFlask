/* Set the width of the sidebar to 250px and the left margin of the page content to 250px */
function openNav() {
  document.getElementById("mySidebar").style.width = "250px";
  document.getElementById("main").style.marginLeft = "250px";
  document.getElementById("menubtn").style.display = 'none';
}

/* Set the width of the sidebar to 0 and the left margin of the page content to 0 */
function closeNav() {
  document.getElementById("mySidebar").style.width = "0";
  document.getElementById("main").style.marginLeft = "0";
  document.getElementById("menubtn").style.display = 'initial';
}

// close menu when user clicks outside anywhere outside of the menu

// window.addEventListener ("mouseup", function(event){
//   var menu = document.getElementById("mySidebar");
//   if (event.target != menu &&  event.target.parentNode != menu){
//       menu.style.display = 'none';
//   }
    

// })