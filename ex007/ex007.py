import random
numero = random.randint(1,10)
usuario = 0

while usuario !=numero:
    usuario = int(input("Digite um numero: "))


print("Acertou numero era: "+str(numero))