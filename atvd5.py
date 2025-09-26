# Escreva um programa que peça dois números inteiros e imprima
# todos os números inteiros entre eles.
num1 = int(input('Digite um número inteiro: '))
num2 = int(input('Digite o segundo número: '))

if num1 < num2:
    for i in range(num1+1, num2):
        print(i)
elif num1 > num2:
    for i in range(num1+1, num2):
        print(i)
else:
    print('Os dois números são iguais.')
