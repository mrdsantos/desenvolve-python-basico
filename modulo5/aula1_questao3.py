import random

# Gera um número aleatório entre 1 e 10
numeroAleatorio = random.randint(1, 10)

# Loop de jogo até o usuário acertar o número
while True:
    # Solicita ao usuário um palpite
    palpite = int(input("Tente adivinhar o número entre 1 e 10: "))

    # Verifica se o palpite está correto
    if palpite == numeroAleatorio:
        print("Parabéns! Você acertou!")
        break  # Encerra o loop se o palpite estiver correto
    elif palpite < numeroAleatorio:
        print("O palpite é baixo, tente novamente!")
    else:
        print("O palpite é alto, tente novamente!")