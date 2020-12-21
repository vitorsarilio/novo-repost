kmh = int(input('Digite a velocidade do carro:  '))
multa = 7.00
limitev = 80
if kmh > limitev:
    kmmulta = (kmh - limitev) * multa
    print('Vc foi multado!\nVelocidade: {} KM/H\nVelocidade acima do permitido: {} KM/H\nMulta: R${:.2F}'
          .format(kmh, kmh - limitev, kmmulta))
else:
    print('Velocidade ok!')
