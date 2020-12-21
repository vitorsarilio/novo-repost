valor = input('Digite algo: ')
print('{} e numerico? {}'.format(valor, valor.isnumeric()))
print('{} e alfabetico? {}'.format(valor, valor.isalpha()))
print('{} e espaco? {}'.format(valor, valor.isspace()))
print('{} e capitalizado? {}'.format(valor, valor.istitle()))
print('{} e maisculo? {}'.format(valor, valor.isupper()))
print('{} e minusculo? {}'.format(valor, valor.islower()))

