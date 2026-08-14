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


class Curso:
    def __init__(self, nome):
        self.nome = nome
        self.alunos = []

    def adicionar_aluno(self, aluno):
        self.alunos.append(aluno)

    def listar_alunos(self):
        print(f"\nAlunos do curso {self.nome}:")
        if not self.alunos:
            print("Nenhum aluno cadastrado.")
        for aluno in self.alunos:
            print("-", aluno.exibir_dados_aluno())


curso = Curso("Programação Python")

aluno1 = Aluno("Ana", 20, "ana@email.com", "2024001", "Programação Python")
aluno2 = Aluno("Bruno", 22, "bruno@email.com", "2024002", "Programação Python")

curso.adicionar_aluno(aluno1)
curso.adicionar_aluno(aluno2)

curso.listar_alunos()
