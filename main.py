from datetime import datetime

vez = "s"

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

def escrever_resultado(v1, v2, op, res):
    data = datetime.now()
    data_operacao = data.strftime("%d-%m-%Y")
    hora_atual = data.strftime("%H:%M:%S")
    with open("historico.txt", "a") as arquivo:
        arquivo.write(f"{data_operacao}\n{hora_atual}\n{v1} {op} {v2} = {res}\n\n")

while vez.lower() == "s":

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

    escrever_resultado(valor1, valor2, operacao, resultado)
    print(f"Resultado: {resultado}")
    print('testando...')

    vez = input("\nDeseja realizar outra operação? (s/n): ")