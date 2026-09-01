function validarSenha(senha) {
  const erros = [];

  if (senha.length < 8) {
    erros.push("A senha deve ter no mínimo 8 caracteres");
  }

  if (!/[A-Z]/.test(senha)) {
    erros.push("A senha deve ter ao menos uma letra maiúscula");
  }

  if (!/[0-9]/.test(senha)) {
    erros.push("A senha deve ter ao menos um número");
  }

  return erros.length === 0 ? ["Senha válida"] : erros;
}

console.log(validarSenha("abc123"));
console.log(validarSenha("Abcdefgh1"));

module.exports = validarSenha;
