# Vários números com flag

cont = soma = 0
while True:
    num = int(input('Digite um número [999 -> STOP]: '))
    if num == 999:
        break
    else:
        soma += num
        cont += 1
print('A soma dos {} valores foi {}.'.format(cont, soma))
