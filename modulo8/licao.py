from collections import Counter
import re


def contar_palavras(arquivo):
    # Abrir e ler o conteúdo do arquivo
    with open(arquivo, "r", encoding="ISO-8859-1") as file:
        texto = file.read()

    # Utilizar expressão regular para encontrar todas as palavras
    palavras = re.findall(r"\b\w+\b", texto.lower())

    # Contar a frequência das palavras
    contagem_palavras = Counter(palavras)

    # Ordenar o dicionário por valores de forma decrescente
    dicionario_ordenado = dict(
        sorted(contagem_palavras.items(), key=lambda item: item[1], reverse=True)
    )

    return dicionario_ordenado


# Nome do arquivo
arquivo = "estomago.txt"

# Contar palavras e obter o dicionário ordenado
dicionario_ordenado = contar_palavras(arquivo)

# Imprimir o dicionário ordenado
print(dicionario_ordenado)
