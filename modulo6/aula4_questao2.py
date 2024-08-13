# Solicita ao usuário que digite uma frase
frase = input("Digite uma frase: ")

# Lista de vogais presentes na frase, ordenadas alfabeticamente
vogaisOrdenadas = sorted([letra for letra in frase if letra.lower() in 'aeiou'])

# Lista de consoantes presentes na frase
consoantes = [letra for letra in frase if letra.lower() in 'bcdfghjklmnpqrstvwxyz']

# Exibindo os resultados
print("Vogais:", vogaisOrdenadas)
print("Consoantes:", consoantes)