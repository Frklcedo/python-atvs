#coding: utf-8

from pprint import pprint


class MEstaticos:

    # @staticmethod
    def func1():
        print("func1()")

    @staticmethod
    def func2(x, y):
        print("Função {}\nargs= ({}, {})".format("func2", x, y))

    # @staticmethod
    def func3(a, b, c):
        info = """
        Nome da função: {nome}
        Quantidade de Args: {quantidade}
        Args: {args}
        """
        info = info.format(
            nome=MEstaticos.func3.__name__,
            quantidade=MEstaticos.func3.__code__.co_argcount,
            args=MEstaticos.func3.__code__.co_varnames
        )
        pprint(info)

    func1 = staticmethod(func1)
    # func2 = staticmethod(func2)
    func3 = staticmethod(func3)


me = MEstaticos()
me.func1()
MEstaticos.func1()
me.func2(4, 6)
MEstaticos.func2(23, 27)
me.func3('a', 'bb', 'ccc')
me.func3(32, 43, 54)
