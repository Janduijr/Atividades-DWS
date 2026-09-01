class ContaBancaria {
  constructor(titular, saldo = 0) {
    this.titular = titular;
    this.saldo = saldo;
  }

  depositar(valor) {
    if (valor <= 0) {
      return "Valor de depósito inválido";
    }
    this.saldo += valor;
    return this.saldo;
  }

  sacar(valor) {
    if (valor <= 0) {
      return "Valor de saque inválido";
    }
    if (valor > this.saldo) {
      return "Saldo insuficiente";
    }
    this.saldo -= valor;
    return this.saldo;
  }

  extrato() {
    return `Titular: ${this.titular} | Saldo atual: R$ ${this.saldo.toFixed(2)}`;
  }
}

const contaMaria = new ContaBancaria("Maria", 500);
const contaJoao = new ContaBancaria("João", 100);

contaMaria.depositar(200);
console.log(contaMaria.extrato());

contaJoao.sacar(50);
console.log(contaJoao.extrato());

console.log(contaJoao.sacar(1000));

const valorTransferencia = 100;
contaMaria.sacar(valorTransferencia);
contaJoao.depositar(valorTransferencia);

console.log(contaMaria.extrato());
console.log(contaJoao.extrato());

module.exports = ContaBancaria;
