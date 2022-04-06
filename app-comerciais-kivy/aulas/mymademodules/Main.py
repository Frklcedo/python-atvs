#coding: utf-8

#Modulo Main

from pprint import pprint
from sys import path as lpath
import Estudo
import dis
from ferramentas import *
import mod_a
import importlib


def func():
    print("Oi mãe")


pprint(lpath)
print(__name__)
Estudo.module_name()
dis.dis(func)
print()
print()
pprint(globals())

mod_a.a = 0
del(mod_a.b)
pprint(mod_a.__dict__)

importlib.reload(mod_a)

pprint(mod_a.__dict__)

print("O programa acabou")
