import tkinter as tk

# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


def get_values():
    num1 = int(number1_entry.get())
    num2 = int(number2_entry.get())
    return num1, num2


def insert_values(value):
    answer_entry.delete(0, 'end')
    answer_entry.insert(0, value)


def add():
    num1, num2 = get_values()
    res = num1 + num2
    insert_values(res)


def sub():
    num1, num2 = get_values()
    res = num1 - num2
    insert_values(res)


def div():
    num1, num2 = get_values()
    res = num1 / num2
    insert_values(res)


def mul():
    num1, num2 = get_values()
    res = num1 * num2
    insert_values(res)


def mod():
    num1, num2 = get_values()
    res = num1 % num2
    insert_values(res)


window = tk.Tk()
window.title('Калькулятор')
window.geometry("415x400")
window.resizable(False, False)
button_add = tk.Button(window, text="+\nSum", width=3, height=2, command=add)
button_add.place(x=25, y=200)
button_sub = tk.Button(window, text="-\nSub", width=3, height=2, command=sub)
button_sub.place(x=100, y=200)
button_mul = tk.Button(window, text="*\nMul", width=3, height=2, command=mul)
button_mul.place(x=175, y=200)
button_div = tk.Button(window, text="/\nDiv", width=3, height=2, command=div)
button_div.place(x=250, y=200)
button_mod = tk.Button(window, text="%\nRemains ", width=4, height=2, command=mod)
button_mod.place(x=325, y=200)
number1_entry = tk.Entry(window, width=44)
number1_entry.place(x=25, y=75)
number2_entry = tk.Entry(window, width=44)
number2_entry.place(x=25, y=150)
answer_entry = tk.Entry(window, width=44)
answer_entry.place(x=25, y=300)
number1 = tk.Label(window, text="Введите первое число:")
number1.place(x=50, y=50)
number2 = tk.Label(window, text="Введите второе число:")
number2.place(x=50, y=125)
answer = tk.Label(window, text="Ответ:")
answer.place(x=50, y=275)
window.mainloop()

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
