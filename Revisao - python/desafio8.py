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
        if not self.alunos:
            print("  Nenhum aluno cadastrado.")
        for aluno in self.alunos:
            print("  -", aluno.exibir_dados_aluno())


cursos = []


def cadastrar_curso():
    nome = input("Nome do curso: ")
    cursos.append(Curso(nome))
    print(f"Curso '{nome}' cadastrado com sucesso!\n")


def adicionar_aluno_ao_curso():
    if not cursos:
        print("Nenhum curso cadastrado ainda!\n")
        return

    print("\nCursos disponíveis:")
    for i, curso in enumerate(cursos):
        print(f"{i + 1} - {curso.nome}")

    try:
        escolha = int(input("Escolha o número do curso: ")) - 1
        curso_escolhido = cursos[escolha]
    except (ValueError, IndexError):
        print("Opção inválida!\n")
        return

    nome = input("Nome do aluno: ")
    idade = int(input("Idade do aluno: "))
    email = input("Email do aluno: ")
    matricula = input("Matrícula do aluno: ")

    aluno = Aluno(nome, idade, email, matricula, curso_escolhido.nome)
    curso_escolhido.adicionar_aluno(aluno)
    print(f"Aluno '{nome}' adicionado ao curso '{curso_escolhido.nome}'!\n")


def listar_cursos():
    if not cursos:
        print("Nenhum curso cadastrado ainda!\n")
        return

    print("\n===== Cursos cadastrados =====")
    for curso in cursos:
        print(f"\nCurso: {curso.nome}")
        curso.listar_alunos()
    print()


def menu():
    while True:
        print("===== Sistema de Cursos =====")
        print("1 - Cadastrar curso")
        print("2 - Adicionar aluno a um curso")
        print("3 - Listar cursos e alunos")
        print("4 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            cadastrar_curso()
        elif opcao == "2":
            adicionar_aluno_ao_curso()
        elif opcao == "3":
            listar_cursos()
        elif opcao == "4":
            print("Saindo do sistema...")
            break
        else:
            print("Opção inválida! Tente novamente.\n")


if __name__ == "__main__":
    menu()
