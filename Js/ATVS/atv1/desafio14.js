class Produto {
  constructor(nome, preco, quantidade) {
    this.nome = nome;
    this.preco = preco;
    this.quantidade = quantidade;
  }

  aplicarDesconto(porcentagem) {
    this.preco = this.preco - this.preco * (porcentagem / 100);
    return this.preco;
  }

  estaDisponivel() {
    return this.quantidade > 0;
  }
}

const produto1 = new Produto("Notebook", 3000, 5);
const produto2 = new Produto("Fone de Ouvido", 150, 0);
const produto3 = new Produto("Mouse Gamer", 200, 12);

console.log(`${produto1.nome} disponível?`, produto1.estaDisponivel());
produto1.aplicarDesconto(10);
console.log(`Novo preço do ${produto1.nome}:`, produto1.preco);

console.log(`${produto2.nome} disponível?`, produto2.estaDisponivel());

console.log(`${produto3.nome} disponível?`, produto3.estaDisponivel());
produto3.aplicarDesconto(25);
console.log(`Novo preço do ${produto3.nome}:`, produto3.preco);

module.exports = Produto;
