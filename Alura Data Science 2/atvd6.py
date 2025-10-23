# Escreva um programa para calcular quantos dias levará para a
# colônia de uma bactéria A ultrapassar ou igualar a colônia
# de uma bactéria B, com base nas taxas de crescimento de 3%
# e 1,5% respectivamente. Considere que a colônia A inicia
# com 4 elementos e a B com 10.
colonia_a = 4
colonia_b = 10

taxa_a = 0.03
taxa_b = 0.015

dias = 0

while colonia_a <= colonia_b:
    colonia_a *= 1 + taxa_a
    colonia_b *= 1 + taxa_b
    dias += 1

print(f'Irá levar {dias} para a colonia A ultrapassar a colonia B')
