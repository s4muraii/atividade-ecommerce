class Carrinho_Compra:
    lista_compra = []

    def inserir_produto(self, produto):
        self.produto = produto
        self.lista_compra.append(produto)

    def listar_produtos(self):
        self.cont = 0
        for produto in self.lista_compra:
            self.cont += 1
            print(f"{self.cont}: Nome: {produto.getNome()}, Valor: {produto.getPreco()}")

    def getLista(self, vetor):
        return self.lista_compra(vetor)
    
    def delProduto(self, vetor):
        self.vetor_lista = vetor - 1
        self.lista_compra.pop(vetor)
    
class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def getNome(self):
        return self.nome
    
    def getPreco(self):
        return self.preco
    
class Usuário (Produto, Carrinho_Compra):
    clientes = []
    def __init__(self, nome, senha):
        self.nome = nome
        self.senha = senha

    def inserir_cliente(self, cliente):
        self.cliente = cliente
        self.clientes.append(cliente)

    def delCliente(self, vetor):
        self.vetor_lista = vetor - 1
        self.clientes.pop(vetor)

    def getNome(self):
        return self.nome
    
    def getSenha(self):
        return self.senha
    
    def setNome(self, nome):
        self.nome = nome

    def setSenha(self, senha):
        self.senha = senha

    def listar_clientes(self):
        self.cont = 0
        for cliente in self.clientes:
            self.cont += 1
            print(f"{self.cont}: Nome: {cliente.getNome()}, Senha: {cliente.getSenha()}")