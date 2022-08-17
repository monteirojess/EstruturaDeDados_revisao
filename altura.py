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