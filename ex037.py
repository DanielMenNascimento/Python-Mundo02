# Conversor númerico para Binário, Octal e Hexadecimal

numero = int(input('Digite o número que deseja converter: '))
print(''' Escolha uma das bases para converção
[ 1 ] Binário
[ 2 ] Octal
[ 3 ] Héxadecimal''')
opcao = int(input('Sua Opção: '))
if opcao == 1:
    print('O número {}, em binário fica {}.'.format(numero, bin(numero)[2:]))
elif opcao == 2:
    print('O número {}, em octals fica {}.'.format(numero, oct(numero)[2:]))
elif opcao == 3:
    print('O número {}, em héxadecimal fica {}.'.format(numero, hex(numero)[2:]))
else:
    print('Opção inválida')
