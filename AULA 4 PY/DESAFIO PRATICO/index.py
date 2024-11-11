def soma (a, b):

    return a + b

def subtracao (a, b):

    return a - b

def multiplicacao (a, b):

    return a * b

def divisao (a, b):

    return a / b

def calculadora ():

    while True:

        print("Escolha uma opção: ")
        print("1. soma")
        print("2. subtração")
        print("3. multiplicação")
        print("4. divisão")
        print("5. sair")
    
        escolha = int(input("Digite o numero da opção que você deseja: "))
        
        if escolha == 5:
            print("Saindo da calculadora...")
            break

        try:
            num1 = float(input("Digite o primeiro numero: "))
            num2 = float(input("Digite o segundo numero: "))
        except:
            print("ERRO: Numero invalido")
            break

        if escolha == 1:
            soma(num1, num2)
            print(f"O resultado da operação {num1} + {num2} = {soma(num1, num2)}")
        elif escolha == 2:
            subtracao(num1, num2)
            print(f"O resultado da operação {num1} - {num2} = {subtracao(num1, num2)}")
        elif escolha == 3:
            multiplicacao(num1, num2)
            print(f"O resultado da operação {num1} x {num2} = {multiplicacao(num1, num2)}")
        elif escolha == 4:
            divisao(num1, num2)
            print(f"O resultado da operação {num1} / {num2} = {divisao(num1, num2)}")
        else:
            print("Tente novamente")
            calculadora()

calculadora()
