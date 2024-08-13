import random

def embaralhar_palavras(frase):
    def embaralhar_palavra(palavra):
        if len(palavra) <= 3:
            return palavra  # Retorna a palavra original se tiver 3 ou menos caracteres
        
        meio = list(palavra[1:-1])  # Pega os caracteres internos
        random.shuffle(meio)  # Embaralha os caracteres internos
        return palavra[0] + ''.join(meio) + palavra[-1]  # Reconstrói a palavra

    palavras = frase.split()  # Separa a frase em palavras
    palavras_embaralhadas = [embaralhar_palavra(p) for p in palavras]  # Embaralha cada palavra
    return ' '.join(palavras_embaralhadas)  # Junta as palavras de volta em uma frase

# Exemplo de uso
frase = "Python é uma linguagem de programação"
resultado = embaralhar_palavras(frase)
print(resultado)
# Possível saída: "Ptohyn é uma lignaugem de prarmoagãço"
