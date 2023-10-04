import cadastro
import login

while True:
    print("Escolha uma opção:")
    print("1. Cadastro")
    print("2. Login")
    print("3. Sair")
    
    opcao = input("Opção: ")
    
    if opcao == "1":
        cadastro.cadastrar_usuario()
    elif opcao == "2":
        login.login()
    elif opcao == "3":
        print("Parando programa.")
        break
    else:
        print("Opção inválida")