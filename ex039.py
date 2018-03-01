# Alistamento militar

from datetime import date

ano = date.today().year
nasc = int(input('Ano de nascimento: '))
idade = ano - nasc
if idade == 18:
    print('\033[1;32mAPROVADO!\033[m Apresente-se ao posto de alistamento mais próximo imediatamente!')
elif idade < 18:
    print('\033[1;31mNEGADO!\033[m Você precisa ter 18 anos para se alistar.')
    print('Volte daqui a {}.'.format(18 - idade))
elif idade > 18:
    print('\033[1;31mMULTA!\033[m Fugindo dos serviços hein, porque não se apresentou quando tinha 18 anos?')
    print('Não se preoculpe, você está só {} ano atrasado.'.format(idade - 18))
