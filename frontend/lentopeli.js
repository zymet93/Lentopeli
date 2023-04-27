//let name = prompt("Please enter your name:");
//let job = prompt("Please enter your job:");

async function getPlayer(name, job) {
    let val = await fetch("http://127.0.0.1:3000/player/create/" + name + "/" + job).then(function(res) {
        return res.json();
    });
    return val;
}

async function getPlayerUpdate(index) {
    let val = await fetch("http://127.0.0.1:3000/player/" + index + "/get").then(function(res) {
        return res.json();
    });
    return val;
}

function resetcookie() {
    document.cookie = "fgplayercookie=;expires=Thu, 01 Jan 1970 00:00:01 GMT";
}

if (document.cookie.split(";").some((item) => item.trim().startsWith("fgplayercookie="))) {
    document.getElementById("newdiv").classList.add("hidden");
    const cookieValue = document.cookie
          .split("; ")
          .find((row) => row.startsWith("fgplayercookie="))?.split("=")[1];
    console.log(cookieValue);
    getPlayerUpdate(cookieValue).then(function(res) {
        console.log(res);

        let select = document.getElementById("player-topname");
        select.innerHTML = res.playerName;

        select = document.getElementById("player-toplocation");
        select.innerHTML = res.playerLocation;

        select = document.getElementById("player-money");
        select.innerHTML = res.playerMoney;

        select = document.getElementsByClassName("profession")[0];
        select.innerHTML = 'Profession: ' + res.playerProfession + '<progress id="player-profession"></progress>';
    });
} else {
    document.getElementById("maindiv").classList.add("hidden");
}

const plyform = document.querySelector("#playercreator");
plyform.addEventListener("submit", async function(e) {
    e.preventDefault();
    const name = document.getElementById("nimimerkkikentta").value;
    const job = document.getElementById("jobselect").value;

    getPlayer(name, job).then(function(res) {
        console.log(res);
        document.cookie = "fgplayercookie=" + res.playersIndex;

        let select = document.getElementById("player-topname");
        select.innerHTML = res.playerName;

        select = document.getElementById("player-toplocation");
        select.innerHTML = res.playerLocation;

        select = document.getElementById("player-money");
        select.innerHTML = res.playerMoney;

        select = document.getElementsByClassName("profession")[0];
        select.innerHTML = 'Profession: ' + res.playerProfession + '<progress id="player-profession"></progress>';
    }).then(function() {
        window.location.reload(false)
    });
});

function flytobotan(target) {
    const cookieValue = document.cookie
          .split("; ")
          .find((row) => row.startsWith("fgplayercookie="))?.split("=")[1];
    fetch("http://127.0.0.1:3000/fly/" + cookieValue + "/" + target).then(function(){window.location.reload(false)});
}

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
          flytobotan(selectedOption.value);
        }
        document.getElementById('fly-button').disabled = false;
      }
    });
  }
}


// Call the function to add markers to the map
addMarkers();


const countrySelect = document.getElementById('country-select');



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
    document.getElementById("country-select").value=document.getElementById("player-toplocation").innerHTML;
}

// Call the function to populate the select element
getmyairports();

const flyform = document.querySelector(".country-select-form");
flyform.addEventListener("submit", async function(e) {
    e.preventDefault();
    const flyselect = document.getElementById("country-select");
    flytobotan(flyselect.value);
});
function createNewGame() {
    // Delete saved cookies
    document.cookie = "fgplayercookie=;expires=Thu, 01 Jan 1970 00:00:01 GMT";

    // Call creategame() function
    fetch('/player/create/name/job')
    .then(response => response.json())
    .then(data => {
        // Do something with the response data, such as redirecting to a new page
    })
    .catch(error => {
        console.error('Error:', error);
        location.reload();

    });
}
