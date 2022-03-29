print("Olá mundo")
"""
print("testando comentários: primeira linha")
#print("segunda linha")
print("terceira linha")
"""

if True:
    print("oi")
print("ola")

#print("tchau"); print("tchauu"); # não recomendado

a = 10
b =30
print(a + b)
texto = "um texto aleatório"
print(texto)
print(type(texto))
print(type(a))
dinheiro = 15.50
print(dinheiro)
print(type(dinheiro))

# manipulando variáveis
num_int = 5
num_dec =10.5
val_str = "qualquer texto"

print("1 O valor inteiro é: ", num_int)
print("2 O valor inteiro é: %i" %num_int)
print(f"3 O valor inteiro é: {num_int}")
print("4 O valor inteiro é: " + str(num_int))

print("Concatenando decimal: ", num_dec)
print("Concatenando decimal: %f" %num_dec)
print("Concatenando decimal: %.2f" %num_dec)
print("Concatenando decimal: " + str(num_dec))

print("Concatenando strings:", val_str)
print("Concatenando strings: %s" %val_str)
print("Concatenando strings: " + val_str)
