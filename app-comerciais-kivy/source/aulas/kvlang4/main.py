#coding: utf-8

import kivy
kivy.require("1.9.1")

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout


class MinhaTela(BoxLayout):
    def click(self):
        print("oi")
        self.ids.lb1.text = 'Ola'
        self.ids.lb2.text = 'Mundo'


class Estudo4App(App):
    pass


janela = Estudo4App()
janela.run()
