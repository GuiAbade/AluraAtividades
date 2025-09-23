"""Alura Data Science"""

numero1 = float(input('Informe o primeiro número '))
numero2 = float(input('Informe o segundo número '))

if numero1 > numero2:
    print(f'O primeiro numero informado é maior - {numero1}')
elif numero2 > numero1:
    print(f' O segundo número informado é maior - {numero2}')
else:
    print(f'Os números são iguais {numero1}')
