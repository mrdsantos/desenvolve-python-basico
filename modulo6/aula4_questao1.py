# Lista com todos os números pares entre 20 e 50
numerosPares = [x for x in range(20, 51) if x % 2 == 0]

# Quadrados dos números presentes na lista [1,2,3,4,5,6,7,8,9]
quadradosNumeros = [x**2 for x in [1, 2, 3, 4, 5, 6, 7, 8, 9]]

# Números entre 1 e 100 que são múltiplos de 7
divisiveisPor7 = [x for x in range(1, 101) if x % 7 == 0]

# Verificação da paridade para cada valor em range(0, 30, 3)
verificarParidade = ["par" if x % 2 == 0 else "ímpar" for x in range(0, 30, 3)]

# Exibindo os resultados gerados
print("Números pares entre 20 e 50:", numerosPares)
print("Quadrados da lista [1,2,3,4,5,6,7,8,9]:", quadradosNumeros)
print("Números divisíveis por 7 entre 1 e 100:", divisiveisPor7)
print('Paridade dos números em range(0, 30, 3):', verificarParidade)