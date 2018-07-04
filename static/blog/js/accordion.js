// const accordionButton = document.getElementsByClassName("accordion-button");
//
// for(i = 0; i < accordionButton.length; i++){
//   accordionButton[i].addEventListener("click", toggleBio)
// }
//
//
//
// function toggleBio(e) {
//   showAccordion(e);
//   activateBio(e);
// }
//
//
// // Toggles a class on the hidden text paragraph and changes the button text
// function showAccordion(e) {
//   e.target.parentElement.parentElement.querySelector(".accordion-content").classList.toggle("accordion-hidden");
//   if(e.target.innerHTML === "More") {
//     e.target.innerHTML = "Less";
//   } else {
//     e.target.innerHTML = "More";
//   }
// }
//
// // Adds a class to the parent bio div that keeps everything opaque even while not hovering
// function activateBio(e) {
//   e.target.parentElement.parentElement.classList.toggle("bio-content-active");
// }




//////////////////////////////////////////////////////////

function accordionEvents(){
  // Get all "accordion-button" elements
  var $accordionButtons = Array.prototype.slice.call(document.querySelectorAll('.accordion-button'), 0);

  // Check if there are any accordion buttons
  if ($accordionButtons.length > 0) {

    // Add a click event on each accordion button
    $accordionButtons.forEach(function ($ab) {
      $ab.addEventListener('click', function (e) {
        // Toggles a class on the hidden text paragraph and changes the button text
        e.target.parentElement.parentElement.querySelector(".accordion-content").classList.toggle("accordion-hidden");
        if(e.target.innerHTML === "More") {
          e.target.innerHTML = "Less";
        } else {
          e.target.innerHTML = "More";
        }
        // Adds a class to the parent bio div that keeps everything opaque even while not hovering
        e.target.parentElement.parentElement.classList.toggle("bio-content-active");
      });
    });
  }
}
