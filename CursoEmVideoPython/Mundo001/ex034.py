salario = float(input('Digite um salario: R$'))
if salario > 1250:
    print('Salario: R${:.2f}\nAumento: R${:.2f}\nValor final: R${:.2f}'
          .format(salario, salario * 0.1, salario + salario * 0.1))
else:
    print('Salario: R${:.2f}\nAumento: R${:.2f}\nValor final: R${:.2f}'
          .format(salario, salario * 0.15, salario + salario * 0.15))
