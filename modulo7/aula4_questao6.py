import pandas as pd

# Carregar o arquivo CSV
dataFrame = pd.read_csv('spotify-2023.csv', encoding='latin-1')

# Filtrar as músicas dentro do intervalo de anos desejado
filteredDataFrame = dataFrame[(dataFrame['released_year'] >= 2012) & (dataFrame['released_year'] <= 2022)].copy()

# Certificar-se de que as colunas necessárias estão presentes e converter os tipos
filteredDataFrame.loc[:, 'released_year'] = pd.to_numeric(filteredDataFrame['released_year'])
filteredDataFrame.loc[:, 'streams'] = pd.to_numeric(filteredDataFrame['streams'])

# Verificar e ignorar linhas com dados ausentes ou inválidos
filteredDataFrame = filteredDataFrame.dropna(subset=['released_year', 'streams'])

# Encontrar a música mais tocada de cada ano
result = filteredDataFrame.loc[filteredDataFrame.groupby('released_year')['streams'].idxmax()]

# Selecionar apenas as colunas necessárias
result = result[['track_name', 'artist(s)_name', 'released_year', 'streams']]

# Garantir que a lista contenha apenas 10 anos únicos
result = result[result['released_year'].between(2012, 2022)]
result = result.drop_duplicates(subset=['released_year'])
result = result.sort_values(by='released_year').head(10)

# Converter o DataFrame para uma lista de listas
resultList = result.values.tolist()

# Imprimir cada índice e o respectivo resultado em uma linha separada
for index, item in enumerate(resultList):
    print(f"Posição {index+1}: {item}")