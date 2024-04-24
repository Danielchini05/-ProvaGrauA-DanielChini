# Faça uma função divisivelPor2 que receba como parâmetro um número inteiro, e retorne True se o
# número é divisível por 2, e False caso contrário.

def divisivelPor2(num):
    if num % 2 == 0:
        print(True)
    else:
        print(False)


num = int(input("Digite um número inteiro: "))

divisivelPor2(num)