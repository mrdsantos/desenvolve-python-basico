import random
import math

# Solicita ao usuário o número de valores a serem gerados
n = int(input("Digite o número de valores a serem gerados: "))

# Gera uma lista com n valores aleatórios entre 0 e 100
valores = [random.randint(0, 100) for _ in range(n)]

# Calcula a soma dos valores gerados
soma = sum(valores)

# Calcula a raiz quadrada da soma dos valores
raiz_quadrada = math.sqrt(soma)

# Exibe os valores gerados e o resultado
print("Valores gerados:", valores)
print("Soma dos valores:", soma)
print(f"Raiz quadrada da soma: {raiz_quadrada:.2f}")