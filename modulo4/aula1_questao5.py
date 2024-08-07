# Lê o número de respondentes
n = int(input("Digite a quantidade de respondentes: "))

# Inicializa variáveis
soma_idades = 0
contador = 0

# Lê as idades e calcula a soma usando while
while contador < n:
    idade = int(input("Digite a idade do respondente: "))
    soma_idades += idade
    contador += 1

# Calcula a média das idades
media_idades = soma_idades / n

# Imprime a média
print("A média das idades é:", media_idades)