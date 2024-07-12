"""Modulo responsavel por guardar a declaração da janela da aplicação"""

import tkinter as tk

from app.view.main_window_frame import MainWindowFrame

class Window(tk.Tk):
    """Classe da janela da aplicação, aqui se define caracteristicas da janela e
    se declara o frame"""
    def __init__(self):
        super().__init__()
        self.title("Calculadora")
        self.geometry("350x500+1100+300")
        self.minsize(350,500)
        #self.maxsize() Definir tamanho maximo depois

        self.main_frame = MainWindowFrame(self)
        self.main_frame.place(relx=0, rely=0, relwidth=1, relheight=1)
