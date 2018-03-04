#  Validação de Dados

sexo = str(input('Informe seu sexo [M/F]: ')).upper().strip()[0]
while sexo not in 'MmFf':
    sexo = str(input('Inválido, por favor informe uma opção válida [M/F]: ')).upper().strip()[0]
print('Sexo {} registrado com \033[1;32mSUCESSO!\033[m'.format(sexo))
