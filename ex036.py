# Aprovação de empréstimo bancário

''' dividir o valor pela quantidade de meses e verificar se esse valor é menor ou igual a 30%
 do salário '''

print('\033[1;34m-=-\033[m' * 20)
print('\033[1;30m{:^60}\033[m'.format('Agencia de Empréstimos'))
print('\033[1;34m-=-\033[m' * 20)

cliente = str(input('Por favor, digite seu nome: ')).title().strip().split()
nome = cliente[0]
valor = float(input('Olá {} por gentileza, informe o valor desejado: '.format(nome)))
meses = int(input('Certo {}, agora informe em quantos meses deseja pagar: '.format(nome)))
salario = float(input('Por questões de segurança, informe o seu salário: '))

mensalidade = valor / meses
atual = salario * 30 / 100

if mensalidade < atual:
    print('\033[1;32m\n{:*^60}\033[m'.format('Transferência aprovada com SUCESSO!'))
    print('Sua mensalidade será de R${:.2f} por {} meses.'.format(mensalidade, meses))
else:
    print('\033[1;31m\n{:¨^60}\033[m'.format('Transferência NEGADA!'))
    print('A mensalidade de R${:.2f} é maior que 30% de R${:.2f}'.format(mensalidade, salario))
print('-*' * 30)
