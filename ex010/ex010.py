numero = int(input("Digite um número: "))

a, b = 0, 1

while a <= numero:
    print(a)
    a, b = b, a + b
