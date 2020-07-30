/* Set the width of the sidebar to 250px and the left margin of the page content to 250px */
function openNav() {
 // document.getElementById("mySidebar").style.width = "250px";
 // document.getElementById("main").style.marginLeft = "250px";
  // document.getElementById("menubtn").style.display = 'none';
  //document.getElementsByTagName("body")[0] - this will only add the word "class" instead of "class="menu-open"" as expected. it works when using other elements but not the body
  document.getElementsByTagName("body")[0].classList.add("menu-open");

}

// $(document).ready(function(){
//   $("openNav").click(function(){
//     $("body").addClass("menu-open");
    
//   });
// });

/* Set the width of the sidebar to 0 and the left margin of the page content to 0 */
function closeNav() {

  /*
  document.getElementById("mySidebar").style.width = "0";
  document.getElementById("main").style.marginLeft = "0";
  
  document.getElementById("menubtn").style.display = 'initial';
*/

  document.getElementsByTagName("body")[0].classList.remove("menu-open");
}
//keep working on fixing this - 7/20
// window.addEventListener('click', function(evt){

//   //closeNav();

//   console.log('Got clicked', evt);

//   var tgt = evt.target;
//   if (tgt.id !== main && evt.target.parentNode !== "mySidebar"){
//     closeNav();
//   }
// });
// close menu when user clicks outside anywhere outside of the menu

// window.addEventListener ("click", function(event){
//   var menu = document.getElementById("mySidebar");
//   if (event.target != menu &&  event.target.parentNode != menu){
//       closeNav();
//   }
  
// })

/* Note from Coach Mike regarding why the above code did not work-
 -i’ve done some debugging and it looks like the closeNav function is fired immediately after the openNav function. the fix will be do something like this…notice the new logic for the menuBtn
 -to debug it i put a few console log statements in the code. one within the openNav function, one within the closeNav function, and one within the if block. this way i could know which function fired when. after doing that i figured out that there needed to be another check for the menu button itself when it came to deciding whether or not to close the nav */

window.addEventListener("click", function(event) {
  var menu = document.getElementById("mySidebar");
  var menuBtn = document.getElementById("menubtn");
  if (event.target != menu && 
      event.target.parentNode != menu && 
      event.target != menuBtn) {
    closeNav();
  }
});

// accordian js so that menu expands when "+" is clicked and collapsed when "-" is clicked
/* Loop through all dropdown buttons to toggle between hiding and showing its dropdown content 
- This allows the user to have multiple dropdowns without any conflict */
var dropdown = document.getElementsByClassName("dropdown-btn");
var i;

for (i = 0; i < dropdown.length; i++) {
  dropdown[i].addEventListener("click", function() {
  this.classList.toggle("active");
  var dropdownContent = this.nextElementSibling;
  if (dropdownContent.style.display === "block") {
  dropdownContent.style.display = "none";
  } else {
  dropdownContent.style.display = "block";
  }
  });
}