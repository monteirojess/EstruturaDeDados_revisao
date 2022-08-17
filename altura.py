#Faça um Programa que peça a idade e a altura de 5 pessoas, armazene cada informação no seu respectivo vetor. Imprima a idade e a altura na ordem inversa a ordem lida.

alturas = []
idades = []
for i in range(5):
    usuario_altura = float(input('Digite a altura:'))
    usuario_idade = float(input('Digite a idade:'))
    alturas.append(usuario_altura)
    idades.append(usuario_idade)
new_altura = list(reversed(alturas))
new_idade = list(reversed(idades))
print(f'Alturas: {new_altura}')
print(f'Idades: {new_idade}')
