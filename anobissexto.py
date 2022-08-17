#Façaum Programa que peça um número correspondente a um determinado ano e em seguida informe se este ano é ou não bissexto.


ano = int(input('Digite o ano:'))
if ano % 4 == 0 and ano % 100 > 0:
    print('Ano é bissexto !')
elif ano % 4 == 0 and ano % 100 == 0 and ano % 400 == 0:
    print('Ano é bissexto !')
else:
    print('Ano não é bissexto !')


