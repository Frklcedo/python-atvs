#coding: utf-8

import os
import kivy
kivy.require("1.9.1")

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.button import Button

code = """

BoxLayout: 
    Button:
        text: "1"
    Button:
        text: "2"

"""


class Estudo6App(App):
    def build(self):
        return Builder.load_string(code)
        # return Builder.load_file(os.path.join(os.path.dirname(__file__)) + '/usingbuilder.kv')


janela = Estudo6App()
janela.run()
