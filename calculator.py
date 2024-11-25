from tkinter import *
import math
from functions import functions

class calculator:
    def __init__(self):
        self.calc = Tk()
        self.calc.configure(bg="#2C3E50")
        self.calc.title("Scientific Calculator")
        
        self.function_obj = functions() 
        
        self.setup_display()
        self.setup_buttons()
        
    def setup_display(self):
        self.display_frame = Frame(self.calc, bg="#2C3E50")
        self.display_frame.grid(row=0, column=0, columnspan=5, padx=10, pady=15, sticky="nsew")
        self.display = Text(self.display_frame, height=2, width=20, font=('Arial', 20), bd=5, bg='#ECF0F1')
        self.display.pack(fill=BOTH, expand=True)
        self.display.tag_configure('expression', justify='right')
        self.display.tag_configure('result', justify='right', font=('Arial', 24, 'bold'))
        self.function_obj.set_display(self.display)

    def setup_buttons(self):
        button_params = {
            'bd': 1,
            'fg': '#FFFFFF',
            'bg': '#34495E',
            'font': ('Arial', 16),
            'relief': 'raised',
            'padx': 5,
            'pady': 5
        }
        
        button_params_main = {
            'bd': 1,
            'fg': '#FFFFFF',
            'bg': '#2980B9',
            'font': ('Arial', 16),
            'relief': 'raised',
            'padx': 5,
            'pady': 5
        }
        
        function_params = {
            'bd': 1,
            'fg': '#FFFFFF',
            'bg': '#2C3E50',
            'font': ('Arial', 14),
            'relief': 'raised',
            'padx': 5,
            'pady': 5
        }


        Button(self.calc, function_params, text='abs', command=lambda: self.function_obj.button_click('abs(')).grid(row=1, column=0, sticky="nsew")
        Button(self.calc, function_params, text='mod', command=lambda: self.function_obj.button_click('%')).grid(row=1, column=1, sticky="nsew")
        Button(self.calc, function_params, text='div', command=lambda: self.function_obj.button_click('//')).grid(row=1, column=2, sticky="nsew")
        Button(self.calc, function_params, text='x!', command=self.function_obj.fact_func).grid(row=1, column=3, sticky="nsew")
        Button(self.calc, function_params, text='e', command=lambda: self.function_obj.button_click(str(math.e))).grid(row=1, column=4, sticky="nsew")

        Button(self.calc, function_params, text='sin', command=self.function_obj.trig_sin).grid(row=2, column=0, sticky="nsew")
        Button(self.calc, function_params, text='cos', command=self.function_obj.trig_cos).grid(row=2, column=1, sticky="nsew")
        Button(self.calc, function_params, text='tan', command=self.function_obj.trig_tan).grid(row=2, column=2, sticky="nsew")
        Button(self.calc, function_params, text='cot', command=self.function_obj.trig_cot).grid(row=2, column=3, sticky="nsew")
        Button(self.calc, function_params, text='π', command=lambda: self.function_obj.button_click(str(math.pi))).grid(row=2, column=4, sticky="nsew")

        Button(self.calc, function_params, text='x²', command=lambda: self.function_obj.button_click('**2')).grid(row=3, column=0, sticky="nsew")
        Button(self.calc, function_params, text='x³', command=lambda: self.function_obj.button_click('**3')).grid(row=3, column=1, sticky="nsew")
        Button(self.calc, function_params, text='x^n', command=lambda: self.function_obj.button_click('**')).grid(row=3, column=2, sticky="nsew")
        Button(self.calc, function_params, text='x⁻¹', command=lambda: self.function_obj.button_click('**(-1)')).grid(row=3, column=3, sticky="nsew")
        Button(self.calc, function_params, text='10^x', command=lambda: self.function_obj.button_click('10**')).grid(row=3, column=4, sticky="nsew")

        Button(self.calc, function_params, text='√x', command=self.function_obj.square_root).grid(row=4, column=0, sticky="nsew")
        Button(self.calc, function_params, text='³√x', command=self.function_obj.third_root).grid(row=4, column=1, sticky="nsew")
        Button(self.calc, function_params, text='∛n', command=lambda: self.function_obj.button_click('**(1/')).grid(row=4, column=2, sticky="nsew")
        Button(self.calc, function_params, text='log₁₀', command=lambda: self.function_obj.button_click('log(')).grid(row=4, column=3, sticky="nsew")
        Button(self.calc, function_params, text='ln', command=lambda: self.function_obj.button_click('math.log(')).grid(row=4, column=4, sticky="nsew")

        Button(self.calc, button_params_main, text="AC", command=self.function_obj.button_clear_all).grid(row=5, column=0, columnspan=2, sticky="nsew")
        Button(self.calc, button_params_main, text="DEL", command=self.function_obj.button_delete).grid(row=5, column=2, sticky="nsew")
        Button(self.calc, button_params_main, text="±", command=self.function_obj.sign_change).grid(row=5, column=3, sticky="nsew")
        Button(self.calc, button_params_main, text="=", command=self.function_obj.button_equal).grid(row=5, column=4, sticky="nsew")

        Button(self.calc, button_params, text='7', command=lambda: self.function_obj.button_click('7')).grid(row=6, column=0, sticky="nsew")
        Button(self.calc, button_params, text='8', command=lambda: self.function_obj.button_click('8')).grid(row=6, column=1, sticky="nsew")
        Button(self.calc, button_params, text='9', command=lambda: self.function_obj.button_click('9')).grid(row=6, column=2, sticky="nsew")
        Button(self.calc, button_params, text='/', command=lambda: self.function_obj.button_click('/')).grid(row=6, column=3, sticky="nsew")
        Button(self.calc, button_params, text='(', command=lambda: self.function_obj.button_click('(')).grid(row=6, column=4, sticky="nsew")

        Button(self.calc, button_params, text='4', command=lambda: self.function_obj.button_click('4')).grid(row=7, column=0, sticky="nsew")
        Button(self.calc, button_params, text='5', command=lambda: self.function_obj.button_click('5')).grid(row=7, column=1, sticky="nsew")
        Button(self.calc, button_params, text='6', command=lambda: self.function_obj.button_click('6')).grid(row=7, column=2, sticky="nsew")
        Button(self.calc, button_params, text='*', command=lambda: self.function_obj.button_click('*')).grid(row=7, column=3, sticky="nsew")
        Button(self.calc, button_params, text=')', command=lambda: self.function_obj.button_click(')')).grid(row=7, column=4, sticky="nsew")

        Button(self.calc, button_params, text='1', command=lambda: self.function_obj.button_click('1')).grid(row=8, column=0, sticky="nsew")
        Button(self.calc, button_params, text='2', command=lambda: self.function_obj.button_click('2')).grid(row=8, column=1, sticky="nsew")
        Button(self.calc, button_params, text='3', command=lambda: self.function_obj.button_click('3')).grid(row=8, column=2, sticky="nsew")
        Button(self.calc, button_params, text='-', command=lambda: self.function_obj.button_click('-')).grid(row=8, column=3, sticky="nsew")
        Button(self.calc, button_params, text='%', command=self.function_obj.percent).grid(row=8, column=4, sticky="nsew")

        Button(self.calc, button_params, text='0', command=lambda: self.function_obj.button_click('0')).grid(row=9, column=0, columnspan=2, sticky="nsew")
        Button(self.calc, button_params, text='.', command=lambda: self.function_obj.button_click('.')).grid(row=9, column=2, sticky="nsew")
        Button(self.calc, button_params, text='+', command=lambda: self.function_obj.button_click('+')).grid(row=9, column=3, columnspan=2, sticky="nsew")

        for i in range(5):
            self.calc.grid_columnconfigure(i, weight=1)
        for i in range(10):
            self.calc.grid_rowconfigure(i, weight=1)

        padding = {'padx': 1, 'pady': 1}
        for child in self.calc.winfo_children():
            child.grid_configure(**padding)

        self.calc.mainloop()

if __name__ == "__main__":
    app = calculator()