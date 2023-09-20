class ContaBancaria:
    def __init__(self,saldo):
        self.saldo = saldo

    def getSaldo(self):
        return self.saldo
    
    def setSaldo(self,saldo):
        self.saldo = saldo

    def exibeSaldo(self):
        print("Saldo: "+str(self.saldo))