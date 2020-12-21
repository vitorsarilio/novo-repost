valorNormal = float(input('Valor do produto: R$'))
tipoPagamento = int(input('1 - Dinheiro ou Cheque\n2 - Cartao a vista\n3 - 2x no cartao\n4 - 3x ou mais no cartao\n'))
valorDinheiro = valorNormal - valorNormal * 0.1
valorCartaoAvista = valorNormal - valorNormal * 0.05
valorJuros = valorNormal + valorNormal * 0.2
if tipoPagamento == 1:
    print('10% de desconto valor: {}'.format(valorDinheiro))
elif tipoPagamento == 2:
    print('5% de desconto valor: {}'.format(valorCartaoAvista))
elif tipoPagamento == 3:
    print('Sem desconto valor: {}'.format(valorNormal))
elif tipoPagamento == 4:
    print('20% de juros valor: {}'.format(valorJuros))
else:
    print('Opcao invalida')
