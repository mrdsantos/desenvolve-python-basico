# Lê o valor em reais
valor = int(input("Quantia em reais: "))

# Calcula a quantidade de notas de 100
notas100 = valor // 100
valor %= 100

# Calcula a quantidade de notas de 50
notas50 = valor // 50
valor %= 50

# Calcula a quantidade de notas de 20
notas20 = valor // 20
valor %= 20

# Calcula a quantidade de notas de 10
notas10 = valor // 10
valor %= 10

# Calcula a quantidade de notas de 5
notas5 = valor // 5
valor %= 5

# Calcula a quantidade de notas de 2
notas2 = valor // 2
valor %= 2

# Calcula a quantidade de notas de 1
notas1 = valor // 1

# Imprime a quantidade de notas de cada valor
print(f"{notas100} nota(s) de R$100,00")
print(f"{notas50} nota(s) de R$50,00")
print(f"{notas20} nota(s) de R$20,00")
print(f"{notas10} nota(s) de R$10,00")
print(f"{notas5} nota(s) de R$5,00")
print(f"{notas2} nota(s) de R$2,00")
print(f"{notas1} nota(s) de R$1,00")
