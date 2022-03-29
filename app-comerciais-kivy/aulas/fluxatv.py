num = int(input("Digite um número: "))

if(num==0):
    print("O número digitado é nulo")
elif(num>0):
    print(f"O número {num} é maior que 0")
else:
    print(f"O número {num} é menor que 0")
print()

###
num = input("Digite um número: ")
num = int(num)

if(num%2==0):
    print(f"O número {num} é par")
else:
    print(f"O número {num} é impar")

###
"""
#num,num2 = input("Digite dois números: ").split()
num, num2 = [int(x) for x in input("Digite dois números\t").split()]
print(num if (num > num2) else num2)
print()
"""
###
idade = int(input("digite sua idade: "))
idade_mae = int(input("digite a idade de sua mãe: "))

print(f"Sua mãe o teve com {idade_mae - idade} anos de idade")
print()

###
num = int(input("digite um número: "))
num2 = int(input("digite um segundo número: "))
print(f"{num}, {num2}" if (num > num2) else f"{num2}, {num}")

print(" - \n"*50)
print()
###
inp = input("Digite algum número: ")
print("inteiro" if inp.isnumeric() else "não é inteiro")
inp = input("Digite algo: ")
print("string" if inp.isalpha() else "não é string")
inp = input("Digite alguma coisa: ")
print("decimal" if inp.isdecimal() else "não é float")
print()
###
a = [ int(x) for x in input("Digite 3 números\t").split()]
print(max(a))
a.sort()
print(a)
print()
###
letra = input("digite uma letra: ").lower()
print("vogal" if letra in "aeiou" else "não é vogal")