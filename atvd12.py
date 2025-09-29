# Dados de gastos
gastos = [2172.54, 3701.35, 3518.09, 3456.61, 3249.38,
          2840.82, 3891.45, 3075.26, 2317.64, 3219.08]

contador_acima_3000 = 0

for gasto in gastos:
    if gasto > 3000:
        contador_acima_3000 += 1

quantidade_compras = len(gastos)

porcentagem_acima_3000 = 100*(contador_acima_3000)/quantidade_compras

print(f'{contador_acima_3000} compras foram acima de R$3000,00.')
print(f'{porcentagem_acima_3000}% dos gastos foram acima de R$3000,00.')
