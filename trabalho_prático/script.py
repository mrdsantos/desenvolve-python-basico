import pandas as pd

# Variável global para total de vendas
totalDeVendas = 0

# Função para carregar dados de usuários
def carregar_usuarios(nomeArquivo):
    """
    Carrega os dados de usuários a partir de um arquivo CSV.
    
    Args:
        nomeArquivo (str): Nome do arquivo CSV contendo os dados dos usuários.
        
    Returns:
        pd.DataFrame: DataFrame com os dados dos usuários.
    """
    return pd.read_csv(nomeArquivo)

# Função para carregar dados de produtos
def carregar_produtos(nomeArquivo):
    """
    Carrega os dados de produtos a partir de um arquivo CSV.
    
    Args:
        nomeArquivo (str): Nome do arquivo CSV contendo os dados dos produtos.
        
    Returns:
        pd.DataFrame: DataFrame com os dados dos produtos.
    """
    return pd.read_csv(nomeArquivo)

# Função para salvar dados de usuários
def salvar_usuarios(dataFrame, nomeArquivo):
    """
    Salva os dados de usuários em um arquivo CSV.
    
    Args:
        dataFrame (pd.DataFrame): DataFrame contendo os dados dos usuários.
        nomeArquivo (str): Nome do arquivo CSV onde os dados serão salvos.
    """
    dataFrame.to_csv(nomeArquivo, index=False)

# Função para salvar dados de produtos
def salvar_produtos(dataFrame, nomeArquivo):
    """
    Salva os dados de produtos em um arquivo CSV.
    
    Args:
        dataFrame (pd.DataFrame): DataFrame contendo os dados dos produtos.
        nomeArquivo (str): Nome do arquivo CSV onde os dados serão salvos.
    """
    dataFrame.to_csv(nomeArquivo, index=False)

# Função para cadastrar novo produto
def cadastrar_produto(dataFrame, nome, preco, quantidade):
    """
    Cadastra um novo produto no DataFrame.
    
    Args:
        dataFrame (pd.DataFrame): DataFrame contendo os dados dos produtos.
        nome (str): Nome do produto.
        preco (float): Preço do produto.
        quantidade (int): Quantidade do produto.
        
    Returns:
        pd.DataFrame: DataFrame atualizado com o novo produto.
        str: Mensagem de sucesso.
    """
    novoProduto = pd.DataFrame([[nome.lower(), preco, quantidade]], columns=['nome', 'preco', 'quantidade'])
    dataFrameAtualizado = pd.concat([dataFrame, novoProduto], ignore_index=True)
    return dataFrameAtualizado, "Produto cadastrado com sucesso!"

# Função para editar produto existente
def editar_produto(dataFrame, nome, preco=None, quantidade=None):
    """
    Edita um produto existente no DataFrame.
    
    Args:
        dataFrame (pd.DataFrame): DataFrame contendo os dados dos produtos.
        nome (str): Nome do produto a ser editado.
        preco (float, optional): Novo preço do produto. Se não fornecido, o preço não será alterado.
        quantidade (int, optional): Nova quantidade do produto. Se não fornecido, a quantidade não será alterada.
        
    Returns:
        pd.DataFrame: DataFrame atualizado com as modificações.
        str: Mensagem de sucesso ou erro.
    """
    indiceProduto = dataFrame[dataFrame['nome'] == nome.lower()].index
    if not indiceProduto.empty:
        if preco is not None:
            dataFrame.at[indiceProduto[0], 'preco'] = preco
        if quantidade is not None:
            dataFrame.at[indiceProduto[0], 'quantidade'] = quantidade
        return dataFrame, "Produto editado com sucesso!"
    else:
        return dataFrame, "Produto não encontrado!"

