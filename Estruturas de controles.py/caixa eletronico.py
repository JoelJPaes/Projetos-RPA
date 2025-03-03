saldo = 1000  # Saldo inicial

while True:
    print("\nBem-vindo ao Caixa Eletrônico")
    print("1. Ver saldo")
    print("2. Sacar dinheiro")
    print("3. Sair")
    
    opcao = input("Escolha uma opção: ")
    
    if opcao == "1":
        print(f"Saldo atual: R${saldo}")
    elif opcao == "2":
        valor = int(input("Digite o valor para sacar: "))
        if valor > saldo:
            print("Saldo insuficiente!")
        else:
            saldo -= valor
            print("Contando notas...")
            notas = [100, 50, 20, 10, 5, 2, 1]
            for nota in notas:
                qtd = valor // nota
                if qtd > 0:
                    print(f"{qtd} nota(s) de R${nota}")
                    valor -= qtd * nota
            print(f"Saque realizado! Saldo restante: R${saldo}")
    elif opcao == "3":
        print("Saindo... Obrigado por usar nosso caixa eletrônico!")
        break
    else:
        print("Opção inválida! Tente novamente.")
