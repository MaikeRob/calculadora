"""Script que roda a aplicação"""

from app.views.window import Window
from app.controllers.calculator_handler import CalculatorHandler
from app.models.calculation_processor import CalculationProcessor

if __name__ == "__main__":
    calculator = CalculationProcessor()
    controller = CalculatorHandler(view=None, calculator=calculator)
    view = Window(controller)
    controller.view = view
    view.mainloop()
