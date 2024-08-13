import random

def encrypt(lista_nomes):
    # Gera uma chave aleatória entre 1 e 10
    chave_aleatoria = random.randint(1, 10)

    def criptografar_caractere(c, chave):
        # Obtém o código Unicode do caractere e aplica a criptografia
        novo_codigo = ord(c) + chave
        # Garante que o novo código esteja no intervalo visível (33 a 126)
        if novo_codigo > 126:
            novo_codigo = 33 + (novo_codigo - 127)
        return chr(novo_codigo)

    def criptografar_nome(nome, chave):
        # Aplica a criptografia a cada caractere do nome
        return ''.join(criptografar_caractere(c, chave) for c in nome)

    # Criptografa todos os nomes na lista usando a chave aleatória
    nomes_criptografados = [criptografar_nome(nome, chave_aleatoria) for nome in lista_nomes]

    return nomes_criptografados, chave_aleatoria

# Lista de nomes a serem criptografados
nomes = ["Luana", "Ju", "Davi", "Vivi", "Pri", "Luiz"]

# Criptografa os nomes e obtém a chave
nomes_criptografados, chave = encrypt(nomes)

print(f"Chave de criptografia: {chave}")
print(f"Nomes criptografados: {nomes_criptografados}")