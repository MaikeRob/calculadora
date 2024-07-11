import tkinter as tk

class Aplicattion(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Calculadora")
        self.geometry("350x500+1100+300")
        self.minsize(350,500)
        #self.maxsize() Definir tamanho maximo depois

        self.button_frame = ButtonFrame(self)
        self.button_frame.config(
            background='white'
        )
        self.button_frame.place(relx=0, rely=0.332, relwidth=1, relheight=0.67)


        self.entry_frame = ButtonFrame(self)
        self.entry_frame.config(
            background='red'
        )
        self.entry_frame.place(relx=0, rely=0, relwidth=1, relheight=0.332)

class ButtonFrame(tk.Frame):
    def __init__(self, parent=None):
        super().__init__()





class EntryFrame(tk.Frame):
    def __init__(self, parent=None):
        super().__init__()

app = Aplicattion()
app.mainloop()