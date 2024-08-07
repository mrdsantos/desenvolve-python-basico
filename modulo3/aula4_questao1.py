# Solicita dois números ao usuário
numero1, numero2 = int(input("Digite o primeiro número: ")), int(input("Digite o segundo número: "))

# Verifica se a soma é par ou ímpar
# if (numero1 + numero2) % 2 == 0:
#     print("A soma é par.")
# else:
#     print("A soma é ímpar.")

#retorna se é par ou impar
print ( "É par" if (numero1 + numero2) %2 == 0 else "É impar")