import math 
from tkinter import StringVar, END

class functions:
    def __init__(self):
        self.calc_operator = ""
        self.calc_expression = ""
        self.display = None
        
    def set_display(self, display):
        self.display = display

    def update_display(self):
        if not self.display:
            return
        self.display.delete(1.0, END)
        display_expr = self.calc_expression.replace('math.', '')
        self.display.insert(END, display_expr + '\n', 'expression')
        
        if self.calc_operator:
            try:
                if self.calc_operator[-1] == ')' or self.calc_operator[-1].isdigit():
                    result = str(eval(self.calc_operator))
                    self.display.insert(END, result, 'result')
            except ZeroDivisionError:
                self.display.insert(END, "Error: Division by 0", 'result')
            except Exception:
                self.display.insert(END, "Error", 'result')

    def button_click(self, char):
        try:
            if char.startswith('math.'):

                self.calc_operator += char
                self.calc_expression += char[5:]
            else:
                self.calc_operator += str(char)
                self.calc_expression += str(char)
            self.update_display()
        except Exception:
            self.display.delete(1.0, END)
            self.display.insert(END, "Error")

    def button_clear_all(self):
        try:
            self.calc_operator = ""
            self.calc_expression = ""
            if self.display:
                self.display.delete(1.0, END)
                self.display.insert(END, "\n", 'expression')
        except Exception:
            if self.display:
                self.display.delete(1.0, END)
                self.display.insert(END, "Error")

    def button_delete(self):
        try:
            if self.calc_operator:
                self.calc_operator = self.calc_operator[:-1]
                self.calc_expression = self.calc_expression[:-1]
                self.update_display()
        except Exception:
            self.display.delete(1.0, END)
            self.display.insert(END, "Error")

    def factorial(self, n):
        try:
            if n == 0 or n == 1:
                return 1
            else:
                return n * self.factorial(n - 1)
        except Exception as e:
            raise ValueError(f"Invalid input for factorial: {str(e)}")

    def fact_func(self):
        try:
            result = str(self.factorial(int(eval(self.calc_operator))))
            self.calc_operator = result
            self.calc_expression = result
            self.update_display()
        except Exception:
            self.display.delete(1.0, END)
            self.display.insert(END, "Error")

    def trig_sin(self):
        self.button_click('math.sin(')

    def trig_cos(self):
        self.button_click('math.cos(')

    def trig_tan(self):
        self.button_click('math.tan(')

    def trig_cot(self):
        try:
            self.button_click('1/math.tan(')
        except ZeroDivisionError:
            self.display.delete(1.0, END)
            self.display.insert(END, "Error: Division by 0")

    def square_root(self):
        self.button_click('math.sqrt(')

    def third_root(self):
        try:
            temp = f"({self.calc_operator})**(1/3)"
            result = str(eval(temp))
            self.calc_operator = result
            self.calc_expression = result
            self.update_display()
        except Exception:
            self.display.delete(1.0, END)
            self.display.insert(END, "Error")

    def sign_change(self):
        try:
            if self.calc_operator:
                if self.calc_operator[0] == '-':
                    self.calc_operator = self.calc_operator[1:]
                    self.calc_expression = self.calc_expression[1:]
                else:
                    self.calc_operator = '-' + self.calc_operator
                    self.calc_expression = '-' + self.calc_expression
                self.update_display()
        except Exception:
            self.display.delete(1.0, END)
            self.display.insert(END, "Error")

    def percent(self):
        try:
            temp = str(eval(self.calc_operator + '/100'))
            self.calc_operator = temp
            self.calc_expression = temp
            self.update_display()
        except Exception:
            self.display.delete(1.0, END)
            self.display.insert(END, "Error")

    def button_equal(self):
        try:
            temp_op = str(eval(self.calc_operator))
            self.calc_operator = temp_op
            self.calc_expression = temp_op
            self.update_display()
        except ZeroDivisionError:
            self.display.delete(1.0, END)
            self.display.insert(END, "Error: Division by Zero")
        except Exception:
            self.display.delete(1.0, END)
            self.display.insert(END, "Error")
