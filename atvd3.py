# Coletamos a letra da pessoa usuária como minúscula

letra = input('Digite uma letra. ').lower()
vogais = 'aeiou'

if letra in vogais:
    print('A letra é uma vogal.')
else:
    print('A letra é uma consoante.')
