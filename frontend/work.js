// Define the work options array
var workOptions = ['Koodari', 'Rakentaja', 'Kuski'];
var workNappula = document.querySelector('.work-nappula input[type="submit"]');

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

// Initialize an empty array to store the countries the player has worked in
var workedCountries = [];

// Function to check if the player has already worked in a country
function hasWorkedInCountry(country) {
  return workedCountries.includes(country);
}

// Handle the form submission
document.getElementById("work-form").addEventListener("submit", function(event) {
  event.preventDefault(); // prevent the default form submission

  // Get the selected country
  var countrySelect = document.getElementById("country-select");
  var selectedCountry = countrySelect.value;

  // Check if the player has already worked in this country
  if (hasWorkedInCountry(selectedCountry)) {
    alert("You've already worked in " + selectedCountry);
    return;
  }

  // Add the country to the workedCountries array
  workedCountries.push(selectedCountry);

  // Generate new work options
  var numWorkOptions = Math.floor(Math.random() * 3) + 1; // generate a random number between 1 and 3
  workSelect.innerHTML = ""; // clear the existing options
  for (var i = 0; i < numWorkOptions; i++) {
    var option = document.createElement("option");
    option.value = workOptions[i];
    option.text = workOptions[i];
    workSelect.add(option);
  }
});

function doworkin(target) {
    const cookieValue = document.cookie
          .split("; ")
          .find((row) => row.startsWith("fgplayercookie="))?.split("=")[1];
    fetch("http://127.0.0.1:3000/work/" + cookieValue + "/" + target).then(function(){window.location.reload(false)});
}
// Add a click event listener to the work nappula
workNappula.addEventListener('click', function() {
    // Get the selected work option
    var selectedWorkOption = workSelect.options[workSelect.selectedIndex].value;

    doworkin(selectedWorkOption);
});
