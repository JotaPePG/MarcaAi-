// Inicializando o mapa
var map = L.map("map", {
  center: [-23.55052, -46.633308], // Coordenadas iniciais [latitude, longitude]
  zoom: 13, // Nível de zoom inicial
  zoomControl: false, // Desativando o controle de zoom
});

// Adicionando uma camada de tile do OpenStreetMap
L.tileLayer("https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png", {
  attribution:
    '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors',
}).addTo(map);

// Adicionando um marcador ao mapa
var esporte = L.marker([-15.7801, -47.9292])
  .addTo(map)
  .bindPopup("Futebol, Quadra 101")
  .openPopup();

esporte.on("click", function () {
  window.location.href = "../main/esporte.html"; // Substitua pelo seu link
});

var esporte2 = L.marker([-15.752210589006298, -47.8853830805223])
  .addTo(map)
  .bindPopup("Futebol, Quadra 102")
  .openPopup();

esporte2.on("click", function () {
  window.location.href = "../main/esporte2.html"; // Substitua pelo seu link
});

var esporte3 = L.marker([-15.790532578184004, -47.877629615615085])
  .addTo(map)
  .bindPopup("Futebol, Quadra 208")
  .openPopup();

esporte3.on("click", function () {
  window.location.href = "../main/esporte3.html"; // Substitua pelo seu link
});

const atvSearch = document.getElementById("atv_search");

function hideBar() {
  var style = window.getComputedStyle(atvSearch);
  var displayType = style.display;
  if (style.display === "block") {
    atvSearch.style.display = "none";
  } else {
    atvSearch.style.display = "block";
  }
}
