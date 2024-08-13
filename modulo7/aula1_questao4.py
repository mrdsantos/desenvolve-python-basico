# Solicita ao usuário que insira o número de celular
numeroCelular = input("Digite o número do celular: ")

# Verifica o comprimento do número
if len(numeroCelular) == 8:
    # Adiciona o dígito 9 na frente
    numeroCelular = "9" + numeroCelular
elif len(numeroCelular) == 9:
    # Verifica se o primeiro dígito é 9
    if numeroCelular[0] != "9":
        print("Número inválido. Um número com 9 dígitos deve começar com 9.")
        exit()

# Adiciona o separador "-" e imprime o número formatado
numeroFormatado = f"{numeroCelular[:5]}-{numeroCelular[5:]}"
print(f"Número formatado: {numeroFormatado}")