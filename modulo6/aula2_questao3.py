from random import randint
from collections import Counter

# Inicialização das listas
lista1, lista2 = [], []

# Preenchendo as listas com 20 valores inteiros aleatórios entre 0 e 50
for i in range(20):
    lista1.append(randint(0, 50))
    lista2.append(randint(0, 50))

# Encontrando a interseção entre as duas listas sem duplicatas
interseccao = sorted(set(lista1) & set(lista2))

# Contagem de vezes que cada elemento aparece em cada lista
contagemLista1 = Counter(lista1)
contagemLista2 = Counter(lista2)

# Impressão dos resultados
print(f"lista1 - {lista1}")
print(f"lista2 - {lista2}")
print(f"Interseccao - {interseccao}")
print("Contagem")

for item in interseccao:
    print(f"O numero {item} aparece {contagemLista1[item]} vez(es) na lista 1 e {contagemLista2[item]} vez(es) na lista 2)")
