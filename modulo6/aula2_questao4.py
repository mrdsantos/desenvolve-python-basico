# Criando as listas
list1, list2 = [], []
# Recebendo a quantidade de elementos da lista 1
elemCountList1 = int(input('Digite a quantidade de elementos da lista 1: '))
elemCountList2 = int(input('Digite a quantidade de elementos da lista 2: '))

for i in range(elemCountList1):
    list1.append(int(input('Digite o elemento da lista 1: ')))

for i in range(elemCountList2):
    list2.append(int(input('Digite o elemento da lista 2: ')))

# Criando a lista intercalada
list3 = []
for i in range(max(elemCountList1, elemCountList2)):
    if i < elemCountList1:
        list3.append(list1[i])
    if i < elemCountList2:
        list3.append(list2[i])

print(f'Lista intercalada: {list3}')