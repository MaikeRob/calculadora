"""Responsavel por guardar a classe que realiza o processamento dos calculos"""

class CalculationProcessor:
    """Classe que recebe a string de entrada e devolve o resultado"""

    def __init__(self):
        pass

    def evaluate_expression(self, expression):
        """Responsavel por calcular a espressão de entrada e devolver uma resposta"""

        for digit in expression:
            if not digit in "0123456789,/*-+":
                return "Security Error"
        try:
            result = eval(expression)
            return result
        except ZeroDivisionError:
            return "Divisão por Zero!"
        except Exception as e:
            print(f"Processador de calculos diz : {e}")
            return "Erro"
