from collections import Counter

def encontrar_anagramas(frase, palavra_objetivo):
    # Função para verificar se duas palavras são anagramas
    def sao_anagramas(palavra1, palavra2):
        return Counter(palavra1) == Counter(palavra2)

    # Divide a frase em palavras e normaliza todas para minúsculas
    palavras = frase.lower().split()

    # Encontra todos os anagramas da palavra objetivo
    anagramas = [palavra for palavra in palavras if sao_anagramas(palavra, palavra_objetivo.lower())]

    return anagramas

# Solicita ao usuário que insira uma frase
frase = input("Digite uma frase: ")

# Solicita ao usuário que insira a palavra objetivo
palavra_objetivo = input("Digite a palavra objetivo: ")

# Encontra e exibe os anagramas
anagramas = encontrar_anagramas(frase, palavra_objetivo)
print(f"Anagramas: {anagramas}")