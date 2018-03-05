# Tratando vários valores v1.0

num = 0
cont = 0
soma =0

num = int(input('Digite um número[999 -> STOP]: '))
while num != 999:
    cont += 1
    soma += num
    num = int(input('Digite um número[999 -> STOP]: '))
    
print('Você digitou {} números.'.format(cont))
print('A soma entre eles é {}.'.format(soma))
