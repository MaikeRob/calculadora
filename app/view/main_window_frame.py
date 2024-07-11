import tkinter as tk

class MainWindowFrame(tk.Frame):
    """Classe do frame Principal da janela da calculadora, contem o frame de botoes e o frame da entrada,
    está contido na janela da aplicação"""
    def __init__(self, parent=None):
        super().__init__()

        self.button_frame = ButtonFrame(self)
        self.button_frame.config(
            background='white'
        )
        self.button_frame.place(relx=0, rely=0.332, relwidth=1, relheight=0.67)


        self.entry_frame = EntryFrame(self)
        self.entry_frame.config(
            background='red'
        )
        self.entry_frame.place(relx=0, rely=0, relwidth=1, relheight=0.332)



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
            text='0'
            )
        self.zero_button.place(relx=0.25, rely=0.8, relwidth=0.25, relheight=0.20)

        self.one_button = tk.Button(
            self, 
            bg="white",
            fg="black",
            activebackground="#F3F3F3",
            highlightthickness=0,
            bd=0,
            text='1'
            )
        self.one_button.place(relx=0, rely=0.6, relwidth=0.25, relheight=0.20)

        self.two_button = tk.Button(
            self, 
            bg="white",
            fg="black",
            activebackground="#F3F3F3",
            highlightthickness=0,
            bd=0,
            text='2'
            )
        self.two_button.place(relx=0.25, rely=0.6, relwidth=0.25, relheight=0.20)

        self.three_button = tk.Button(
            self, 
            bg="white",
            fg="black",
            activebackground="#F3F3F3",
            highlightthickness=0,
            bd=0,
            text='3'
            )
        self.three_button.place(relx=0.50, rely=0.6, relwidth=0.25, relheight=0.20)

class EntryFrame(tk.Frame):
    """Classe do frame da string de entrada, está contido no frame principal"""
    def __init__(self, parent=None):
        super().__init__()