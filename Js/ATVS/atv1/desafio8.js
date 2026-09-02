function ehPalindromo(texto) {
  const limpo = texto
    .toLowerCase()
    .replace(/\s/g, "");

  const invertido = limpo.split("").reverse().join("");

  return limpo === invertido;
}

console.log(ehPalindromo("Arara"));
console.log(ehPalindromo("A sacada da casa"));
console.log(ehPalindromo("JavaScript"));

module.exports = ehPalindromo;
