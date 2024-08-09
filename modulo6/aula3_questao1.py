# Coleta de números do usuário
numeros = []
print("Digite pelo menos 4 números inteiros (digite 'sair' para finalizar):")

while True:
    entrada = input("Digite um número inteiro: ")
    if entrada.lower() == 'sair' and len(numeros) >= 4:
        print("Programa encerrado")
        break
    else:
        numero = int(entrada)
        numeros.append(numero)

# Fatiamento e exibição das listas
print(f"Lista original: {numeros}")
print(f"Os 3 primeiros elementos: {numeros[:3]}")
print(f"Os 2 últimos elementos: {numeros[-2:]}")
print(f"Lista invertida: {numeros[::-1]}")
print(f"Elementos de índice par: {numeros[::2]}")
print(f"Elementos de índice ímpar: {numeros[1::2]}")