vez = "n"

def soma(a, b):
    return a + b

def subtracao(a, b):
    return a - b

def multiplicacao(a, b):
    return a * b

def divisao(a, b):
    if b != 0:
        return a / b
    else:
        return "Erro: Divisão por zero"
    
def potencia(a, b):
    return a ** b

while vez.lower() == "n":

    try:
        valor1 = float(input("Digite o primeiro valor: "))
        valor2 = float(input("Digite o segundo valor: "))

    except ValueError:
        print("Valor inválido. Por favor, digite um número.")
        continue
    
    operacao = input("Digite o simbolo da operação (+, -, *, /, **): ")

    if operacao == "+":
        resultado = soma(valor1, valor2)

    elif operacao == "-":
        resultado = subtracao(valor1, valor2)

    elif operacao == "*":
        resultado = multiplicacao(valor1, valor2)

    elif operacao == "/":
        resultado = divisao(valor1, valor2)

    elif operacao == "**":
        resultado = potencia(valor1, valor2)

    else:
        resultado = "Operação inválida"

    print("Resultado: ", resultado)

    vez = input("Deseja realizar outra operação? (s/n): ")