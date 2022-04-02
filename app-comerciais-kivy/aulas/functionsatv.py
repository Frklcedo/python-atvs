def estudo():
    print("Estamos estudando as funções")


def estudo1(x):
    print(f"Função invocada com sucesso. O valor passado pelo argumento x é: {x}")


def soma(x, y):
    print(x + y)


def ascendente(a, b, c):
    lista = [a, b, c]
    lista.sort()
    for num in lista:
        print(num)
    print((a + b + c) / 3)


def obrigatfacult(x, y='inexistente'):
    print(x, y)


def func1(x, y):

    def func2(x, y):
        return x + y

    return func2(x, y)


def list_funf(*args):
    print(args)


def dicio_func(**dicio):
    for k, v in dicio.items():
        print(k, v)


def func(a, b, c, d):
    print(a + b + c + d)


def maior(a, b, c):
    return max(list((a, b, c)))


def soma_all(*args):
    resultado = 0
    for num in args:
       resultado += num
    return resultado


def multiplica_all(*args):
    resultado = list(args).pop(0);
    for num in args:
        resultado *= num
    return resultado


def revert_order(l):
    l = list(l)
    le, j = [], -1
    while(len(le) < len(l)):
        le.append(l[j])
        j -= 1
    return le


def fatorial(n):
    nf = n
    n -= 1
    if(nf == 0):
        nf += 1
    while( n > 0):
        nf *= n
        n-= 1
    return nf


def inrange(x, start, end):
    return x in range(start, end)


def stcount(string):
    up, low = 0, 0
    for c in string:
        if 65 <= ord(c) <= 90:
            up += 1
        elif 97 <= ord(c) <= 122:
            low += 1
    return {"upper_c": up, "lower_c": low}


def create_set(*args):
    lista = []
    for item in args:
        if(not lista.__contains__(item)):
            lista.append(item)
    return lista


def primos_in(*args):
    aset, res = create_set(*args), []
    for numero in range(len(aset)):
        if (numero % 2 == 0 and numero != 2):
            continue
        cont = 0
        for divisor in range(1, numero):
            if (numero % divisor == 0):
                cont += 1
        if (cont == 1):
            res.append(numero)
    return res


ascendente(2, 3, 1)

print(func1(12, 13))

lista = 1, 2, 3, 4
func(*lista)

print(maior(5, 54, 32))

print("Soma: ", soma_all(1, 2, 3, 4, 5))
print("Multiplicação: ", multiplica_all(1, 2, 3, 4, 5))

print(revert_order("1234abcd"))

print(fatorial(2))

print(inrange(4, 2, 3))

print(stcount("Ooi Mundo"))

print(create_set(1,2,2,3,4,54,5,3,43,43,5,5,6,2,1,2,2,1,2,1,2,1))

print(primos_in(1,2,3,4,5,7,4,3,2,2,6,7,8,9))