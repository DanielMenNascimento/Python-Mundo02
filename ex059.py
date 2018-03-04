# Criando um Menu de Opções

from time import sleep
n1 = int(input('1° Valor: '))
n2 = int(input('2° Valor: '))
opcao = 0
while opcao != 5:
    print('''======== MENU ========
[ 1 ] Somar
[ 2 ] Multiplicar
[ 3 ] Maior
[ 4 ] Novos números
[ 5 ] Sair
======== xxxx ========''')

    opcao = int(input('Escolha uma opção: '))

    if opcao == 1:
       print('{} + {} = {}'.format(n1, n2, n1 + n2))

    elif opcao == 2:
        print('{} x {} = {}'.format(n1, n2, n1 * n2))

    elif opcao == 3:
        if n1 > n2:
            print('{} > {}'.format(n1, n2))
        elif n1 < n2:
            print('{} < {}'.format(n1, n2))
        elif n1 == n2:
            print('{} = {}'.format(n1, n2))

    elif opcao == 4:
        n1 = int(input('1° Valor: '))
        n2 = int(input('2° Valor: '))

    elif opcao == 5:
        print('Finalizando...')

    else:
        print('Digite uma das opções válidas!')

    print('-==' * 8)
    sleep(2)


print('Fim do programa, Volte sempre!')
