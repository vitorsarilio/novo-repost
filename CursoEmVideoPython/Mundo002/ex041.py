from datetime import date
nascimento = int(input("Digite o ano de nascimento: "))
idade = date.today().year - nascimento
if idade < 10:
    print("Idade: {} categoria MIRIM".format(idade))
elif idade < 15:
    print("Idade: {} categoria INFANTIL".format(idade))
elif idade < 20:
    print("Idade: {} categoria JUNIOR".format(idade))
elif idade < 21:
    print("Idade: {} categoria SENIOR".format(idade))
else:
    print("Idade: {} categoria MASTER".format(idade))
