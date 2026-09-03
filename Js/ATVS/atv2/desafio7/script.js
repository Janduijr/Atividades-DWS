class Produto {
    constructor(nome, preco, quantidade) {
        this.nome = nome;
        this.preco = preco;
        this.quantidade = quantidade;
    }

    aplicarDesconto(percentual) {
        this.preco = this.preco - (this.preco * percentual / 100);
    }

    estaDisponivel() {
        return this.quantidade > 0;
    }
}

const produto1 = new Produto('Teclado', 250, 10);
const produto2 = new Produto('Mouse', 120, 0);
const produto3 = new Produto('Monitor', 900, 5);

produto1.aplicarDesconto(15);

const resultado = document.querySelector('#resultado');

[produto1, produto2, produto3].forEach((produto) => {
    resultado.innerHTML += `
        <p>
            ${produto.nome} - R$ ${produto.preco.toFixed(2)} -
            ${produto.estaDisponivel() ? 'Disponível' : 'Indisponível'}
        </p>
    `;
});
