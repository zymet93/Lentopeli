let name = prompt("Please enter your name:");
let job = prompt("Please enter your job:");




// Create a Leaflet map and set the initial view to somewhere in Europe
var map = L.map('map').setView([48.8566, 2.3522], 5);

// Add a tile layer
L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
  attribution: 'Map data &copy; OpenStreetMap contributors'
}).addTo(map);

// Function to add markers from API data to the map
async function addMarkers() {
  const val = await fetch("http://127.0.0.1:3000/airports");
  const jsonData = await val.json();

  for (let i = 0; i < jsonData.length; i++) {
    const marker = L.marker([jsonData[i].latitude_deg, jsonData[i].longitude_deg]).addTo(map);
    marker.bindPopup(`${jsonData[i].name} (${jsonData[i].ident}) - ${jsonData[i].iso_country}`);
    marker.on('click', function() {
      const answer = confirm(`Do you want to fly to ${jsonData[i].name}?`);
      if (answer) {
        const selectedOption = countrySelect.querySelector(`option[value='${jsonData[i].ident}']`);
        if (selectedOption) {
          selectedOption.selected = true;
        }
        document.getElementById('fly-button').disabled = false;
      }
    });
  }
}


// Call the function to add markers to the map
addMarkers();


const countrySelect = document.getElementById('country-select');

// Fetch airport data from backend API
/*fetch('/airports')
  .then(response => response.json())
  .then(data => {
    // Build country options list
    const countries = {};
    data.forEach(airport => {
      if (!(airport.iso_country in countries)) {
        countries[airport.iso_country] = true;
        const option = document.createElement('option');
        option.text = airport.iso_country;
        option.value = airport.iso_country;
        countrySelect.add(option);
      }
    });
    // Remove the "loading countries" option
    countrySelect.remove(0);
  });*/

/* async function getmyairports() {
    const val = await fetch("http://127.0.0.1:3000/airports");
    const jsonData = await val.json();
    console.log(jsonData);
}

getmyairports(); */

async function getmyairports() {
    const val = await fetch("http://127.0.0.1:3000/airports");
    const jsonData = await val.json();
    const select = document.getElementById("country-select");
    for (let i = 0; i < jsonData.length; i++) {
        const option = document.createElement("option");
        option.value = jsonData[i].ident;
        option.text = `${jsonData[i].name} (${jsonData[i].ident}) - ${jsonData[i].iso_country}`;
        select.add(option);
    }
}


// Call the function to populate the select element
getmyairports();

