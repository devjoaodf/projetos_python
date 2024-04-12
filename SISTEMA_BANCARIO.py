menu = """

[s] Sacar

[d] Depositar

[e] Extrato

[q] Sair

=> """

saldo = 0

limite = 500

extrato = 0

extratofinal = 0


numero_saques = 0

LIMITE_SAUQES = 3

while True:

    opcao = input(menu)

    if opcao == "s":
        try:
            print("Seu saldo é: ", extratofinal)
            saque = int(input("Seu Saldo : "))
            if saque <= deposito:
                deposito -= saque
            else:
                print("valor imcompativel favor inserir novamente")
        except ValueError:
            print("Seu Saldo não é suficiente, escolha o valor dentro do seu saldo")
            continue # volta para o inicio do loop
    elif opcao == "e":
         print("seu saldo é: ", extratofinal)

    if opcao == "d":
        print("Deposito")
        deposito = int(input("insira um valor inteiro deposito : "))

    elif opcao == "q":
        break

    else:
        print("Operação invalida, por favor selecione novamente a operação desejada.")