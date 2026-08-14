class Pessoa:
    def __init__(self, nome, idade, email):
        self.nome = nome
        self.idade = idade
        self.email = email

    def exibir_info(self):
        return f"Nome: {self.nome} | Idade: {self.idade} | Email: {self.email}"



pessoa1 = Pessoa("Ana", 25, "ana@email.com")
pessoa2 = Pessoa("Bruno", 30, "bruno@email.com")
pessoa3 = Pessoa("Carla", 22, "carla@email.com")

print(pessoa1.exibir_info())
print(pessoa2.exibir_info())
print(pessoa3.exibir_info())
