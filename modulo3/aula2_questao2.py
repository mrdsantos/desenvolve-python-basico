#Recebe a idade de Juliana
ageJuliana = int(input("Qual é a idade de Juliana?"))
#Recebe a idade de Cris
ageCris = int(input("Qual é a idade de Cris?"))
#Valida a expressão se ambos valores forem maiores que 17
allowEnter = ageJuliana > 17 or ageCris > 17
#Retorno
print(allowEnter)