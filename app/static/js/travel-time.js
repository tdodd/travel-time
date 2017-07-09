/**
 * Variables
 */

// Max number of checkboxes that can be checked
var maxLocations = 2;

// Current number of checkboxes that have been clicked
var currentNumClicked = 0;

/**
 * Listeners
 */

// Get checkboxes
var checkboxes = document.getElementsByClassName('location-box');
for (var i = 0; i < checkboxes.length; i++) {
   checkboxes[i].addEventListener('click', checkNumClicked(i));
}

// Check the current number of active checkboxes
function checkNumClicked(index) {

   if (currentNumClicked <= maxLocations && checkboxes[index].checked == false) {
      checkboxes[index].checked = true;
      currentNumClicked++;
   }
   
   else if (currentNumClicked <= maxLocations && checkboxes[index].checked == true) {
      checkboxes[index].checked = true;
      currentNumClicked--;
   }
   
   else {
      checkboxes[index].checked = false;
   }

}