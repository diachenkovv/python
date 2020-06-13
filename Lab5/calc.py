# Дяченко В.В., ЗПІ-18
# Створити... калькулятор!

from tkinter import *


class Main(Frame):
    def __init__(self, root):
        super(Main, self).__init__(root)
        self.build()

    def build(self):
        self.formula = "0"
        self.lbl = Label(text=self.formula, font=(
            "Arial Black", 21, "bold"), bg="#000", foreground="#FFF")
        self.lbl.place(x=11, y=50)  # рядок

        btns = [
            "C", "DEL", "*", "=",
            "1", "2", "3", "/",
            "4", "5", "6", "+",
            "7", "8", "9", "-",
            "(", "0", ")", "X²"
        ]

        x = 10
        y = 140
        for bt in btns:
            def com(x=bt): return self.logicalc(x)
            Button(text=bt, bg="#FFF", foreground="#000",
                   font=("Arial Black", 15, "bold"),
                   command=com).place(x=x, y=y,
                                      width=115,
                                      height=79)  # кнопки
            x += 117
            if x > 400:
                x = 10
                y += 81

    def logicalc(self, operation):
        if operation == "C":
            self.formula = ""
        elif operation == "DEL":
            self.formula = self.formula[0:-1]
        elif operation == "X²":
            self.formula = str((eval(self.formula))**2)
        elif operation == "=":
            self.formula = str(eval(self.formula))
        else:
            if self.formula == "0":
                self.formula = ""
            self.formula += operation
        self.update()

    def update(self):
        if self.formula == "":
            self.formula = "0"
        self.lbl.configure(text=self.formula)


if __name__ == '__main__':  # віконечко
    root = Tk()
    root["bg"] = "#000"
    root.geometry("485x550+200+200")
    root.title("Калькулятор")
    root.resizable(False, False)
    app = Main(root)
    app.pack()
    root.mainloop()
