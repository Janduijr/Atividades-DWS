class Retangulo {
  constructor(base, altura) {
    this.base = base;
    this.altura = altura;
  }

  calcularArea() {
    return this.base * this.altura;
  }

  calcularPerimetro() {
    return 2 * (this.base + this.altura);
  }
}

const retangulo1 = new Retangulo(5, 3);

console.log("Área:", retangulo1.calcularArea());
console.log("Perímetro:", retangulo1.calcularPerimetro());

module.exports = Retangulo;
