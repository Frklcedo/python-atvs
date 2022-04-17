#coding: utf-8

class B:
    def __init__(self):
        print(id(self))
        self._var = 0

    @property
    def var(self):
        return self._var

    @var.setter
    def var(self, v):
        self._var = v


b = B()
b.var = 10
print(b.var)