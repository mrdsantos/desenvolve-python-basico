# Lista de URLs
urls = ["www.google.com", "www.gmail.com", "www.github.com", "www.reddit.com", "www.yahoo.com"]

# Extração dos domínios
dominios = [url[4:-4] for url in urls]

# Exibição dos domínios
print("dominios:", dominios)