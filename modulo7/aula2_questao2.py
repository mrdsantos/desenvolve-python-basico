# Solicita uma frase ao usuário
frase = input("Digite uma frase: ")

# Substitui todas as vogais por "*"
frase_modificada = ''.join('*' if letra in 'aeiouAEIOU' else letra for letra in frase)

# Imprime a frase modificada
print(f"Frase modificada: {frase_modificada}")
