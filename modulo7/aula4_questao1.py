import os

# Solicita uma frase ao usuário
frase = input("Digite uma frase: ")

# Define o nome do arquivo
nomeAquivo = "frase.txt"

# Abre o arquivo para escrita e salva a frase
with open(nomeAquivo, 'w') as arquivo:
    arquivo.write(frase)

# Obtém o caminho absoluto do arquivo
caminhoArquivo = os.path.abspath(nomeAquivo)

# Imprime o caminho completo do arquivo salvo
print(f"Frase salva em {caminhoArquivo}")