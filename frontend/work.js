// Define the work options array
var workOptions = ['Coder', 'Builder', 'Driver'];

// Get a random number between 1 and 3 for the number of work options to show
var numWorkOptions = Math.floor(Math.random() * 3) + 1;

// Shuffle the work options array
workOptions.sort(() => Math.random() - 0.5);

// Get a reference to the work select element
var workSelect = document.getElementById('work-select');

// Add the selected number of work options to the dropdown
for (var i = 0; i < numWorkOptions; i++) {
  var option = document.createElement('option');
  option.value = workOptions[i];
  option.text = workOptions[i];
  workSelect.add(option);
}
document.getElementById("work-form").addEventListener("submit", function(event) {
  event.preventDefault(); // prevent the default form submission
  var workOptions = ['Coder', 'Builder', 'Driver'];
  var numWorkOptions = Math.floor(Math.random() * 3) + 1; // generate a random number between 1 and 3
  var workSelect = document.getElementById("work-select");
  workSelect.innerHTML = ""; // clear the existing options
  for (var i = 0; i < numWorkOptions; i++) {
    var option = document.createElement("option");
    option.value = workOptions[i];
    option.text = workOptions[i];
    workSelect.add(option);
  }
});
