n1 = float(input("Nota 1 do aluno: "))
n2 = float(input("Nota 2 do aluno: "))
media = (n1 + n2) / 2
if media < 5:
    print("Media: {:.2f} REPROVADO".format(media))
elif media < 7:
    print("Media: {:.2f} RECUPERACAO".format(media))
else:
    print("Media: {:.2f} APROVADO".format(media))
