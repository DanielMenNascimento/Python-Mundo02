# Calculando desconto e júros

print('{:=^40}'.format(' Byte Studio '))
preco = float(input('Total a ser pago: R$'))
print('''Formas de pagamento:
{:<30}(10% de desconto)
{:<30}(5% de desconto)
{:<30}(Sem descontos e/ou Júros)
{:<30}(20% de Júros)
'''.format('[ 1 ] À vista dinheiro/cheque', '[ 2 ] À vista cartão', '[ 3 ] 2x cartão', '[ 4 ] 3x no cartão'))
opcao = int(input('Opção: '))

if opcao == 1:
    total = preco - (preco * 10 / 100)
    print('Pagando à vista, o total a pagar será de R${:.2f}'.format(total))
elif opcao == 2:
    total = preco - (preco * 5 / 100)
    print('Pagando à vista no cartão , o total a pagar será de R${:.2f}'.format(total))
elif opcao == 3:
    parcela = preco / 2
    print('Sua compra será parcelada em 2x de R${:.2f}'.format(parcela))
elif opcao == 4:
    total = preco + (preco * 20 / 100)
    parcela = total / 3
    print('Sua compra será parcelada em 3x de R${:.2f} com o valor final de R${:.2f}'.format(parcela, total))
else:
    print('Opção inválida!')
