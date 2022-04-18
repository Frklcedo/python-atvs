#coding: utf-8

from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.core.window import Window

input_text = None


def click():
    print(input_text.text)


def build():
    layout = FloatLayout()

    global input_text
    input_text = TextInput(text="Digite algo aqui")
    input_text.size_hint = None, None
    input_text.height = 300
    input_text.width = 400
    input_text.x = 60
    input_text.y = 250

    bt = Button(text="Clique aqui")
    bt.size_hint = None, None
    bt.height = 100
    bt.width = 200
    bt.x = 100
    bt.y = 100
    bt.on_press = click

    layout.add_widget(input_text)
    layout.add_widget(bt)
    return layout


janela = App()
janela.title = "First Layout"

Window.size = 600, 600

janela.build = build
janela.run()
