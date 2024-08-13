# Solicita a data de nascimento ao usuário
data = input("Digite a data de nascimento (dd/mm/aaaa): ")

# Lista dos nomes dos meses
meses = [
    "Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho",
    "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"
]

# Separa o dia, mês e ano da data informada
dia, mes, ano = map(int, data.split('/'))

# Formata e imprime a data com o nome do mês por extenso
print(f"Você nasceu em {dia} de {meses[mes-1]} de {ano}.")