#coding: utf-8

from kivy.app import App
from kivy.uix.textinput import TextInput


class firstIO(App):

    def build(self):
        ti = TextInput(text="Componente TextInput: escreva algo aqui")
        return ti


janela = firstIO()
janela.run()
