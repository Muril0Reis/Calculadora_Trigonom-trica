def validar_entrada(mensagem):
    try:
        valor = float(input(mensagem))
        if valor <= 0:
            print("O valor deve ser positivo!")
            return None
        return valor
    except ValueError:
        print("Entrada inválida! Certifique-se de inserir um número.")
        return None
