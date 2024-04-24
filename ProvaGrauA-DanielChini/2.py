# Agora crie uma função divisivelPorN que receba como parâmetro dois números inteiros e retorne
# True se o primeiro é divisível pelo segundo, e False caso contrário. O segundo parâmetro não pode ser zero,
# então cheque isso dentro da função (se for zero, imprima uma mensagem dizendo que não é possível efetuar
# divisão por zero e retorne False).

def divisivelPorN(num1, num2):
    if num2 == 0:
        print("Não é possivel efetuar a operação")
    elif num1 % num2 == 0:
        print(True)
    else:
        print("False")
    
num1 = int(input("Digite um número: "))
num2 = int(input("Digite outro número: "))

divisivelPorN(num1, num2)