"""
def greet():
    print("Hello World")

greet()
"""


def greet(nome = "Mundo"):
    print(f"Olá, {nome}")


def soma(x,y):
    total = x+y
    print(f"A soma de {x} + {y} é: {total}")


def dados_pessoais(nome,sobrenome,idade,sexo):
    print("Nome: {}\nSobrenome: {}\nIdade: {}\nSexo: {}"
          .format(nome, sobrenome, idade, sexo))


def multiplicacao(x, y):
    return x * y


def get_dados():
    x = float(input("Digite um número: "))
    y = float(input("Digite um outro número: "))
    return x, y


def potencias(x):
    quadrado = x**2
    cubo = x**3

    return quadrado, cubo


def lista_de_argumentos(*args):
    print(args)


def lista_de_argumentos_associativos(**kwargs):
    print(kwargs)


def argumentos(*args, **kwargs):
    print(args)
    print(kwargs)


def printing(a, b):
    print(a, b)


def pessoa(nome, sobrenome, idade):
    print(nome)
    print(sobrenome)
    print(idade)


def func_externa():
    print("func")

    def func_interna():
        print("func_interna")

    func_interna()


greet()
soma(10,50)
greet("Frklcedo")
dados_pessoais("Bilbo", "Bolseiro", 115, True)
print()
dados_pessoais(nome="Túrin",
               sexo=True,
               sobrenome="Turambar",
               idade=85)
print()
print(multiplicacao(3, 3))

a, b = 3, 2 # get_dados()
soma(a, b)
print()
a = 3
q, c = potencias(a)
print(f"{a} ao quadrado é {q}")
print(f"{a} ao cubo é {c}")

"""
lista_de_argumentos(1,2,3,4,5,6)
lista_de_argumentos("um", "dois", "três", "quatro")
lista_de_argumentos_associativos(nome="Frklcedo", idade=21, ambicao="dev")
lista_de_argumentos_associativos(um=1 , dois=2, tres=3, quatro=4)
"""
argumentos(1,2,3,4,5,6, nome="Frklcedo", idade=21, ambicao="dev")
argumentos("um", "dois", "três", "quatro", um=1 , dois=2, tres=3, quatro=4)

# desempacotamento
lista = [10, 20]
printing(*lista)
print()
#person = 'Elendil', 'Voronda', 87
person = ['Elendil', 'Voronda', 87]
pessoa(*person)
print()
person = {"nome":'Isildur', "idade":55, "sobrenome":'Voronda'}
pessoa(**person)

lista = 11,12,10,9;


def mustorder(a,b,c,d):
    print("This numbers must go out in order")
    print("{}\n{}\n{}\n{}\n".format(a,b,c,d))


mustorder(**dict(zip(("c", "d", "b", "a"),lista)))

func_externa()

print()


def nonlocal_func():
    var_local = 10

    def func_interna():
        nonlocal var_local
        var_local += 10

    func_interna()
    print(var_local)


nonlocal_func()

x = "global and nonlocal"


def global_func():
    global x
    print(x)


global_func()