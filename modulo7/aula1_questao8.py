# Solicita ao usuário que insira o CPF
cpf = input("Digite o CPF na forma XXX.XXX.XXX-XX: ")

# Função que calcula o primeiro dígito verificador do CPF
def calcular_primeiro_digito(cpf):
    multiplicador = list(range(10, 1, -1))  # Multiplicadores de 10 a 2
    soma = sum(int(digito) * multiplicador[i] for i, digito in enumerate(cpf[:9]))
    resto = soma % 11
    primeiroDigito = 0 if resto < 2 else 11 - resto
    return primeiroDigito

# Função que calcula o segundo dígito verificador do CPF
def calcular_segundo_digito(cpf):
    comPrimeiroDigitoCPF = cpf[:9] + str(calcular_primeiro_digito(cpf))
    multiplicador = list(range(11, 1, -1))
    soma = sum(int(digito) * multiplicador[i] for i, digito in enumerate(comPrimeiroDigitoCPF))
    resto = soma % 11
    segundoDigito = 0 if resto < 2 else 11 - resto
    return segundoDigito

# Função que verifica se o CPF é válido
def validar_cpf(cpf):
    cpf = cpf.replace(".", "").replace("-", "")  # Remove pontos e traços
    if len(cpf) != 11 or not cpf.isdigit():
        return False
    primeiroDigito = str(calcular_primeiro_digito(cpf))
    segundoDigito = str(calcular_segundo_digito(cpf))
    return cpf[-2:] == primeiroDigito + segundoDigito

print(f"CPF {'Válido' if validar_cpf(cpf) else 'Inválido'}")