saques_feitos = []
limite_saques = 3
limite_saque_individual = 500
deposito_valor = 0
todos_usuarios = []

class Usuario:
    def __init__(self, nome, cpf):
        self.nome = nome
        self.cpf = cpf

def saque():
    global deposito_valor
    global saques_feitos
    global limite_saques
    global limite_saque_individual

    print("Você selecionou o Saque")
    saqueuser = int(input("Digite um valor: "))
    
    if saqueuser <= limite_saque_individual and len(saques_feitos) < limite_saques:
        if saqueuser <= deposito_valor:
            saques_feitos.append(saqueuser)
            deposito_valor -= saqueuser
            print("Saque de", saqueuser, "realizado com sucesso.")
            print("Saldo restante:", deposito_valor)
        else:
            print("Saldo insuficiente.")
    else:
        print("O valor do saque excede o limite permitido ou você atingiu o limite de saques.")


def deposito():
      global deposito_valor
      print("Você selecionou o deposito: ")
      deposito_valor = (int(input("Insira um valor para deposito: ")))
      print("Seu valor inserido para deposito é: ", deposito_valor)
      
def extrato():
    global deposito_valor
    global saques_feitos

    print("Seu extrato:")
    print("Depósito inicial:", deposito_valor)
    print("Saques realizados:", saques_feitos)
    print("Saldo atual:", deposito_valor - sum(saques_feitos))

def opcao_padrao():
      print("Escolha uma opção valida.")

def mostrar_menu():
      print("Menu:")
      print("1. Opção saque")
      print("2. Opção deposito")
      print("3. Opção extrato")
      print("4. Listar todos os usuários")
      print("5. Criar novo usuário")
      print("6. Opção sair")

def validar_saque(saqueuser):
      try:
            return int(saqueuser)
      except ValueError:
            return None
      

def listar_usuarios():
    print("Lista de Usuários:")
    for usuario in todos_usuarios:
        print("Nome:", usuario.nome)
        print("CPF:", usuario.cpf)
        print()


def criar_usuario():
    nome = input("Digite o nome do novo usuário: ")
    cpf = input("Digite o CPF do novo usuário: ")
    for usuario in todos_usuarios:
        if usuario.nome == nome and usuario.cpf == cpf:
            print("Usuário já existe.")
            return
    todos_usuarios.append(Usuario(nome, cpf))
    print("Usuário criado com sucesso.")


def menu():
    while True:
        mostrar_menu()
        opcao = input("Escolha uma operação: ")

        if opcao == '1':
            saque()
        elif opcao == '2':
            deposito()
        elif opcao == '3':
            extrato()
        elif opcao == '4':
            listar_usuarios()
        elif opcao == '5':
            criar_usuario()
        elif opcao == '6':
            exit()
        else:
            opcao_padrao()

if __name__ == "__main__":
    menu()
                  
