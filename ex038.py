''' Escreva um programa que leia dois números inteiros e compare-os. mostrando na tela uma mensagem:
 - O primeiro valor é maior
 - O segundo valor é maior
 - Não existe valor maior
 - Os dois são iguais '''

n1 = int(input('1° valor: '))
n2 = int(input('2° valor: '))

if n1 > n2:
    print('O PRIMEIRO número é maior!')
elif n1 < n2:
    print('O SEGUNDO número é maior!')
else:
    print('Os dois números são iguais!')