from random import choices
import random

participantes = []
nome = int(input("Digita o numero de participantes do sorteio: "))

for i in range(nome):
    valor = input(f"Digite o nome da {i+1}ª pessoa: ")
    participantes.append(valor)
print(participantes)  # Validar ordem informada
random.shuffle(participantes)  # Embaralha a lista de participantes
print(participantes)  # Validar se embaralhou
duplas = []  # Armazenar as duplas

while len(participantes) >= 2:
    dupla = [participantes.pop(), participantes.pop()]
    duplas.append(dupla)

# Verifica se sobrou participantes
sobrando = participantes[0] if participantes else None

# Exibir resultados:

print('Duplas sorteadas:')

for i, dupla in enumerate(duplas, start=1):
    print(f'Dupla {i}: {dupla[0]} e {dupla[1]}')

if sobrando:
    print(f'\n Pessoa que ficou de fora: {sobrando}')
