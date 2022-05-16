#coding: utf-8
import kivy

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button


class Tela1(BoxLayout):

    def on_press_bt(self):
        janela.root_window.remove_widget(janela.root)
        janela.root_window.add_widget(Tela2())

    def __init__(self, **kwargs):
        super(Tela1, self).__init__(**kwargs)
        self.orientation = "vertical"
        btn1 = Button(text="btn1")
        btn1.on_press = self.on_press_bt
        self.add_widget(btn1)
        self.add_widget(Button(text="btn2"))
        self.add_widget(Button(text="btn3"))


class Tela2(BoxLayout):

    def on_press_bt(self):
        janela.root_window.remove_widget(janela.root)
        janela.root_window.add_widget(Tela1())

    def __init__(self, **kwargs):
        super(Tela2, self).__init__(**kwargs)
        self.orientation = "vertical"
        bt = Button(text="Sad")
        bt.on_press = self.on_press_bt
        self.add_widget(bt)


class KVvsPY(App):
    def build(self):
        return Tela1()


janela = KVvsPY()
janela.run()
