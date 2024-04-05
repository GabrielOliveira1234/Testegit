class Aluno:
    def __init__(self, matricula, nome, sexo, idade):
        self.matricula = matricula
        self.nome = nome
        self.sexo = sexo
        self.idade = idade

    def mostrar_informacoes(self):
        print(f"Matrícula: {self.matricula}")
        print(f"Nome: {self.nome}")
        print(f"Sexo: {self.sexo}")
        print(f"Idade: {self.idade}")

aluno1 = Aluno("000081", "Gabriel", "Feminino", 20)
aluno1.mostrar_informacoes()

