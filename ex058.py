# Jogo da adivinhação 2.0

from random import randint
from time import sleep
maquina = randint(0, 10)
acertou = False
palpites = 0
print('Eu pensei em um número entre 0 e 10.')
while not acertou:
    jogador = int(input('Qual número vocẽ acha que eu pensei: '))
    palpites += 1
    if jogador == maquina:
        acertou = True
    else:
        if jogador < maquina:
            sleep(1)
            print('Mais...')
            sleep(0.5)
        elif jogador > maquina:
            sleep(1)
            print('Menos...')
            sleep(0.5)
print('Acertou com {} tentativas!'.format(palpites))
