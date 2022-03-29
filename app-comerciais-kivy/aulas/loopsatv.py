"""
for i in range(2,100):
    print(i)

for i in range(10,0,-1):
    print(i)

for pares in range (0,101,2):
    print(pares)

starto = int(input("Digite o começo do intervalo: "))
intervalo = int(input("Digite o fim do intervalo: "))
for numero in range(starto,intervalo):
    if(numero%2 == 0 and numero != 2):
        continue
    cont = 0
    for divisor in range(1,numero):
        if(numero%divisor == 0):
            cont += 1
    if(cont==1):
        print(numero)

starto = int(input("Digite o começo do intervalo: "))
intervalo = int(input("Digite o fim do intervalo: "))

a = [ int(x) for x in input("Digite números para serem ignorados:").split()]

for i in range(starto, intervalo):
    if(a.__contains__(i)):
        continue
    print(i)
"""

while(True):
    print("estou em looping")
    q = input()
    if(q == 'q'):
        break