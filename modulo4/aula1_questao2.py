n = int(input("Digite um valor para n: "))
cont = 0

# o fluxograma pede enquanto n < cont, o que parece errado pois geraria um loop infinito, ao que se propõe o laço deve rodar
# até que o contador alcance n, por isso while n > cont. Ou seria esperado cont < n como numa resolução apresentada de um exercício parecido.
while n > cont:
    cont += 1
    print(cont)

if n == 0:
    print("fim")
