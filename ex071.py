print('=' * 30)
print('{:^30}'.format('BANCO'))
print('=' * 30)
valor = int(input('SAQUE: R$'))
total = valor
ced = 50
totCed = 0

while True:
	if total >= ced:
		total -= ced
		totCed += 1
	else:
		if totCed > 0:
			print('Total de {} cédulas de R${:.2f}.'.format(totCed, ced))
		if ced == 50:
			ced = 20
		elif ced == 20:
			ced = 10
		elif ced == 10:
			ced = 1
		totCed = 0
		if total == 0:
			break