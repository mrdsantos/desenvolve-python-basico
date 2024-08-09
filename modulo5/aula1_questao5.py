import emoji

# Lista de emojis disponíveis
emojis = {
    "❤️": ":red_heart:",
    "👍": ":thumbs_up:",
    "🤔": ":thinking_face:",
    "🥳": ":partying_face:"
}

# Exibe os emojis disponíveis
print("Emojis disponíveis:")
for symbol, code in emojis.items():
    print(f"{symbol} - {code}")

# Solicita uma frase codificada ao usuário
frase_codificada = input("Digite uma frase e ela será emojizada:\n")

# Converte a frase codificada em emojis
frase_emojizada = emoji.emojize(frase_codificada)

# Exibe a frase com emojis
print("Frase emojizada:")
print(frase_emojizada)