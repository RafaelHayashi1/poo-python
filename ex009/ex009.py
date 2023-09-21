numero = int(input("Digite um numero: "))
numeroB = numero-1
for i in range(numeroB,0,-1):
    numero*=i

'''
while contador !=0:
    numero *=contador
    contador-=1
'''
print(numero) 