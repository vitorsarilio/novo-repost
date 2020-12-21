km = float(input('Km rodado: '))
dias = int(input('Dias Alugado: '))
adia = 60
akm = 0.15
vdia = dias * adia
vkm = km * akm
total = vdia + vkm
print('Km rodado: {}\nDias alugado: {}\nValor dia: {}\nValor km: {}\nTotal a pagar: R${}'
      .format(km, dias, vdia, vkm, total))
