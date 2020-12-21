km = int(input('Distancia em km da viagem: '))
if km <= 200:
    print('Distancia da viagem: {} km\nValor cobrado: R${:.2f}'.format(km, km * 0.50))
else:
    print('Distancia da viagem: {} km\nValor cobrado: R${:.2f}'.format(km, km * 0.45))