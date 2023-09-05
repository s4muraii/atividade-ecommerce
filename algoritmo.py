from classes import *
import os

def main():
    x = 1
    def tela2 ():
        escolha = int(input("1 - Cadastrar produto\n2 - Listar produtos\n3 - Adicionar no carrinho\n4 - Visualizar carrinho\n5 - Excluir produto\n6 - Sair\n"))  
        match escolha:
            case 1:
                produto = Produto(input("Digite o nome do produto: "), float(input("Digite o valor do produto: ")))
                cliente.inserir_produto(produto)
                print("Produto cadastrado com sucesso!")
                os.system("pause")
                os.system("cls")
                tela2()
            case 2:
                cliente.listar_produtos()
                os.system("pause")
                os.system("cls")
                tela2()
            case 3:
                cliente.listar_produtos()
                cliente.getLista(int(input("Digite o número do produto que deseja adicionar ao carrinho: ")))
                print("Produto adicionado ao carrinho com sucesso!")
                os.system("pause")
                os.system("cls")
                tela2()
            case 4:
                cliente.listar_produtos()
                os.system("pause")
                os.system("cls")
                tela2()
            case 5:
                cliente.listar_produtos()
                cliente.delProduto(int(input("Digite o número do produto que deseja excluir: ")))
                print("Produto excluído com sucesso!")
                os.system("pause")
                os.system("cls")
                tela2()
            case 6:
                print("Saindo...")
                os.system("pause")
                os.system("cls")
                main()

    while x == 1:
        print ("----------------------------------------------------------------------\n\n Bem-Vindo ao E-Commerce\n\n----------------------------------------------------------------------\n")
        menu = int(input("1 - Cadastrar\n2 - Login\n3 - Listar\n4 - Excluir\n5 - Sair\n"))
        match menu:
            case 1:
                os.system("cls")
                cliente = Usuário(input("Digite o nome do cliente: "), input("Digite a senha do cliente: "))
                cliente.inserir_cliente(cliente)
                print("Cliente cadastrado com sucesso!")
                os.system("pause")
                os.system("cls")
                tela2()
                              
            case 2:
                nome = input("Digite o nome do cliente: ")
                senha = input("Digite a senha do cliente: ")
                if nome == cliente.getNome() and senha == cliente.getSenha():
                    print("Login efetuado com sucesso!")
                    os.system("pause")
                    os.system("cls")
                    tela2()
                else:
                    print("Login ou senha incorretos!")
                    os.system("pause")
                    os.system("cls")
                    main()

            case 3:
                cliente.listar_clientes()
                os.system("pause")
                os.system("cls")
                main()
            case 4:
                cliente.listar_clientes()
                cliente.delCliente(int(input("Digite o número do cliente que deseja excluir: ")))
                print("Cliente excluído com sucesso!")
                os.system("pause")
                os.system("cls")
                main()

            case 5:
                print("Saindo...")
                x = 0
