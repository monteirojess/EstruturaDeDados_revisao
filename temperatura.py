#Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre atemperatura em graus Celsius. C = 5 * ((F-32) / 9).


temperatura = float(input('Digite uma temperatura em Fahrenheit:'))
conversor = (temperatura - 32) * 5 / 9
print(f'{conversor:.2f}ºC')