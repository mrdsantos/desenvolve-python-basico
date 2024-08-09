# Solicita ao usuário para inserir dois números decimais
numero1 = float(input("Digite o primeiro número decimal: "))
numero2 = float(input("Digite o segundo número decimal: "))

# Calcula a diferença absoluta entre os dois números
diferenca = abs(numero1 - numero2)

# Arredonda o resultado para duas casas decimais
diferenca_arredondada = round(diferenca, 2)

# Exibe o resultado
print("A diferença absoluta entre os dois números é:", diferenca_arredondada)