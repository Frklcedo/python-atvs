#coding: utf-8

from kivy.app import App
from kivy.uix.textinput import TextInput


def build():
    ti = TextInput(text="Componente TextInput: escreva algo aqui")
    return ti


janela = App()
janela.build = build
janela.run()
