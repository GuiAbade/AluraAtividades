num1 = int(input("Digite um numero inteiro de 1 a 10: "))
num2 = int(input("Digite um numero inteiro de 1 a 10: "))


def tabuada(numero: int):
    print(f'Tabuada do numero {numero}')
    for i in range(11):
        resultado = numero * i
        print(f"{numero} x {i} = resultado")


tabuada(num1)
tabuada(num2)
