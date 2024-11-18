from calculos import calcular_distancia, calcular_angulos

def menu():
    while True:
        print("\n=== Calculadora Trigonométrica ===")
        print("1. Calcular o terceiro lado (Teorema de Pitágoras)")
        print("2. Calcular ângulos e lados com um ângulo conhecido")
        print("3. Sair")
        
        opcao = input("Escolha uma opção: ")
        
        if opcao == "1":
            calcular_distancia()
        elif opcao == "2":
            calcular_angulos()
        elif opcao == "3":
            print("Encerrando a calculadora. Até mais!")
            break
        else:
            print("Opção inválida! Escolha novamente.")

if __name__ == "__main__":
    menu()
