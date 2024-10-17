import tkinter as tk
def calculate():
    number1 = float(tbxNumber1.get())
    number2 = float(tbxNumber2.get())
    lblResult["text"] = number1 + number2
window = tk.Tk()
window.title("Calculator")
lblNumber1 = tk.Label(window, text="Enter a number:")
tbxNumber1 = tk.Entry(window)
lblNumber2 = tk.Label(window, text="Enter another number:")
tbxNumber2 = tk.Entry(window)
btnCalculate = tk.Button(window, text="Calculate", command=calculate)
lblResult = tk.Label(window)
lblNumber1.grid(column=0, row=0)
tbxNumber1.grid(column=1, row=0)
lblNumber2.grid(column=0, row=1)
tbxNumber2.grid(column=1, row=1)
btnCalculate.grid(column=0, row=2)
lblResult.grid(column=1, row=2)
window.mainloop()

