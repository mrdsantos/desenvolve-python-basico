# Solicita a idade do participante
age = int(input("Digite sua idade: "))

# Solicita se o participante já jogou pelo menos 3 jogos de tabuleiro
playedThreeGames = input("Já jogou pelo menos 3 jogos de tabuleiro? (True/False): ") == "true" or "True"

# Solicita a quantidade de vezes que o participante venceu um jogo
hasWon = int(input("Quantas vezes venceu um jogo? "))

# Verifica se o participante atende aos critérios para ingresso no clube
podeIngressarNoClube = (16 <= age <= 18) and playedThreeGames and (hasWon >= 1)

# Imprime o resultado
print(podeIngressarNoClube)