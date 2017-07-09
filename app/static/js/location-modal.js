/**
 * Variables
 */

// Small screen breakpoint
var smallScreenSize = 576;

// Get elements
var addLocationBtn = document.getElementById('add-location');
var locationModal = document.getElementById('location-modal');
var pageOverlay = document.getElementById('page-overlay');
var saveBtn = document.getElementById('save-btn');
var errorMsg = document.getElementById('error-msg');

// Delay before hiding the modal (in ms)
var animationDuration = 400;

/**
* Listeners
*/

// Add click listener to 'add-location' button
addLocationBtn.addEventListener('click', function() {
  if (window.innerWidth > smallScreenSize) showModal();
  else showModalSmall();
});

// Add click listener to page overlay
pageOverlay.addEventListener('click', function() {
  if (window.innerWidth > smallScreenSize) hideModal();
  else hideModalSmall();
});

// Add click listener to save btn
saveBtn.addEventListener('click', function() {

  // Dont hide modal if there are errors
  if (errorMsg.classList.contains('hidden')) {
      if (window.innerWidth > smallScreenSize) hideModal();
      else hideModalSmall();
  }

});

/**
* Modal functions
*/

// Show the 'add-location' modal
function showModal() {

  pageOverlay.classList.toggle('hidden');

  locationModal.className = '';
  locationModal.classList.add('showing');
  locationModal.classList.add('modal-in');

}

// Show the 'add-location' modal on small screens
function showModalSmall() {

  pageOverlay.classList.toggle('hidden');

  locationModal.className = '';
  locationModal.classList.add('showing');
  locationModal.classList.add('modal-in');

}

// Hide modal and overlay
function hideModal() {

  if (locationModal.classList.contains('showing')) {

      pageOverlay.classList.toggle('hidden');

      locationModal.className = '';
      locationModal.classList.add('modal-out');

      // Hide modal once animation is done
      setTimeout(addHidden, animationDuration);
      
  }

}

// Hide modal and overlay on small screens
function hideModalSmall() {

  if (locationModal.classList.contains('showing')) {

      pageOverlay.classList.toggle('hidden');

      locationModal.className = '';
      locationModal.classList.add('modal-out');
      
      // Hide modal once animation is done
      setTimeout(addHidden, animationDuration);

  }

}

function addHidden() {
  locationModal.classList.add('hidden');
}