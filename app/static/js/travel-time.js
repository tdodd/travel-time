// Google Maps API constats
var GOOGLE_MAPS_API_ENDPOINT = 'https://maps.googleapis.com/maps/api/distancematrix/json?units=metric';
var API_KEY = 'AIzaSyBDw6Ac70Y8ctrz1nkx1_y8IaF8U05SbQc';

// Max number of checkboxes that can be checked
var maxNumActive = 2;

// Current number of checkboxes that have been clicked
var currentNumActive = 0;

// Checkboxes
var checkboxes = document.getElementsByClassName('location-box');

// Click listeners
for (var i = 0; i < checkboxes.length; i++) {
   checkboxes[i].addEventListener('click', function(e) {
      checkNumClicked(e.target);
   });
}

// Check the current number of active checkboxes
function checkNumClicked(checkbox) {

   // Update # of checkbox boxes
   checkbox.checked ? currentNumActive++ : currentNumActive--;

   // Remove origin
   if (currentNumActive === 0) {
      var currentOrigin = document.getElementById('origin');
      if (currentOrigin) currentOrigin.id = '';
   }

   // Set origin
   else if (currentNumActive === 1) checkbox.id = 'origin';

   // Get travel time
   else if (currentNumActive === 2) {

      // Get both locations
      var origin = '';
      var destination = '';
      console.log('fetching..');

   } else {
      
   }

}