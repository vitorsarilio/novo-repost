import random
num = int(input('Digite um numero: '))
aleatorio = random.randint(0, 5)
print('Vc escolheu o numero {}, o computador escolheu o numero {}'.format(num, aleatorio))
if num == aleatorio:
    print('Vc ganhou!')
else:
    print('Vc perdeu!')
