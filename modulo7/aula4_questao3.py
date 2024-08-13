import re

# Abre o arquivo para leitura
with open("estomago.txt", "r", encoding="ISO-8859-1") as file:
    linhas = file.readlines()

# 1. O texto das primeiras 25 linhas
primeiras25Linhas = ''.join(linhas[:25])
print("Texto das primeiras 25 linhas:")
print(primeiras25Linhas)

# 2. O número de linhas do arquivo
numeroLinhas = len(linhas)
print(f"Número de linhas do arquivo: {numeroLinhas}")

# 3. A linha com maior número de caracteres
linhaMaiorCaracteres = max(linhas, key=len).strip()
print(f"Linha com maior número de caracteres: {linhaMaiorCaracteres}")

# 4. O número de menções aos nomes dos personagens "Nonato" e "Íria"
textoCompleto = ''.join(linhas)
mencoesNonato = len(re.findall(r'\bNonato\b', textoCompleto, re.IGNORECASE))
mencoesIria = len(re.findall(r'\bÍria\b', textoCompleto, re.IGNORECASE))

print(f"Número de menções ao nome 'Nonato': {mencoesNonato}")
print(f"Número de menções ao nome 'Íria': {mencoesIria}")
