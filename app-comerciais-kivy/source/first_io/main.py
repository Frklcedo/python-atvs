#coding: utf-8

from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.core.window import Window


class Program(App):

    def __init__(self, iotext, bttext):
        super().__init__()
        self.itext = TextInput(text=iotext)
        self.bt = Button(text=bttext)

    def click(self):
        print(self.itext.text)

    def text_input_config(self, h, w, x, y):
        self.itext.size_hint = None, None
        self.itext.height = h
        self.itext.width = w
        self.itext.x = x
        self.itext.y = y

    def button_config(self, h, w, x, y):
        self.bt.size_hint = None, None
        self.bt.height = h
        self.bt.width = w
        self.bt.x = x
        self.bt.y = y

    def build(self):
        layout = FloatLayout()

        self.bt.on_press = self.click

        # self.text_input_config(h=300, w=400, x=60, y=250)
        # self.button_config(h=100, w=200, x=100, y=100)

        layout.add_widget(self.itext)
        layout.add_widget(self.bt)
        return layout


# janela = Program()
janela = Program(iotext="Digite algo aqui", bttext="Clique aqui")

janela.title = "First Layout"
janela.text_input_config(h=300, w=400, x=60, y=250)
janela.button_config(h=100, w=200, x=100, y=100)

Window.size = 600, 600

janela.run()
