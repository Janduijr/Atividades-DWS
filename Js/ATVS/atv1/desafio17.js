class Agenda {
  constructor() {
    this.contatos = [];
  }

  adicionarContato(nome, telefone, categoria) {
    this.contatos.push({ nome, telefone, categoria });
    return this.contatos;
  }

  removerContato(nome) {
    this.contatos = this.contatos.filter((contato) => contato.nome !== nome);
    return this.contatos;
  }

  listarPorCategoria(categoria) {
    return this.contatos.filter((contato) => contato.categoria === categoria);
  }
}

const minhaAgenda = new Agenda();

minhaAgenda.adicionarContato("Maria", "99999-0001", "Família");
minhaAgenda.adicionarContato("João", "99999-0002", "Trabalho");
minhaAgenda.adicionarContato("Ana", "99999-0003", "Família");

console.log("Agenda completa:", minhaAgenda.contatos);
console.log("Categoria Família:", minhaAgenda.listarPorCategoria("Família"));

minhaAgenda.removerContato("João");
console.log("Agenda após remover João:", minhaAgenda.contatos);

module.exports = Agenda;
