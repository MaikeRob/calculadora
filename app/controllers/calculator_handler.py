"""Modulo responsavel por guardar a declaração da classe que lida com os eventos da aplicação"""


class CalculatorHandler:
    """Lida com os eventos da aplicação"""

    def __init__(self, view):

        self.view = view
        self.current_real_expression = ""
        self.current_view_expression = ""

    def on_button_click(self, button_text):
        """Quando um botão da aplicação é clicado, recebe qual botão foi clicado
        e lida com o evento relacionado.
         Adicionar elementos na string da entrada ou
         Fazer o calculo da string"""

        match button_text:
            case "=":
                pass
            case digit if digit in "0123456789":
                self.current_real_expression += digit
                self.current_view_expression += digit
                self.view.update_main_frame_entry(self.current_view_expression)
            case digit if digit in "+-":
                self.current_real_expression += digit
                self.current_view_expression += digit
                self.view.update_main_frame_entry(self.current_view_expression)
            case "x":
                self.current_real_expression += "*"
                self.current_view_expression += "x"
                self.view.update_main_frame_entry(self.current_view_expression)
            case "÷":
                self.current_real_expression += "/"
                self.current_view_expression += "÷"
                self.view.update_main_frame_entry(self.current_view_expression)
            case _:
                pass