# Função para deletar produto
def deletar_produto(dataFrame, nome):
    """
    Deleta um produto do DataFrame.
    
    Args:
        dataFrame (pd.DataFrame): DataFrame contendo os dados dos produtos.
        nome (str): Nome do produto a ser deletado.
        
    Returns:
        pd.DataFrame: DataFrame atualizado sem o produto deletado.
        str: Mensagem de sucesso ou erro.
    """
    if nome.lower() in dataFrame['nome'].values:
        dataFrameAtualizado = dataFrame[dataFrame['nome'] != nome.lower()]
        return dataFrameAtualizado, "Produto deletado com sucesso!"
    else:
        return dataFrame, "Produto não encontrado!"

# Função para vender produto
def vender_produto(dataFrame, nome, quantidade):
    """
    Realiza a venda de um produto e atualiza o estoque.
    
    Args:
        dataFrame (pd.DataFrame): DataFrame contendo os dados dos produtos.
        nome (str): Nome do produto a ser vendido.
        quantidade (int): Quantidade do produto a ser vendida.
        
    Returns:
        pd.DataFrame: DataFrame atualizado com o estoque modificado.
        str: Mensagem de sucesso com o total de vendas ou erro.
    """
    global totalDeVendas
    indiceProduto = dataFrame[dataFrame['nome'] == nome.lower()].index
    if not indiceProduto.empty:
        if dataFrame.at[indiceProduto[0], 'quantidade'] >= quantidade:
            dataFrame.at[indiceProduto[0], 'quantidade'] -= quantidade
            valorVenda = quantidade * dataFrame.at[indiceProduto[0], 'preco']
            totalDeVendas += valorVenda
            return dataFrame, f"Venda realizada com sucesso! Total: R${valorVenda:.2f}"
        else:
            return dataFrame, "Quantidade insuficiente no estoque!"
    else:
        return dataFrame, "Produto não encontrado!"

# Função para listar produtos ordenados por nome
def listar_produtos_por_nome(dataFrame):
    """
    Lista os produtos ordenados por nome.
    
    Args:
        dataFrame (pd.DataFrame): DataFrame contendo os dados dos produtos.
    """
    dataFrameOrdenado = dataFrame.sort_values(by='nome')
    for _, produto in dataFrameOrdenado.iterrows():
        print(f"Nome: {produto['nome'].title()}, Quantidade: {produto['quantidade']}, Preço: {produto['preco']}")

# Função para listar produtos ordenados por preço
def listar_produtos_por_preco(dataFrame):
    """
    Lista os produtos ordenados por preço.
    
    Args:
        dataFrame (pd.DataFrame): DataFrame contendo os dados dos produtos.
    """
    dataFrameOrdenado = dataFrame.sort_values(by='preco')
    for _, produto in dataFrameOrdenado.iterrows():
        print(f"Nome: {produto['nome'].title()}, Quantidade: {produto['quantidade']}, Preço: {produto['preco']}")

# Função para buscar um produto específico
def buscar_produto(dataFrame, nome):
    """
    Busca e exibe um produto específico.
    
    Args:
        dataFrame (pd.DataFrame): DataFrame contendo os dados dos produtos.
        nome (str): Nome do produto a ser buscado.
    """
    produto = dataFrame[dataFrame['nome'] == nome.lower()]
    if not produto.empty:
        for _, p in produto.iterrows():
            print(f"Nome: {p['nome'].title()}, Quantidade: {p['quantidade']}, Preço: {p['preco']}")
    else:
        print("Produto não encontrado!")

# Função para adicionar novo usuário
def adicionar_usuario(dataFrame, username, password, userType):
    """
    Adiciona um novo usuário ao DataFrame.
    
    Args:
        dataFrame (pd.DataFrame): DataFrame contendo os dados dos usuários.
        username (str): Nome do usuário.
        password (str): Senha do usuário.
        userType (int): Tipo do usuário (1 para Administrador, 0 para Operador).
        
    Returns:
        pd.DataFrame: DataFrame atualizado com o novo usuário.
        str: Mensagem de sucesso.
    """
    novoUsuario = pd.DataFrame([[username, password, userType]], columns=['username', 'password', 'userType'])
    dataFrameAtualizado = pd.concat([dataFrame, novoUsuario], ignore_index=True)
    return dataFrameAtualizado, "Usuário adicionado com sucesso!"

