"""Script que roda a aplicação"""

from app.views.window import Window
from app.controllers.calculator_handler import CalculatorHandler

if __name__ == "__main__":
    controller = CalculatorHandler(None)
    view = Window(controller)
    controller.view = view
    view.mainloop()
