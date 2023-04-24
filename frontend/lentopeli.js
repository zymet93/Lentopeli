let name = prompt("Please enter your name:");
let job = prompt("Please enter your job:");





// Create an array of addresses
var addresses = [  {    name: 'Address 1',    latitude: 40.7128,    longitude: -74.0060  },  {    name: 'Address 2',    latitude: 37.7749,    longitude: -122.4194  },  {    name: 'Address 3',    latitude: 51.5074,    longitude: -0.1278  },  {    name: 'Address 4',    latitude: 48.8566,    longitude: 2.3522  },  {    name: 'Address 5',    latitude: 35.6895,    longitude: 139.6917  }];

// Create a Leaflet map
var map = L.map('map').setView([40.7128, -74.0060], 10);

// Add a tile layer
L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
  attribution: 'Map data &copy; OpenStreetMap contributors'
}).addTo(map);

// Loop through the addresses array and add markers to the map
addresses.forEach(function(address) {
  L.marker([address.latitude, address.longitude]).addTo(map)
    .bindPopup(address.name);

});

var circle = L.circle([51.508, -0.11], {
    color: 'red',
    fillColor: '#f03',
    fillOpacity: 0.5,
    radius: 500
}).addTo(map);

circle.bindPopup("I am a circle.");

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

async function getmyairports() {
    const val = await fetch("http://127.0.0.1:3000/airports");
    const jsonData = await val.json();
    console.log(jsonData);
}

getmyairports();
