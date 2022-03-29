import math

login = input("Login: ")
senha = input("Senha: ")
#print(login)
#print(senha)
print("O usuário informado foi: %s, e a senha foi: %s" %(login,senha))
a1 = int(input("Digite o primeiro numero: "))
a2 = int(input("Digite o segundo numero: "))
print("soma:",a1 + a2)
print("subtração:",a1 - a2)
print("multiplicação:",a1 * a2)
print("divisão:",a1 / a2)
print("divisão para inteiro:",a1 // a2)
print("resto da divisão:",a1 % a2)
# pontenciacao e radiciacao

print()
b = int(input("Digite um número para radiciação: "))
bp = b**2
br = b**(1/2)
print(f"{b} elevado ao quadrado é {bp}")
print(f"A raiz quadrada de {b} é {br}")
print(math.pi)