# Lista de horas trabalhadas por cada funcionário
horasTrabalhadas = [40, 37, 45, 40, 40, 48]

# Valores fixos de ganho por hora regular e hora extra
ganhoPorHora = 20
horaExtra = 25

# Construção da lista de pagamentos utilizando compreensão de listas
pagamentos = [
    ganhoPorHora * min(hora, 40) + horaExtra * max(0, hora - 40)
    for hora in horasTrabalhadas
]

# Exibindo a lista de pagamentos
print(pagamentos)