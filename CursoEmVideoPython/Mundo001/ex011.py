altura = float(input('Altura da parede: '))
largura = float(input('Largura da parede: '))
mq = altura * largura
mqt = 0.5
tn = mq * mqt
print('Altura da parede: {}m\nLargura da parede: {}m\nMetros quadrados: {:.2f}m\n Tinta necessaria: {:.2f} litros'
      .format(altura, largura, mq, tn))
