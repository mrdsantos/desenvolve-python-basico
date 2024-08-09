from datetime import datetime

# Obtém a data e hora atuais
agora = datetime.now()

# Formata e imprime a data e hora
print(f"Data: {agora.day:02}/{agora.month:02}/{agora.year}")
print(f"Hora: {agora.hour:02}:{agora.minute:02}")