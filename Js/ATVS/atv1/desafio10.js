function fibonacci(n) {
  if (n < 0) return "Número inválido";
  if (n === 0) return 0;
  if (n === 1) return 1;

  let anterior = 0;
  let atual = 1;

  for (let i = 2; i <= n; i++) {
    const proximo = anterior + atual;
    anterior = atual;
    atual = proximo;
  }

  return atual;
}

console.log(fibonacci(0));
console.log(fibonacci(1));
console.log(fibonacci(5));
console.log(fibonacci(10));

module.exports = fibonacci;
