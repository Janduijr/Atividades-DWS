function classificarIMC(peso, altura) {
  const imc = peso / (altura * altura);

  if (imc < 18.5) {
    return "Abaixo do peso";
  } else if (imc < 25) {
    return "Peso normal";
  } else if (imc < 30) {
    return "Sobrepeso";
  } else {
    return "Obesidade";
  }
}

console.log(classificarIMC(50, 1.70));
console.log(classificarIMC(65, 1.70));
console.log(classificarIMC(80, 1.70));
console.log(classificarIMC(100, 1.70));

module.exports = classificarIMC;
