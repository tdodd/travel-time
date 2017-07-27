// Get datalist options
var options = document.getElementsByClassName('dl-option');

// User's saved locations
var locations = [];
for (var i = 0; i < options.length; i++) {
   locations.push(options[i].value);
}

// Validate form
function validateLocations() {

   // Inputs
   var from = document.getElementById('from-input').value;
   var to = document.getElementById('to-input').value;

   // Check if input is in datalist
   if (locations.indexOf(from) > -1 && locations.indexOf(to) > -1) {
      return true;
   } else {
      return false;
   }

}