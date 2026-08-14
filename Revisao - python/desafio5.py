class Pessoa:
    def __init__(self, nome, idade, email):
        self.nome = nome
        self.idade = idade
        self.email = email

    @property
    def idade(self):
        return self._idade

    @idade.setter
    def idade(self, valor):
        if valor < 0:
            raise ValueError("Idade não pode ser negativa!")
        self._idade = valor

    def aniversario(self):
        self.idade += 1
        print(f"{self.nome} fez aniversário! Nova idade: {self.idade}")

    def exibir_info(self):
        return f"Nome: {self.nome} | Idade: {self.idade} | Email: {self.email}"



pessoa1 = Pessoa("Ana", 25, "ana@email.com")
print(pessoa1.exibir_info())

pessoa1.aniversario()

try:
    pessoa2 = Pessoa("Bruno", -5, "bruno@email.com")
except ValueError as erro:
    print("Erro:", erro)
