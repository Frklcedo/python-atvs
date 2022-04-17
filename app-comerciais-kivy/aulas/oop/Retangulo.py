#coding: utf-8

__all__ = ["Retangulo"]


class Retangulo:

    def __init__(self, h=0, l=0):
        if isinstance(h, int) and h > 0:
            self._h = h
        else:
            self._h = 0
        if isinstance(l, int) and l > 0:
            self._l = l
        else:
            self._l = 0

    # def _get_h(self):
    @property
    def h(self):
        return self._h

    # def _set_h(self, h):
    @h.setter
    def h(self, h):
        if isinstance(h, int) and h > 0:
            self._h = h
        # else:
        #     raise ValueError("Altura é inválida: {}".format(h))

    # def _get_l(self):
    @property
    def l(self):
        return self._l

    # def _set_l(self, l):
    @l.setter
    def l(self, l):
        if isinstance(l, int) and l > 0:
            self._l = l
        # else:
        #     raise ValueError("Largura é inválida: {}".format(l))

    # def _get_area(self):
    @property
    def area(self):
        return self._h * self._l

    # h = property(fget=_get_h, fset=_set_h)
    # l = property(fget=_get_l, fset=_set_l)
    # area = property(fget=_get_area)


r1 = Retangulo()
r1.l = 10
r1.h = 5
# r1._set_l(10)
# r1._set_h(5)

# print(r1.get_area())
print(r1.area)

r2 = Retangulo()
r3 = Retangulo()

# r2.teste = 'algo'
# print(r2.teste)
