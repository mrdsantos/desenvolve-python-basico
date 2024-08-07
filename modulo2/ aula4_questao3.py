# Recebe as informações do produto 1
nomeProduto1 = input("Digite o nome do produto: ")
precoUnitario1 = float(input("Digite o preço unitário do produto: "))
quantidade1 = int(input("Digite a quantidade do produto: "))

# Recebe as informações do produto 2
nomeProduto2 = input("Digite o nome do produto: ")
precoUnitario2 = float(input("Digite o preço unitário do produto: "))
quantidade2 = int(input("Digite a quantidade do produto: "))

# Recebe as informações do produto 3
nomeProduto3 = input("Digite o nome do produto: ")
precoUnitario3 = float(input("Digite o preço unitário do produto: "))
quantidade3 = int(input("Digite a quantidade do produto: "))

# Calcula o preço total da compra
total = (precoUnitario1 * quantidade1) + (precoUnitario2 * quantidade2) + (precoUnitario3 * quantidade3)

# Imprime o total com formatação
print(f"Total: R${total:,.2f}")