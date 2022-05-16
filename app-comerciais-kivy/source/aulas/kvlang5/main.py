#coding: utf-8

import kivy
kivy.require("1.9.1")

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button


def func_self(x):
    print("func_self")


Button.func_self = func_self


class MinhaTela(BoxLayout):
    def func_root(self):
        print("func_root")


class Estudo5App(App):
    def func_app(self):
        print("func_app")


janela = Estudo5App()
janela.run()
