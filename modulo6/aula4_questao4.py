# Listas de alunos e suas respectivas notas
alunos = ["Maria", "Jose", "Carla", "Sol"]
notas = [35, 50, 20, 80]

# Construção da lista de aprovados utilizando compreensão de listas
aprovados = [alunos[i] for i in range(len(notas)) if notas[i] >= 60]

# Exibindo a lista de aprovados
print(aprovados)