def calculadora():
    while True:
        print("\nCalculadora Simples")
        print("1. Somar")
        print("2. Subtrair")
        print("3. Multiplicar")
        print("4. Dividir")
        print("5. Sair")
        
        opcao = input("Escolha uma opção: ")
        
        if opcao == "5":
            print("Saindo... Obrigado por usar a calculadora!")
            break
        
        try:
            num1 = float(input("Digite o primeiro número: "))
            num2 = float(input("Digite o segundo número: "))
            
            if opcao == "1":
                print(f"Resultado: {num1 + num2}")
            elif opcao == "2":
                print(f"Resultado: {num1 - num2}")
            elif opcao == "3":
                print(f"Resultado: {num1 * num2}")
            elif opcao == "4":
                print(f"Resultado: {num1 / num2}")
            else:
                print("Opção inválida! Tente novamente.")
        except ValueError:
            print("Erro: Digite apenas números válidos!")
        except ZeroDivisionError:
            print("Erro: Não é possível dividir por zero!")

calculadora()
