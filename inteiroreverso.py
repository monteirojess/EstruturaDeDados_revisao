# Reverso do número. Faça uma função que retorne o reverso de um número inteiro informado.

def number_inverted(numero_2):
    numero_final = int(str(numero_inicial)[::-1])
    return numero_final



numero_inicial = int(input('Digite um número:'))
number_inverted(numero_inicial)
numero_final = number_inverted(numero_inicial)
print(f'O número é: {numero_inicial}, e o número invertido é: {numero_final}.')
