"""Modulo responsavel por guardar a declaração da classe que lida com os eventos da aplicação"""


class CalculatorHandler:
    """Lida com os eventos da aplicação"""

    def __init__(self, view, calculator):

        self.view = view
        self.calculator = calculator
        self.current_real_expression = ""
        self.current_view_expression = ""

    def on_button_click(self, button_text):
        """Quando um botão da aplicação é clicado, recebe qual botão foi clicado
        e lida com o evento relacionado.
         Adicionar elementos na string da entrada ou
         Fazer o calculo da string"""

        match button_text:
            case "=":
                result = self.calculator.evaluate_expression(
                    self.current_real_expression
                )
                self.current_view_expression = f"{result}"
                self.view.update_main_frame_entry(self.current_view_expression)
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
            case "⌫":
                self.current_real_expression = self.current_real_expression[0:-1]
                self.current_view_expression = self.current_view_expression[0:-1]
                self.view.update_main_frame_entry(self.current_view_expression)
            case "CE":
                self.current_real_expression = ""
                self.current_view_expression = ""
                self.view.update_main_frame_entry(self.current_view_expression)
            case ",":
                self.current_real_expression += "."
                self.current_view_expression += ","
                self.view.update_main_frame_entry(self.current_view_expression)
            case "%":  # melhorar esse calculo, por enquanto deixo assim simples
                self.current_real_expression += "/100"
                self.current_view_expression += "%"
                self.view.update_main_frame_entry(self.current_view_expression)
            case _:
                pass

    def on_key_pressed(self, event):
        """"Quando uma tecla do teclado é apertada, recebe qual tecla foi apertada
        e lida com o evento relacionado."""
        print(f"{event.keysym}")

        numbers = {
            "KP_0": "0",
            "KP_1": "1",
            "KP_2": "2",
            "KP_3": "3",
            "KP_4": "4",
            "KP_5": "5",
            "KP_6": "6",
            "KP_7": "7",
            "KP_8": "8",
            "KP_9": "9",
            "0": "0",
            "1": "1",
            "2": "2",
            "3": "3",
            "4": "4",
            "5": "5",
            "6": "6",
            "7": "7",
            "8": "8",
            "9": "9"
        }

        match event.keysym:
            case "equal":
                result = self.calculator.evaluate_expression(
                    self.current_real_expression
                )
                self.current_view_expression = f"{result}"
                self.view.update_main_frame_entry(self.current_view_expression)
            case digit if digit in numbers:
                self.current_real_expression += numbers[digit]
                self.current_view_expression += numbers[digit]
                self.view.update_main_frame_entry(self.current_view_expression)
            case digit if digit in ["KP_Add", "plus"]:
                self.current_real_expression += "+"
                self.current_view_expression += "+"
                self.view.update_main_frame_entry(self.current_view_expression)
            case digit if digit in ["KP_Subtract", "minus"]:
                self.current_real_expression += "-"
                self.current_view_expression += "-"
                self.view.update_main_frame_entry(self.current_view_expression)
            case digit if digit in ["KP_Multiply", "asterisk"]:
                self.current_real_expression += "*"
                self.current_view_expression += "x"
                self.view.update_main_frame_entry(self.current_view_expression)
            case digit if digit in ["KP_Divide", "slash"]:
                self.current_real_expression += "/"
                self.current_view_expression += "÷"
                self.view.update_main_frame_entry(self.current_view_expression)
            case "percent":  # melhorar esse calculo, por enquanto deixo assim simples
                self.current_real_expression += "/100"
                self.current_view_expression += "%"
                self.view.update_main_frame_entry(self.current_view_expression)
            case "BackSpace":
                self.current_real_expression = self.current_real_expression[0:-1]
                self.current_view_expression = self.current_view_expression[0:-1]
                self.view.update_main_frame_entry(self.current_view_expression)
            case "comma":
                self.current_real_expression += "."
                self.current_view_expression += ","
                self.view.update_main_frame_entry(self.current_view_expression)
            case _:
                pass
            