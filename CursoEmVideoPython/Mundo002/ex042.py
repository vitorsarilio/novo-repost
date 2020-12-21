r1 = float(input('Digite o lado 1: '))
r2 = float(input('Digite o lado 2: '))
r3 = float(input('Digite o lado 3: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Pode formar um triangulo')
    if r1 == r2 and r2 == r3:
        print('Triangulo Equilatero')
    elif r1 == r2 or r2 == r3 or r3 == r1:
        print('Triangulo Isoceles')
    else:
        print('Trinagulo Escaleno')
else:
    print('Nao pode formar um triangulo')