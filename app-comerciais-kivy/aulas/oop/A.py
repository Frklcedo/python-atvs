#coding: utf-8

class A:
    def __init__(self):
        print(id(self))
        self._var = 0

    def _get_var(self):
        return self._var

    def _set_var(self, v):
        self._var = v

    var = property(fget=_get_var, fset=_set_var)


def teste(s):
    print(id(s))


a = A()
print(id(a))
teste(a)
print()

# a.set_var(100)
# print(a.get_var())

a.var = 2000
print(a.var)
