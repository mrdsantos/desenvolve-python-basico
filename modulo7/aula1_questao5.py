# Solicita ao usuário que insira uma frase
frase = input("Digite uma frase: ")

# Lista de vogais
vogais = "aeiou"

# Inicializa uma lista para armazenar os índices das vogais
indicesVogais = []

# Contador de vogais
contadorVogais = 0

# Itera sobre cada caractere da frase e seus índices
for indice, letra in enumerate(frase):
    if letra.lower() in vogais:
        indicesVogais.append(indice)
        contadorVogais += 1

# Exibe o número de vogais e os índices
print(f"Quantidade de vogais na frase: {contadorVogais}")
print(f"Índices das vogais: {indicesVogais}")
