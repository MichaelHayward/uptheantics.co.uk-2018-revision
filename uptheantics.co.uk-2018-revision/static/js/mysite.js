function navEvents() {
  // Get all "navbar-burger" elements
  var $navbarBurgers = Array.prototype.slice.call(document.querySelectorAll('.navbar-burger'), 0);

  // Check if there are any navbar burgers
  if ($navbarBurgers.length > 0) {

    // Add a click event on each of them
    $navbarBurgers.forEach(function ($el) {
      $el.addEventListener('click', function () {
        // Get the target from the "data-target" attribute
        var target = $el.dataset.target;
        var $target = document.getElementById(target);

        // Toggle the class on both the "navbar-burger" and the "navbar-menu"
        $el.classList.toggle('is-active');
        $target.classList.toggle('is-active');
      });
    });
  }
}

function emailObfuscation() {
  // Get all "email-hide" elements
  var $emailHide = Array.prototype.slice.call(document.querySelectorAll('.email-hide'), 0);

  // Check if there are "email-hide" elements
  if ($emailHide.length > 0) {

    // Add a click event on each of them
    $emailHide.forEach(function ($el) {
        let user = "uptheanticsgroup";
        let domain = "gmail.com";
        let email = `${user}@${domain}`;

        // Change their text and href attr
        $el.innerText = email;
        $el.setAttribute("href", `mailto:${email}`)
    });
  }
}

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
        e.target.classList.toggle("accordion-flip");
        // variables to be readable
        const bios = document.querySelector(".bio-container").querySelectorAll(".bio-content")
        let thisBio = e.target.parentElement.parentElement
        // Check to see if clicked bio is already active. If not, make it
        if(!thisBio.classList.contains("bio-content-active")){
          thisBio.classList.add("bio-content-active");
          bios.forEach(function($bc){
            // Add a class to fade out and de-activate (via css) the siblings
            if(!$bc.classList.contains("bio-content-active")){
              $bc.classList.add("bio-content-faded")
            }
          });
        } else {
          // If the clicked bio is already active, undo all prev' classes
          bios.forEach(function (bio) {
            bio.classList.remove("bio-content-faded", "bio-content-active");
          });
        }
      });
    });
  }
}

document.addEventListener('DOMContentLoaded', function () {
  navEvents();
  emailObfuscation();
  accordionEvents();
});
