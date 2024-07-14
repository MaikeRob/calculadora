"""Responsavel por guardar a classe que realiza o processamento dos calculos"""

import sympy as sp


# class CalculationProcessor:
#     """Classe que recebe a string de entrada e devolve o resultado"""

#     def __init__(self):
#         pass

#     def processor(self, expression):
#         """Responsavel por calcular a espressão de entrada e devolver uma resposta"""
#         try:
#             result = sp.sympify(expression)
#             return result
#         except ZeroDivisionError:
#             return "Divisão por Zero!"
#         except sp.SympifyError as e:
#             print(f"Processador de calculos diz : {e}")
#             return "Erro"
#         except SyntaxError as e:
#             print(f"Processador de calculos diz : {e}")
#             return "Erro"
#         except TypeError as e:
#             print(f"Processador de calculos diz : {e}")
#             return "Erro"
#         except Exception as e:
#             print(f"Processador de calculos diz : {e}")
#             return "Erro"


def expression_processor(expression):
    """Responsavel por calcular a espressão de entrada e devolver uma resposta"""
    try:
        result = sp.sympify(expression)#sympify não retorna ponto flutuante
        return result
    except ZeroDivisionError:
        return "Divisão por Zero!"
    except sp.SympifyError as e:
        print(f"Processador de calculos diz : {e}")
        return "Erro"
    except SyntaxError as e:
        print(f"Processador de calculos diz : {e}")
        return "Erro"
    except TypeError as e:
        print(f"Processador de calculos diz : {e}")
        return "Erro"
    except Exception as e:
        print(f"Processador de calculos diz : {e}")
        return "Erro"
