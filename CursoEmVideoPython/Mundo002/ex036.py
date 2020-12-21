valocasa = float(input('Qual o valor da casa? R$'))
salariocomprador = float(input('Qual o seu salario? R$'))
anospagamento = int(input('Pagar em quantos anos? '))
valormes = valocasa / (anospagamento * 12)
salario30 = salariocomprador * 0.3

print('Prestacao mensal de R${:.2f} em {} anos'.format(valormes, anospagamento))

if salario30 < valormes:
    print('Emprestimo negado pois 30% do salario (R${:.2f}) e menos q a prestacao R${:.2f}'
          .format(salario30, valormes))
else:
    print('Emprestimo aceito pois 30% salario (R${:.2f}) e maior ou igual a prestacao R${:.2f}'
          .format(salario30, valormes))
