import random

# Gere aleatoriamente 20 valores inteiros entre -100 e 100 e os armazene em uma lista
numerosLista = []
for i in range(20):
    valor = random.randint(-100, 100)
    numerosLista.append(valor)

print(f"Lista ordenada: {sorted(numerosLista)}")
print(f"Lista original: {numerosLista}")
print(f"O índice de maior valor da lista é {numerosLista.index(max(numerosLista))}")
print(f"O índice de menor valor da lista é {numerosLista.index(min(numerosLista))}")