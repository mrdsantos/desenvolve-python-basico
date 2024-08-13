import csv

# Lista de livros com título, autor, ano de publicação e número de páginas
livros = [
    ["Moby Dick", "Herman Melville", "1851", "635"],
    ["O Grande Gatsby", "F. Scott Fitzgerald", "1925", "180"],
    ["A Arte da Guerra", "Sun Tzu", "5 a.C.", "272"],
    ["O Sol é para Todos", "Harper Lee", "1960", "281"],
    ["O Nome do Vento", "Patrick Rothfuss", "2007", "662"],
    ["A Menina que Roubava Livros", "Markus Zusak", "2005", "552"],
    ["O Hobbit", "J.R.R. Tolkien", "1937", "310"],
    ["O Código Da Vinci", "Dan Brown", "2003", "454"],
    ["A Coisa", "Stephen King", "1986", "1138"],
    ["A Esperança", "Suzanne Collins", "2010", "391"]
]

# Nome do arquivo CSV
nome_arquivo = 'meus_livros.csv'

# Abre o arquivo para escrita
with open(nome_arquivo, mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    
    # Escreve o cabeçalho
    writer.writerow(["Título", "Autor", "Ano de publicação", "Número de páginas"])
    
    # Escreve as linhas com as informações dos livros
    writer.writerows(livros)

print(f'Arquivo "{nome_arquivo}" criado com sucesso!')