n1 = float(input('Digite primeiro numero: '))
n2 = float(input('Digite segundo numero: '))
n3 = float(input('Digite terceiro numero: '))
maiorv = max([n1, n2, n3], key = int)
menorv = min([n1, n2, n3], key = int)
print('Maior valor: {}\nMenor valor: {}'.format(maiorv, menorv))
