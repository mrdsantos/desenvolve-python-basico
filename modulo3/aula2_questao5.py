# Solicita o gênero do usuário
genero = input("Digite seu gênero (M ou F): ").upper()

# Solicita a idade do usuário
idade = int(input("Digite sua idade: "))

# Solicita o tempo de serviço em anos
tempoServico = int(input("Digite seu tempo de serviço em anos: "))

# Verifica se a pessoa pode se aposentar
podeAposentar = (
    (genero == "F" and idade > 60) or
    (genero == "M" and idade > 65) or
    (tempoServico >= 30) or
    (idade == 60 and tempoServico >= 25)
)

# Imprime o resultado
print(podeAposentar)