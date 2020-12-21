n1 = int(input("Digite o primeiro numero inteiro: "))
n2 = int(input("Digite o segundo numero inteiro: "))
if n1 > n2:
    print("O primeiro valor {} e maior que o segundo valor {}".format(n1, n2))
elif n1 < n2:
    print("O segundo valor {1} e maior que o primeiro valor {0}".format(n1, n2))
else:
    print("O primeiro valor {} e igual ao segundo valor {}".format(n1, n2))
