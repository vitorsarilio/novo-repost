nome = input('Digite um nome completo: ')
nomeSplit = nome.split()
print('Primeiro nome: {}'.format(nomeSplit[0]))
print('Ultimo nome: {}'.format(nomeSplit[len(nomeSplit)-1]))
