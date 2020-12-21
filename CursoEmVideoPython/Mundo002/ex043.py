peso = float(input('Digite seu peso: '))
altura = float(input('Digite sua altura: '))
imc = peso / (altura * altura)
if imc < 18.5:
    print('IMC = {:.2f} abaixo do peso'.format(imc))
elif imc <= 25:
    print('IMC = {:.2f} peso ideal'.format(imc))
elif imc <= 30:
    print('IMC = {:.2f} sobrepeso'.format(imc))
elif imc <= 40:
    print('IMC = {:.2f} obesidade'.format(imc))
else:
    print('IMC = {:.2f} obesidade morbida'.format(imc))
