lista = ['a','b', 4, 2.55, ["Olá", "Mundo"]]
print(lista)
print(len(lista))
print("lista[len(lista)-1] == lista[-1]")
print(lista[len(lista)-1])
print(lista[-1])

lista = lista + [33]
print(lista)
lista = ['Algo antes'] + lista
print(lista)
# ou
lista.append(123)
lista.append([123])
print(lista)

#del
## queue
del(lista[0])
## stack
del(lista[-1])
print(lista)

nova_lista = [0]*10
print(nova_lista)
lista += [0]*10
print(lista)

## iterando listas
lista_nums = [100, 200, 300, 400]
for item in lista_nums:
    item += 1000
print(lista_nums)

lista_indice = [0,1,2,3]
for index in lista_indice:
    lista_nums[index] += 1000
print(lista_nums)

print(list(range(len(lista_nums))))
for index in range(len(lista_nums)):
    lista_nums[index] += 1000
print(lista_nums)

## funcão enumerate
for index,key in enumerate(lista_nums):
    lista_nums[index] += 1000
print(lista_nums)

print()
## slices
pyt = list("python") #pyt[ start(def = 0) : end(def = len(pyt) : step(def = 1) ]
print("pyt = ",pyt)
print("pyt[1] = ",pyt[1])
print("pyt[1:] = ",pyt[1:])
print("pyt[:4] = ",pyt[:4])
print("pyt[1:4] = ",pyt[1:4])
print("pyt[::2] = ",pyt[::2])
print("inverter lista")
print("pyt[::-1] = ",pyt[::-1])

# pop push append, etc
l = ['bbb','ccc','ddd']
l.append('eee')
print(l)
l.insert(0,'aaa')
print(l)
l[1] = 'bbbb'
print('fui retirado da lista o último item: ',l.pop())
print(l)
print('fui retirado da lista o primeiro item: ',l.pop(0))
print(l)
l += ['fff','ggg','hhh','iii','jjj','kkk']
print(l)
del(l[4:7])
print(l)
del(l[::2])
print(l)

l.clear()
print(l)

print()
# order list
nomes = ["Zelda", "Link", "Gannondorf", "Mario", "Luigi", "Bowser", "Peach"]
print(nomes)
nomes.reverse()
print("reversão articial: ", nomes)

nomes.sort()
print("ordenação de forma ascendente: ", nomes)
nomes.sort(reverse=True)
print("ordenação de forma descendente: ", nomes)

nomes.insert(4,"Zelda")
nomes.append("Zelda")
print(nomes)
print(nomes.count("Zelda"))
print(nomes.count("Link"))

print(f"{nomes[nomes.index('Link')]} : {nomes.index('Link')}")
print(f"{nomes[nomes.index('Zelda')]} : {nomes.index('Zelda')}")
nomes.pop(nomes.index('Zelda'))
print(nomes.count("Zelda"))
print(f"{nomes[nomes.index('Zelda')]} : {nomes.index('Zelda')}")

print()
# in e not in
a = 10
b = 25
c = 66

x = int(input("Digite um número: "))
if x in (a,b,c):
    print(f"{x} está contido")
else:
    print(f"{x} não está contido")

cores = ["preto", "roxo", "rosa", "verde"]
while True:
    cor = input("Digite o nome de uma cor (forceexit=0) ")
    if cor is "0":
        break
    elif cor in cores:
        print(f"{cor} está contida")
    else:
        print(f"{cor} não está contida")
