from builtins import ZeroDivisionError


def input_float(msg):
    while True:
        try:
            return float(input(msg))
        except ValueError:
            print("Número inválido.")


num1 = input_float("Digite o primeiro número: ")
while True:
    num2 = input_float("Digite o segundo número: ")
    try:
        print(num1 / num2)
    except ZeroDivisionError:
        print("Não é possível dividir número por zero")
