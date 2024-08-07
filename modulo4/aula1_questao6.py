# Lê o número de experimentos registrados
numExperimentos = int(input("Digite o número de experimentos: "))

# Inicializa variáveis
totalCobaias = 0
totalSapos = 0
totalRatos = 0
totalCoelhos = 0

# Processa cada experimento
contador = 0
while contador < numExperimentos:
    # Lê a quantidade e o tipo de cobaia
    quantidade = int(input("Digite a quantidade de cobaias: "))
    tipo = input("Digite o tipo de cobaia (S para sapo, R para rato, C para coelho): ").upper()

    # Atualiza o total de cobaias
    totalCobaias += quantidade

    # Atualiza o total de cada tipo de cobaia
    if tipo == 'S':
        totalSapos += quantidade
        print(f"total de sapos: {totalSapos}")
    elif tipo == 'R':
        totalRatos += quantidade
        print(f"total de ratos: {totalRatos}")
    elif tipo == 'C':
        totalCoelhos += quantidade
        print(f"total de coelhos: {totalCoelhos}")

    # Incrementa o contador
    contador += 1

# Calcula os percentuais
percentualSapos = (totalSapos / totalCobaias) * 100
percentualRatos = (totalRatos / totalCobaias) * 100
percentualCoelhos = (totalCoelhos / totalCobaias) * 100

# Imprime os resultados
print(f"Total de cobaias: {totalCobaias}")
print(f"Total de sapos: {totalSapos}")
print(f"Total de ratos: {totalRatos}")
print(f"Total de coelhos: {totalCoelhos}")
print(f"Percentual de sapos: {percentualSapos:.2f}%")
print(f"Percentual de ratos: {percentualRatos:.2f}%")
print(f"Percentual de coelhos: {percentualCoelhos:.2f}%")
