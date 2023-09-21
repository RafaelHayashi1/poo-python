contador =0
numeros = [0,0]
while contador<2:
    numeros[contador] = int(input("Digite um numero: "))
    contador+=1


xdd=1
while xdd !=59:
    operador = int(input("Digite uma opercao: "))
    if operador ==1:
        soma = numeros[0]+numeros[1]
        print("Soma: "+str(soma))
    elif operador==2:
        multi = numeros[0]*numeros[1]
        print("Multi: "+str(multi))
    elif operador==3:
        if(numeros[0]>numeros[1]):
            print("Maior: "+str(numeros[0]))
        else:
            print("Maior: "+str(numeros[1]))
    elif operador ==4:
        xdd=59


