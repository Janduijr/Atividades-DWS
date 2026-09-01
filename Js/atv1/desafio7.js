function jogarPedraPapelTesoura(jogador1, jogador2) {
  const opcoes = ["pedra", "papel", "tesoura"];

  const j1 = jogador1.toLowerCase();
  const j2 = jogador2.toLowerCase();

  if (!opcoes.includes(j1) || !opcoes.includes(j2)) {
    return "Jogada inválida";
  }

  if (j1 === j2) {
    return "Empate";
  }

  const vence = {
    pedra: "tesoura",
    papel: "pedra",
    tesoura: "papel",
  };

  if (vence[j1] === j2) {
    return "Jogador 1 venceu";
  } else {
    return "Jogador 2 venceu";
  }
}

console.log(jogarPedraPapelTesoura("pedra", "tesoura"));
console.log(jogarPedraPapelTesoura("papel", "pedra"));
console.log(jogarPedraPapelTesoura("tesoura", "papel"));
console.log(jogarPedraPapelTesoura("pedra", "papel"));
console.log(jogarPedraPapelTesoura("pedra", "pedra"));

module.exports = jogarPedraPapelTesoura;
