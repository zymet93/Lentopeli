const map = L.map('map').setView([60.23, 24.74], 13);
L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
  attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors',
}).addTo(map);

const airportMarkers = L.featureGroup().addTo(map);

const searchForm = document.querySelector('#single');
const input = document.querySelector('input[name=icao]');
searchForm.addEventListener('submit', async function(evt) {
  evt.preventDefault();
  const icao = input.value;
  const response = await fetch('http://127.0.0.1:3000/airport/' + icao);
  const airport = await response.json();
  // remove possible other markers
  airportMarkers.clearLayers();
  // add marker
  const marker = L.marker([airport.latitude_deg, airport.longitude_deg]).
      addTo(map).
      bindPopup(airport.name).
      openPopup();
  airportMarkers.addLayer(marker);
  // pan map to selected airport
  map.flyTo([airport.latitude_deg, airport.longitude_deg]);
});