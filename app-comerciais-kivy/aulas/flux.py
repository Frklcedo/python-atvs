# tomada de decisão e if, if else e if elif else
a = 10
if(a==10):
    print("O valor a é igual a 10")
if(a==9):
    print("O valor a é igual a 9")
# teste if else
acao = int(input("Digite 1 para sim e digite 2 para não: "))
if(acao==1):
    print("Você digite que sim")
else:
    if(acao==2):
        print("Você disse que não")
    else:
        print("O número digitado está incorreto")
print()
# operadores comparativos
idade = int(input("informe sua idade:"))
if(idade<0):
    print("a sua idade não pode ser menor que zero")
else:
    if(idade>150):
        print("a sua idade não pode ser maior que 150")
    else:
        if(idade>=18):
            print("você é maior de idade")
        elif(idade<=12):
            print("você é apenas uma criança")
        else:
            print("aproveite a adolescência")
print()
# relacionais na prática
num1 = input("digite o primeiro número:")
num1 = int(num1)
num2 = input("digite o segundo número:")
num2 = int(num2)
print()
if(num1 == num2):
    print(f"{num1} é igual a {num2}")
if(num1 != num2):
    print(f"{num1} é diferente a {num2}")
if(num1 > num2):
    print(f"{num1} é maior a {num2}")
if(num1 < num2):
    print(f"{num1} é menor a {num2}")
if(num1 >= num2):
    print(f"{num1} é maior ou igual a {num2}")
if(num1 <= num2):
    print(f"{num1} é menor ou igual a {num2}")

# operadores lógicos
print()
print("2 == 2 and 4 < 3: ", 2 == 2 and 4 < 3) # &&
print("2 == 2 or 4 < 3: ",2 == 2 or 4 < 3) # ||
print("not(2 == 2 or 4 < 3): ",not(2 == 2 or 4 < 3)) # !
print("type(2) is int: ",type(2) is int)
print("type(2.0) is int: ",type(2.0) is int)
print()

# blocos de instrução
num1 = int(input("Digite um número: "))

if(num1 > 10):
    print("O valor é maior que 10")
    if(num1<=15):
        print("O número é maior que 10 mas menor ou igual a 15")
    else:
        if(num1<=50):
            print("O número é maior que 15 mas menor ou igual a 50")
        else:
            print("O número é maior que 50")
else:
    if(num1>5):
        print("O número é menor que 10 e maior  que 5")
        if(num1==7):
            print("O número é igual a 7")
    else:
        if(num1==5):
            print("O número é igual a 5")
        else:
            print("O valor é menor que 5")