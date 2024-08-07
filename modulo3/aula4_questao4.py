# Recebe a distância e o peso do pacote ao usuário
distancia = float(input("Digite a distância da entrega em quilômetros: "))
peso = float(input("Digite o peso do pacote em quilogramas: "))

# Frete calculado pela distância
if distancia <= 100:
    valorFrete = peso * 1
elif 101 <= distancia <= 300:
    valorFrete = peso * 1.50
else:
    valorFrete = peso * 2

# Taxa sobre pacotes com peso superior a 10 kg
if peso > 10:
    valorFrete += 10

# Retorna o valor do frete
print(f"O valor do frete é R${valorFrete:.2f}")