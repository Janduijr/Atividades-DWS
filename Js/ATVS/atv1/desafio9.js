function estatisticasNotas(notas) {
  if (notas.length === 0) {
    return { media: 0, maior: 0, menor: 0 };
  }

  const soma = notas.reduce((total, nota) => total + nota, 0);
  const media = soma / notas.length;
  const maior = Math.max(...notas);
  const menor = Math.min(...notas);

  return { media, maior, menor };
}

const notasTurma = [7, 8.5, 6, 9, 10, 4.5];
console.log(estatisticasNotas(notasTurma));

module.exports = estatisticasNotas;
