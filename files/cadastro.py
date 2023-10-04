import json

def cadastrar_usuario():
    print("---------------BEM-VINDO---------------")
    
    nome = input("Digite seu nome: ")
    email = input("Digite seu e-mail: ")
    senha = input("Digite sua senha: ")
    
    # Carregar os dados atuais de usuários, se existirem, ou criar uma lista vazia.
    try:
        with open('dados_usuarios.json', 'r') as arquivo:
            dados_usuarios = json.load(arquivo)
    except FileNotFoundError:
        dados_usuarios = []

    # Adicionar o novo usuário aos dados existentes.
    novo_usuario = {"nome": nome, "email": email, "senha": senha}
    dados_usuarios.append(novo_usuario)
    
    # Salvar os dados atualizados no arquivo JSON.
    with open('dados_usuarios.json', 'w') as arquivo:
        json.dump(dados_usuarios, arquivo)
    
    print("Cadastro realizado com sucesso!")
