import math
a = float(input('Digite um angulo: '))
s = math.sin(math.radians(a))
c = math.cos(math.radians(a))
t = math.tan(math.radians(a))
print('Seno: {:.2f}\nCoseno: {:.2f}\nTangente:{:.2f}\n'.format(s, c, t))
