#coding: utf-8

from Retangulo import Retangulo

r1 = Retangulo(h=25, l=20)
r1.l = "algo"
print(r1)
print(dir(r1))
# print(r1.get_l())
# print(r1.get_area())
print(r1.l)
print(r1.area)
