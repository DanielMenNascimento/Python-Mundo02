# Maior e Menor valores

resp = 'S'
soma = quant = media = maior = menor = 0
while resp in 'Ss':
    num = int(input('Digite um número: '))
    soma += num
    quant += 1

    if quant == 1:
        maior = num
        menor = num

    else:
        if num > maior:
            maior = num

        elif num < menor:
            menor = num

    resp = str(input('Quer continuar [S/N]: ')).upper().strip()[0]

media = soma / quant
print('A média dos {} número digitados é {:.2f}'.format(quant, media))
print('O maior número foi {} e o menor foi {}'.format(maior, menor))
