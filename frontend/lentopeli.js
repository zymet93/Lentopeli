let name = prompt("Please enter your name:");
let job = prompt("Please enter your job:");


function getAirports(connection) {
    const sql = "SELECT iso_country, ident, name, type, latitude_deg, longitude_deg\n" +
        "             FROM airport";
    const cursor = connection.cursor({dictionary: true});
    cursor.execute(sql);
    const result = cursor.fetchall();
    return result;
}



fetch('/search?name=' + name + '&job=' + job)
  .then(response => {
    // Handle the response from the server
  })
  .catch(error => {
    // Handle any errors that occurred during the request
  });
function getAirports(connection) {
    const sql = "SELECT iso_country, ident, name, type, latitude_deg, longitude_deg\n" +
        "             FROM airport";
    const cursor = connection.cursor({dictionary: true});
    cursor.execute(sql);
    const result = cursor.fetchall();
    return result;
}
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
