let segundosTotais = 3665;

let horas = Math.floor(segundosTotais / 3600);
let minutos = Math.floor((segundosTotais % 3600) / 60);
let segundos = segundosTotais % 60;

console.log(horas + "h " + minutos + "min " + segundos + "s");
