# Solicita ao usuário que insira uma frase
frase = input("Digite uma frase: ")

# Conta o número de espaços em branco na frase
contagemEspacos = frase.count(' ')

# Exibe o resultado
print(f"A frase contém {contagemEspacos} espaços em branco.")