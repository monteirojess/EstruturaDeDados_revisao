#Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem caso o valor seja inválido e
#continue pedindo até que o usuário informe um valor válido.

nota_invalida = False
while nota_invalida == False:
    nota = int(input('Digite uma nota entre 0 e 10:'))
    if nota < 0 or nota > 10:
        nota_invalida = False
        print('Nota inválida, digite um valor válido !')
    else:
        nota_invalida = True
        print('Nota {} é válida !'.format(nota))
