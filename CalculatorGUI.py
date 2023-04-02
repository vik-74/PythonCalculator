from tkinter import *

root = Tk()
root.geometry("265x400")
root.title("Calculator")
root.config(background="Lightgreen")

expression = ""

result = StringVar()
expression_field = Entry(textvariable=result)
expression_field.grid(columnspan=4, ipadx=70)

def press_num(num):
    global expression
    expression += str(num)
    result.set(expression)

button1 = Button(text="1", height=1, width=7, command=lambda: press_num(1))
button1.grid(row=2, column=0)

button2 = Button(text="2", height=1, width=7, command=lambda: press_num(2))
button2.grid(row=2, column=1)

button3 = Button(text="3", height=1, width=7, command=lambda: press_num(3))
button3.grid(row=2, column=2)

button4 = Button(text="4", height=1, width=7, command=lambda: press_num(4))
button4.grid(row=3, column=0)

button5 = Button(text="5", height=1, width=7, command=lambda: press_num(5))
button5.grid(row=3, column=1)

button6 = Button(text="6", height=1, width=7, command=lambda: press_num(6))
button6.grid(row=3, column=2)

button7 = Button(text="7", height=1, width=7, command=lambda: press_num(7))
button7.grid(row=4, column=0)

button8 = Button(text="8", height=1, width=7, command=lambda: press_num(8))
button8.grid(row=4, column=1)

button9 = Button(text="9", height=1, width=7, command=lambda: press_num(9))
button9.grid(row=4, column=2)

plus = Button(text="+", height=1, width=7)
plus.grid(row=5, column=0)

button0 = Button(text="0", height=1, width=7)
button0.grid(row=5, column=1)

minus = Button(text="-", height=1, width=7)
minus.grid(row=5, column=2)

root.mainloop()