# Função para editar usuário existente
def editar_usuario(dataFrame, username, password=None, userType=None):
    """
    Edita um usuário existente no DataFrame.
    
    Args:
        dataFrame (pd.DataFrame): DataFrame contendo os dados dos usuários.
        username (str): Nome do usuário a ser editado.
        password (str, optional): Nova senha do usuário. Se não fornecido, a senha não será alterada.
        userType (int, optional): Novo tipo do usuário (1 para Administrador, 0 para Operador). Se não fornecido, o tipo não será alterado.
        
    Returns:
        pd.DataFrame: DataFrame atualizado com as modificações.
        str: Mensagem de sucesso ou erro.
    """
    indiceUsuario = dataFrame[dataFrame['username'] == username].index
    if not indiceUsuario.empty:
        if password is not None:
            dataFrame.at[indiceUsuario[0], 'password'] = password
        if userType is not None:
            dataFrame.at[indiceUsuario[0], 'userType'] = userType
        return dataFrame, "Usuário editado com sucesso!"
    else:
        return dataFrame, "Usuário não encontrado!"

# Função para deletar usuário
def deletar_usuario(dataFrame, username):
    """
    Deleta um usuário do DataFrame.
    
    Args:
        dataFrame (pd.DataFrame): DataFrame contendo os dados dos usuários.
        username (str): Nome do usuário a ser deletado.
        
    Returns:
        pd.DataFrame: DataFrame atualizado sem o usuário deletado.
        str: Mensagem de sucesso ou erro.
    """
    if username in dataFrame['username'].values:
        dataFrameAtualizado = dataFrame[dataFrame['username'] != username]
        return dataFrameAtualizado, "Usuário deletado com sucesso!"
    else:
        return dataFrame, "Usuário não encontrado!"

# Função para realizar ações com base no tipo de usuário
def realizar_acao(tipoUsuario, acao, *args):
    """
    Realiza uma ação com base no tipo de usuário e na ação solicitada.
    
    Args:
        tipoUsuario (int): Tipo do usuário (1 para Administrador, 0 para Operador).
        acao (str): Ação a ser realizada.
        *args: Argumentos adicionais necessários para a ação.
    """
    # Carregar dados
    usuarios = carregar_usuarios('usuarios.csv')
    produtos = carregar_produtos('produtos.csv')

    if acao == 'cadastrar_produto' and tipoUsuario == 1:
        produtos, mensagem = cadastrar_produto(produtos, *args)
    elif acao == 'editar_produto' and tipoUsuario == 1:
        produtos, mensagem = editar_produto(produtos, *args)
    elif acao == 'deletar_produto' and tipoUsuario == 1:
        produtos, mensagem = deletar_produto(produtos, *args)
    elif acao == 'vender_produto':
        produtos, mensagem = vender_produto(produtos, *args)
    elif acao == 'adicionar_usuario' and tipoUsuario == 1:
        usuarios, mensagem = adicionar_usuario(usuarios, *args)
    elif acao == 'editar_usuario' and tipoUsuario == 1:
        usuarios, mensagem = editar_usuario(usuarios, *args)
    elif acao == 'deletar_usuario' and tipoUsuario == 1:
        usuarios, mensagem = deletar_usuario(usuarios, *args)
    elif acao == 'listar_por_nome':
        listar_produtos_por_nome(produtos)
        return
    elif acao == 'listar_por_preco':
        listar_produtos_por_preco(produtos)
        return
    elif acao == 'buscar_produto':
        buscar_produto(produtos, *args)
        return
    else:
        print("Ação não permitida ou inválida")
        return

    # Salvar dados
    salvar_usuarios(usuarios, 'usuarios.csv')
    salvar_produtos(produtos, 'produtos.csv')
    
    # Exibir mensagem
    print(mensagem)

