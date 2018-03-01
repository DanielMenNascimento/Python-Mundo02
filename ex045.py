# Pedra, Papel, Tesoura

from time import sleep
from random import randint

itens = ('PEDRA', 'PAPEL', 'TESOURA')
comp = randint(0, 2)
# print('A máquina escolheu {}'.format(itens[comp]))

print('''Suas opṍes:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')
jogador = int(input('Opção: '))
print('JO')
sleep(0.5)
print('KEN')
sleep(0.5)
print('PO')
sleep(0.5)
print('-=' * 15)
print('Máquina ==> {}'.format(itens[comp]))
print('Você ==> {}'.format(itens[jogador]))
print('-=' * 15)

if comp == 0: # Máquina jogou PEDRA
    if jogador == 0:
        print('\033[1;33m EMPATE \033[m')
    elif jogador == 1:
        print('\033[1;32m JOGADOR VENCE \033[m')
    elif jogador == 2:
        print('\033[1;31m MÁQUINA VENCE \033[m')
    else:
        print('Jogada inválida!')
elif comp == 1: # Máquina jogou PAPEL
    if jogador == 0:
        print('\033[1;31m MÁQUINA VENCE \033[m')
    elif jogador == 1:
        print('\033[1;33m EMPATE \033[m')
    elif jogador == 2:
        print('\033[1;32m JOGADOR VENCE \033[m')
    else:
        print('Jogada inválida!')
elif comp == 2: # Máquina jogogu TESOURA
    if jogador == 0:
        print('\033[1;32m JOGADOR VENCE \033[m')
    elif jogador == 1:
        print('\033[1;31m MÁQUINA VENCE \033[m')
    elif jogador == 2:
        print('\033[1;33m EMPATE \033[m')
    else:
        print('Jogada inválida!')
else:
    print('Opção inválida! Se não quiser escolher uma opção pressione [ENTER] e será escolhido automaticamente!')
