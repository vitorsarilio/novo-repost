import math
co = float(input('Cateto oposto: '))
ca = float(input('Cateto adjacente: '))
h = math.hypot(co, ca)
print('Cateto oposto: {}\nCateto adjacente:{}\nHipotenusa: {}'.format(co, ca, h))
