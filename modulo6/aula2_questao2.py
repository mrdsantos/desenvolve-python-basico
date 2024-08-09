import random

num_elementos = random.randint(5, 20)
elementos = []

for i in range(num_elementos):
    elementos.append(random.randint(1,10))

print(elementos)
print(f"A soma dos valores da lista é: {sum(elementos)}")
print(f"A média dos valores da lista elementos é: {(sum(elementos) / num_elementos):.2f}")