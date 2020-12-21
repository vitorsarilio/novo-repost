from datetime import date
ano = int(input("Digite seu ano de nascimento: "))
idade = date.today().year - ano
tempo = 18 - idade
if idade < 18:
    print("Sua idade e {} anos vc ainda nao pode se alistar falta {} anos".format(idade, tempo))
elif idade == 18:
    print("Sua idade e {} anos vc tem que se alistar esse ano".format(idade))
else:
    print("Sua idade e {} anos vc ja se alistou ha {} anos".format(idade, tempo*-1))
