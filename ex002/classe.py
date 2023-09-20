class Pessoa:
    def __init__(self,nome,idade):
        self.nome = nome
        self.idade = idade

    def exibirDados(self):
        print("Nome: "+self.nome+"\nIdade: "+str(self.idade))