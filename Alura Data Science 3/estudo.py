from random import choices

frutas_disponiveis = []
frutas = int(input("Digite a quantidade de frutas: "))

for i in range(frutas):
    valor = input(f"Digite o nome da {i+1}ª fruta: ")
    frutas_disponiveis.append(valor)

salada = choices(frutas_disponiveis, k=2)

print(f"Frutas disponiveis:", frutas_disponiveis)

print(f'Você vai usar {salada} para sua salada!')
