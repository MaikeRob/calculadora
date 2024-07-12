"""Modulo responsavel por guardar a declaração da janela da aplicação"""

import tkinter as tk

from app.views.main_window_frame import MainWindowFrame


class Window(tk.Tk):
    """Classe da janela da aplicação, aqui se define caracteristicas da janela e
    se declara o frame"""

    def __init__(self, controller):
        super().__init__()
        self.title("Calculadora")
        self.geometry("350x500+1100+300")
        self.minsize(350, 500)
        # self.maxsize() Definir tamanho maximo depois

        self.controller = controller

        self.main_frame = MainWindowFrame(self)
        self.main_frame.place(relx=0, rely=0, relwidth=1, relheight=1)

    def update_main_frame_entry(self, expression):
        """Atualiza o frame da entrada"""
        self.main_frame.update_entry_frame_expression(expression)
