from random import randint

# Gera uma lista de 20 elementos aleatórios entre -10 e 10
lista = [randint(-10, 10) for _ in range(20)]

# Exibe a lista original
print("Original:", lista)

# Função para encontrar o intervalo com a maior quantidade de números negativos
def intervalo_max_negativos(lista):
    maxNegativos = 0
    countNegativosAtual = 0
    inicioIntervalo = 0
    inicioMelhorIntervalo = 0
    fimMelhorIntervalo = 0

    for i in range(len(lista)):
        if lista[i] < 0:
            countNegativosAtual += 1
        else:
            countNegativosAtual = 0
            inicioIntervalo = i + 1

        if countNegativosAtual > maxNegativos:
            maxNegativos = countNegativosAtual
            inicioMelhorIntervalo = inicioIntervalo
            fimMelhorIntervalo = i + 1

    return inicioMelhorIntervalo, fimMelhorIntervalo

# Encontrar o intervalo com a maior quantidade de números negativos
inicio, fim = intervalo_max_negativos(lista)

# Deleta o intervalo encontrado
del lista[inicio:fim]

# Exibe a lista após a deleção
print("Editada:", lista)