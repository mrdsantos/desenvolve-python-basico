# Recebe do comprimento do terreno
comprimento = int(input("Digite o comprimento do terreno em metros: "))

# Recebe da largura do terreno
largura = int(input("Digite a largura do terreno em metros: "))

# Recebe do preço do metro quadrado
preco_m2 = float(input("Digite o preço do metro quadrado: "))

# Calcula a área do terreno em metros quadrados
area_m2 = comprimento * largura

# Calcula o valor total do terreno
preco_total = preco_m2 * area_m2

# Retorna o valor total do terreno
print ("O terreno possui", area_m2, "m² e custa R$", preco_total, ".")