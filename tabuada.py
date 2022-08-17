number = int(input('De qual número deseja ver a tabuada:'))
for i in range (0, 10 + 1):
    resultado = number * i
    print('{} x {} = {}'.format(number, i, resultado))