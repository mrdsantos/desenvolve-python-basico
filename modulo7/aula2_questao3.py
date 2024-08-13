def verificar_palindromo(frase):
    # Remove espaços e sinais de pontuação, e converte para minúsculas
    frase_limpa = ''.join(char.lower() for char in frase if char.isalnum())
    # Verifica se a frase é um palíndromo
    return frase_limpa == frase_limpa[::-1]

while True:
    entrada = input('Digite uma frase (digite "fim" para encerrar): ')
    if entrada.lower() == "fim":
        break
    if verificar_palindromo(entrada):
        print(f'"{entrada}" é palíndromo')
    else:
        print(f'"{entrada}" não é palíndromo')