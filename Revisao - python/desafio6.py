class Pessoa:
    def __init__(self, nome, idade, email):
        self.nome = nome
        self.idade = idade
        self.email = email

    def exibir_info(self):
        return f"Nome: {self.nome} | Idade: {self.idade} | Email: {self.email}"


class Aluno(Pessoa):
    def __init__(self, nome, idade, email, matricula, curso):
        super().__init__(nome, idade, email)
        self.matricula = matricula
        self.curso = curso

    def exibir_dados_aluno(self):
        info_pessoa = self.exibir_info()
        return f"{info_pessoa} | Matrícula: {self.matricula} | Curso: {self.curso}"


# Testando
aluno1 = Aluno("Ana", 20, "ana@email.com", "2024001", "Engenharia")
aluno2 = Aluno("Bruno", 22, "bruno@email.com", "2024002", "Direito")

print(aluno1.exibir_dados_aluno())
print(aluno2.exibir_dados_aluno())
