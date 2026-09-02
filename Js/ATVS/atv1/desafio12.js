function valorTotalEstoque(produtos) {
  return produtos.reduce((total, produto) => {
    return total + produto.preco * produto.quantidade;
  }, 0);
}

function produtoMaisCaro(produtos) {
  if (produtos.length === 0) return null;

  return produtos.reduce((maisCaro, produtoAtual) => {
    return produtoAtual.preco > maisCaro.preco ? produtoAtual : maisCaro;
  });
}

function produtosComQuantidadeAbaixoDe(produtos, minimo) {
  return produtos.filter((produto) => produto.quantidade < minimo);
}

const estoque = [
  { nome: "Teclado", preco: 120, quantidade: 10 },
  { nome: "Mouse", preco: 60, quantidade: 3 },
  { nome: "Monitor", preco: 800, quantidade: 5 },
  { nome: "Cabo HDMI", preco: 25, quantidade: 1 },
];

console.log("Valor total do estoque:", valorTotalEstoque(estoque));
console.log("Produto mais caro:", produtoMaisCaro(estoque));
console.log("Estoque baixo (< 5):", produtosComQuantidadeAbaixoDe(estoque, 5));

module.exports = {
  valorTotalEstoque,
  produtoMaisCaro,
  produtosComQuantidadeAbaixoDe,
};
