# Solicita o nome do usuário
nome = input("Digite seu nome: ")

# Imprime o nome em forma de escada
for i in range(len(nome)):
    print(nome[:i+1])