# Solicita a classe do personagem
classCharacter = input("Escolha a classe (guerreiro, mago ou arqueiro): ").lower()

# Solicita os pontos de força e magia
strength = int(input("Digite os pontos de força (de 1 a 20): "))
intelligence = int(input("Digite os pontos de magia (de 1 a 20): "))

# Verifica se os pontos de atributo são consistentes com a classe escolhida
if classCharacter == "guerreiro":
    atributosConsistentes = (strength >= 15) and (intelligence <= 10)
elif classCharacter == "mago":
    atributosConsistentes = (strength <= 10) and (intelligence >= 15)
elif classCharacter == "arqueiro":
    atributosConsistentes = (strength > 5 and strength <= 15) and (intelligence > 5 and intelligence <= 15)
else:
    atributosConsistentes = False

# Imprime o resultado
print("Pontos de atributo consistentes com a classe escolhida:", atributosConsistentes)