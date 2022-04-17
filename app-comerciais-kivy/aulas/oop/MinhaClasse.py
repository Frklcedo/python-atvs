#coding: utf-8

class MinhaClasse:
    membro_cls = 0

    def __init__(self):
        self.membro_inst = 11

    def func(self):
        self.membro_cls = 30
        print(self.membro_inst)
        print(self.membro_cls)
        print(MinhaClasse.membro_cls)
        print("O método func() foi invocado.")


i1 = MinhaClasse()
i1.func()
MinhaClasse.func(i1)
i2 = MinhaClasse()
i2.membro_inst = -10

# MinhaClasse.func('')

print(MinhaClasse.membro_cls)
MinhaClasse.membro_cls = 10
print(MinhaClasse.membro_cls)
