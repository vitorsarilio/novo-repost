import secrets
lista = ['Pedra', 'Papel', 'Tesoura']
humano = int(input('1 - Pedra\n2 - Papel\n3 - Tesoura\n'))-1
maquina = secrets.choice(lista)
maquina2 = lista.index(maquina)
if maquina2 == humano:
    print('Voce escolheu {} e o pc {} entao houve empate'.format(lista[humano], maquina))
elif maquina2 == 0 and humano == 1 or maquina2 == 1 and humano == 2 or maquina2 == 2 and humano == 0:
    print('Voce escolheu {} e o pc {} entao voce ganhou'.format(lista[humano], maquina))
else:
    print('Voce escolheu {} e o pc {} entao voce perdeu'.format(lista[humano], maquina))
