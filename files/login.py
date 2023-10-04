import json

def nome_existe_e_senha_correta(nome, senha):
    # Carregar os dados de usuários a partir do arquivo JSON.
    try:
        with open('dados_usuarios.json', 'r') as arquivo:
            dados_usuarios = json.load(arquivo)
    except FileNotFoundError:
        dados_usuarios = []

    # Verificar se o nome de usuário existe e se a senha está correta.
    for usuario in dados_usuarios:
        if usuario["nome"] == nome and usuario["senha"] == senha:
            return True
    
    return False

def login():
    print("---------------LOGIN---------------")
    
    nome = input("Nome: ")
    senha = input("Senha: ")
    
    if nome_existe_e_senha_correta(nome, senha):
        print("Login realizado com sucesso!", nome)
    else:
        print("Dados inválidos")
