import kivy
from kivy.app import App
kivy.require('1.9.0')
from kivy.uix.gridlayout import GridLayout
from kivy.config import Config
Config.set('graphics', 'resizable', 1)

# Определение класса CalcGridLayout, наследуемого от GridLayout
class CalcGridLayout(GridLayout):

    # Функция вызывается при нажатии на кнопку "равно"
    def calculate(self, calculation):
        if calculation:
            try:
                # Решаем формулу и выводим результат на экран
                self.display.text = str(eval(calculation))
            except Exception:
                self.display.text = "Ошибка"

# Определение класса приложения CalculatorApp, наследуемого от App
class CalculatorApp(App):

    # Метод build, который будет вызван при запуске приложения
    def build(self):
        return CalcGridLayout()

# Создание объекта приложения и его запуск
calcApp = CalculatorApp()
calcApp.run()