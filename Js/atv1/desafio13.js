let agenda = [];

function adicionarContato(nome, telefone, categoria) {
  agenda.push({ nome, telefone, categoria });
  return agenda;
}

function removerContato(nome) {
  agenda = agenda.filter((contato) => contato.nome !== nome);
  return agenda;
}

function listarPorCategoria(categoria) {
  return agenda.filter((contato) => contato.categoria === categoria);
}

adicionarContato("Maria", "99999-0001", "Família");
adicionarContato("João", "99999-0002", "Trabalho");
adicionarContato("Ana", "99999-0003", "Família");

console.log("Agenda completa:", agenda);
console.log("Categoria Família:", listarPorCategoria("Família"));

removerContato("João");
console.log("Agenda após remover João:", agenda);

module.exports = { adicionarContato, removerContato, listarPorCategoria };