# Função para autenticação de usuário
def autenticar_usuario():
    """
    Autentica um usuário com base no nome de usuário e senha.
    
    Returns:
        int: Tipo do usuário (1 para Administrador, 0 para Operador).
    """
    usuarios = carregar_usuarios('usuarios.csv')
    while True:
        username = input("Digite o nome de usuário: ")
        password = input("Digite a senha: ")
        usuario = usuarios[(usuarios['username'] == username) & (usuarios['password'] == password)]
        if not usuario.empty:
            tipoUsuario = usuario.iloc[0]['userType']
            return tipoUsuario
        else:
            print("Credenciais inválidas. Tente novamente.")

# Função para exibir o menu e realizar ações
def exibir_menu():
    """
    Exibe o menu principal e executa ações com base na escolha do usuário.
    """
    global totalDeVendas
    tipoUsuario = autenticar_usuario()
    
    while True:
        print(f"\nTotal de Vendas do Dia: R${totalDeVendas:.2f}")
        print("\nMenu:")
        if tipoUsuario == 1:
            print("1 - Cadastrar produto")
            print("2 - Editar produto")
            print("3 - Deletar produto")
            print("4 - Adicionar usuário")
            print("5 - Editar usuário")
            print("6 - Deletar usuário")
        print("7 - Vender produto")
        print("8 - Listar produtos por nome")
        print("9 - Listar produtos por preço")
        print("10 - Buscar produto")
        print("Digite 'fim' para encerrar")

        opcao = input("Escolha uma opção: ")
        
        if opcao == 'fim':
            break
        
        if tipoUsuario == 1:
            if opcao == '1':
                nome = input("Nome do produto: ")
                preco = float(input("Preço do produto: "))
                quantidade = int(input("Quantidade do produto: "))
                realizar_acao(tipoUsuario, 'cadastrar_produto', nome, preco, quantidade)
            elif opcao == '2':
                nome = input("Nome do produto: ")
                preco = input("Novo preço do produto (deixe em branco se não quiser alterar): ")
                quantidade = input("Nova quantidade do produto (deixe em branco se não quiser alterar): ")
                preco = float(preco) if preco else None
                quantidade = int(quantidade) if quantidade else None
                realizar_acao(tipoUsuario, 'editar_produto', nome, preco, quantidade)
            elif opcao == '3':
                nome = input("Nome do produto: ")
                realizar_acao(tipoUsuario, 'deletar_produto', nome)
            elif opcao == '4':
                username = input("Nome de usuário: ")
                password = input("Senha: ")
                userType = int(input("Tipo de usuário (1 para Administrador, 0 para Operador): "))
                realizar_acao(tipoUsuario, 'adicionar_usuario', username, password, userType)
            elif opcao == '5':
                username = input("Nome de usuário: ")
                password = input("Nova senha (deixe em branco se não quiser alterar): ")
                userType = input("Novo tipo de usuário (1 para Administrador, 0 para Operador - deixe em branco se não quiser alterar): ")
                password = password if password else None
                userType = int(userType) if userType else None
                realizar_acao(tipoUsuario, 'editar_usuario', username, password, userType)
            elif opcao == '6':
                username = input("Nome de usuário: ")
                realizar_acao(tipoUsuario, 'deletar_usuario', username)
        if opcao == '7':
            nome = input("Nome do produto: ")
            quantidade = int(input("Quantidade a vender: "))
            realizar_acao(tipoUsuario, 'vender_produto', nome, quantidade)
        elif opcao == '8':
            realizar_acao(tipoUsuario, 'listar_por_nome')
        elif opcao == '9':
            realizar_acao(tipoUsuario, 'listar_por_preco')
        elif opcao == '10':
            nome = input("Nome do produto: ")
            realizar_acao(tipoUsuario, 'buscar_produto', nome)
        else:
            print("Opção inválida. Retornando ao menu principal")

# Executar o menu
exibir_menu()
