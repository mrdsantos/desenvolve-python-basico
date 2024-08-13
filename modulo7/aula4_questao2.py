import re

# Define os nomes dos arquivos
arquivo_entrada = "frase.txt"
arquivo_saida = "palavras.txt"

# Lê o conteúdo do arquivo de entrada
with open(arquivo_entrada, 'r') as arquivo:
    frase = arquivo.read()

# Remove espaços em branco e caracteres não alfabéticos, e separa as palavras
palavras = re.findall(r'[a-zA-Z0-9]+', frase)

# Salva as palavras no novo arquivo
with open(arquivo_saida, 'w') as arquivo:
    for palavra in palavras:
        arquivo.write(palavra + '\n')

# Lê e imprime o conteúdo do arquivo de saída
with open(arquivo_saida, 'r') as arquivo:
    conteudo = arquivo.read()

print(conteudo)