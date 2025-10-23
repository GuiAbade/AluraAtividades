# Coleta do percentual

variacao = float(input('Digite o percentual de crescimento da empresa: '))

if variacao > 0:
    print(f'Houve um crescimento de {variacao}%')
elif variacao < 0:
    print(f'Houve uma variação de decrescimento de {variacao}%')
else:
    print('Não houve crescimento ou decrescimento.')
