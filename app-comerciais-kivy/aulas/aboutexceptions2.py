#coding: utf-8


def erro(erro):
    try:
        eval(erro)
    except ValueError as e:
        print("ValueError")
        print(type(e)) # instância da exception
        print(e.args) # argumentos da exception
        print(e) # __str__ message
    except ZeroDivisionError:
        print("ZeroDivisionError")
    except (TypeError, NameError) as e:
        print("TypeError ou NameError")
        print(type(e)) # instância da exception
        print(e.args) # argumentos da exception
        print(e) # __str__ message
    else:
        print("Nenhuma exceção ocorreu")
    finally:
        print("Sempre será executado")


# TypeError
erro("int+int")

# NameError
erro("a")

# ValueError
erro("int('a')")

# ZeroDivisionError
erro("5/0")

erro("10/10")
print("código finalizado")
