class Pessoa:
    def __init__(self,nome,idade):
        self.nome = nome
        self.idade = idade

    def exibirDados(self):
        print("Nome: "+self.nome+"\nIdade: "+str(self.idade))


class Estudante(Pessoa):
    def __init__(self, nome, idade,matricula):
        super().__init__(nome, idade)
        self.matricula = matricula

    def exibirMatricula(self):
         print("Nome: "+self.nome+"\nIdade: "+str(self.idade)+"\nId matricula: "+str(self.matricula))