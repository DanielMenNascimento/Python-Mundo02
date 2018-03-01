# Média de notas do aluno

n1 = float(input('1° nota: '))
n2 = float(input('2° nota: '))
media = (n1 + n2) / 2

if 7 > media >= 5:
    print('\033[1;33m RECUPERAÇÃO\033[m com média {:.1f}'.format(media))
elif media < 5:
    print('\033[1;31m REPROVADO\033[m com média {:.1f}'.format(media))
else:
    print('\033[1;32m APROVADO\033[m com média {:.1f}'.format(media))