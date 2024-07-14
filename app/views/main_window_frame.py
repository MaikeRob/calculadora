"""Modulo responsavel por guardar a declaração da classe da janela principal da aplicação"""

import tkinter as tk
from tkinter import font


class MainWindowFrame(tk.Frame):
    """Classe do frame Principal da janela da calculadora, contem o frame
    de botoes e o frame da entrada,está contido na janela da aplicação"""

    def __init__(self, parent=None):
        super().__init__()

        self.controller = parent.controller

        self.inter_font = font.Font(family="Inter", size=25, weight="bold")

        self.button_frame = ButtonFrame(self)
        self.button_frame.config(background="white")
        self.button_frame.place(relx=0, rely=0.332, relwidth=1, relheight=0.67)

        self.entry_frame = EntryFrame(self)
        self.entry_frame.config(background="black")
        self.entry_frame.place(relx=0, rely=0, relwidth=1, relheight=0.332)

    def update_entry_frame_expression(self, expression):
        """Atualiza o frame da entrada"""
        self.entry_frame.update_entry(expression)


class ButtonFrame(tk.Frame):
    """Classe do frame dos botoes, está contido no frame principal"""

    def __init__(self, parent=None):
        super().__init__()

        self.zero_button = tk.Button(
            self,
            bg="white",
            fg="black",
            activebackground="#F3F3F3",
            highlightthickness=0,
            bd=0,
            text="0",
            font=parent.inter_font,
        )
        self.zero_button.place(relx=0.25, rely=0.8, relwidth=0.25, relheight=0.20)

        self.one_button = tk.Button(
            self,
            bg="white",
            fg="black",
            activebackground="#F3F3F3",
            highlightthickness=0,
            bd=0,
            text="1",
            font=parent.inter_font,
        )
        self.one_button.place(relx=0, rely=0.6, relwidth=0.25, relheight=0.20)

        self.two_button = tk.Button(
            self,
            bg="white",
            fg="black",
            activebackground="#F3F3F3",
            highlightthickness=0,
            bd=0,
            text="2",
            font=parent.inter_font,
        )
        self.two_button.place(relx=0.25, rely=0.6, relwidth=0.25, relheight=0.20)

        self.three_button = tk.Button(
            self,
            bg="white",
            fg="black",
            activebackground="#F3F3F3",
            highlightthickness=0,
            bd=0,
            text="3",
            font=parent.inter_font,
        )
        self.three_button.place(relx=0.50, rely=0.6, relwidth=0.25, relheight=0.20)

        self.four_button = tk.Button(
            self,
            bg="white",
            fg="black",
            activebackground="#F3F3F3",
            highlightthickness=0,
            bd=0,
            text="4",
            font=parent.inter_font,
        )
        self.four_button.place(relx=0, rely=0.4, relwidth=0.25, relheight=0.20)

        self.five_button = tk.Button(
            self,
            bg="white",
            fg="black",
            activebackground="#F3F3F3",
            highlightthickness=0,
            bd=0,
            text="5",
            font=parent.inter_font,
        )
        self.five_button.place(relx=0.25, rely=0.4, relwidth=0.25, relheight=0.20)

        self.six_button = tk.Button(
            self,
            bg="white",
            fg="black",
            activebackground="#F3F3F3",
            highlightthickness=0,
            bd=0,
            text="6",
            font=parent.inter_font,
        )
        self.six_button.place(relx=0.5, rely=0.4, relwidth=0.25, relheight=0.20)

        self.seven_button = tk.Button(
            self,
            bg="white",
            fg="black",
            activebackground="#F3F3F3",
            highlightthickness=0,
            bd=0,
            text="7",
            font=parent.inter_font,
        )
        self.seven_button.place(relx=0, rely=0.2, relwidth=0.25, relheight=0.20)

        self.eight_button = tk.Button(
            self,
            bg="white",
            fg="black",
            activebackground="#F3F3F3",
            highlightthickness=0,
            bd=0,
            text="8",
            font=parent.inter_font,
        )
        self.eight_button.place(relx=0.25, rely=0.2, relwidth=0.25, relheight=0.20)

        self.nine_button = tk.Button(
            self,
            bg="white",
            fg="black",
            activebackground="#F3F3F3",
            highlightthickness=0,
            bd=0,
            text="9",
            font=parent.inter_font,
        )
        self.nine_button.place(relx=0.5, rely=0.2, relwidth=0.25, relheight=0.20)

        self.sum_button = tk.Button(
            self,
            bg="white",
            fg="black",
            activebackground="#F3F3F3",
            highlightthickness=0,
            bd=0,
            text="+",
            font=parent.inter_font,
        )
        self.sum_button.place(relx=0.75, rely=0.6, relwidth=0.25, relheight=0.20)

        self.subtraction_button = tk.Button(
            self,
            bg="white",
            fg="black",
            activebackground="#F3F3F3",
            highlightthickness=0,
            bd=0,
            text="-",
            font=parent.inter_font,
        )
        self.subtraction_button.place(
            relx=0.75, rely=0.4, relwidth=0.25, relheight=0.20
        )

        self.multiply_button = tk.Button(
            self,
            bg="white",
            fg="black",
            activebackground="#F3F3F3",
            highlightthickness=0,
            bd=0,
            text="x",
            font=parent.inter_font,
        )
        self.multiply_button.place(relx=0.75, rely=0.2, relwidth=0.25, relheight=0.20)

        self.division_button = tk.Button(
            self,
            bg="white",
            fg="black",
            activebackground="#F3F3F3",
            highlightthickness=0,
            bd=0,
            text="÷",
            font=parent.inter_font,
        )
        self.division_button.place(relx=0.75, rely=0, relwidth=0.25, relheight=0.20)

        self.equals_button = tk.Button(
            self,
            bg="white",
            fg="black",
            activebackground="#F3F3F3",
            highlightthickness=0,
            bd=0,
            text="=",
            font=parent.inter_font,
        )
        self.equals_button.place(relx=0.75, rely=0.8, relwidth=0.25, relheight=0.20)

        self.comma_button = tk.Button(
            self,
            bg="white",
            fg="black",
            activebackground="#F3F3F3",
            highlightthickness=0,
            bd=0,
            text=",",
            font=parent.inter_font,
        )
        self.comma_button.place(relx=0.5, rely=0.8, relwidth=0.25, relheight=0.20)

        self.sinal_button = tk.Button(
            self,
            bg="white",
            fg="black",
            activebackground="#F3F3F3",
            highlightthickness=0,
            bd=0,
            text="+/-",
            font=(parent.inter_font, 20),
        )
        self.sinal_button.place(relx=0, rely=0.8, relwidth=0.25, relheight=0.20)

        self.backspace_button = tk.Button(
            self,
            bg="white",
            fg="#bd2d2d",
            activeforeground="#bd2d2d",
            activebackground="#F3F3F3",
            highlightthickness=0,
            bd=0,
            text="⌫",
            font=parent.inter_font,
        )
        self.backspace_button.place(relx=0.5, rely=0, relwidth=0.25, relheight=0.20)

        self.clear_entry_button = tk.Button(
            self,
            bg="white",
            fg="black",
            activebackground="#F3F3F3",
            highlightthickness=0,
            bd=0,
            text="CE",
            font=parent.inter_font,
        )
        self.clear_entry_button.place(relx=0.25, rely=0, relwidth=0.25, relheight=0.20)

        self.percent_button = tk.Button(
            self,
            bg="white",
            fg="black",
            activebackground="#F3F3F3",
            highlightthickness=0,
            bd=0,
            text="%",
            font=parent.inter_font,
        )
        self.percent_button.place(relx=0, rely=0, relwidth=0.25, relheight=0.20)

        self.buttons = [
            self.zero_button,
            self.one_button,
            self.two_button,
            self.three_button,
            self.four_button,
            self.five_button,
            self.six_button,
            self.seven_button,
            self.eight_button,
            self.nine_button,
            self.sum_button,
            self.subtraction_button,
            self.multiply_button,
            self.division_button,
            self.equals_button,
            self.clear_entry_button,
            self.backspace_button,
            self.percent_button,
            self.comma_button,
        ]

        for self.button in self.buttons:
            self.text = self.button.cget("text")
            self.button.config(
                command=lambda text=self.text: parent.controller.on_button_click(text)
            )


class EntryFrame(tk.Frame):
    """Classe do frame da string de entrada, está contido no frame principal"""

    def __init__(self, parent=None):
        super().__init__()

        self.entry_expression = tk.StringVar()
        self.entry_expression.set("")

        self.entry_label = tk.Label(
            self,
            bg="black",
            foreground="white",
            textvariable=self.entry_expression,
            font=parent.inter_font,
            anchor="se",
        )
        self.entry_label.place(relx=0, rely=0.457, relwidth=1, relheight=0.560)

    def update_entry(self, expression):
        """Atualiza o frame da entrada"""
        self.entry_expression.set(expression)
        # self.entry_label.config(text=self.entry_expression)
