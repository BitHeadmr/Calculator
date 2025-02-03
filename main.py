import tkinter
from tkinter import *
from tkinter import messagebox

root = tkinter.Tk()
root.geometry("250x400+300+300")
root.resizable(0,0)
root.title("Calculator")

val = ""
A = 0
operator = ""


def btn1isclicked():
    global val
    val = val + "1"
    data.set(val)

def btn2isclicked():
    global val
    val = val + "2"
    data.set(val)

def btn3isclicked():
    global val
    val = val + "3"
    data.set(val)

def btn4isclicked():
    global val
    val = val + "4"
    data.set(val)

def btn5isclicked():
    global val
    val = val + "5"
    data.set(val)

def btn6isclicked():
    global val
    val = val + "6"
    data.set(val)

def btn7isclicked():
    global val
    val = val + "7"
    data.set(val)

def btn8isclicked():
    global val
    val = val + "8"
    data.set(val)

def btn9isclicked():
    global val
    val = val + "9"
    data.set(val)

def btn0isclicked():
    global val
    val = val + "0"
    data.set(val)

def btnplusclicked():
    global A
    global operator,val
    A = int(val)
    operator = "+"
    val = val + "+"
    data.set(val)

def btnminusclicked():
    global A
    global operator,val
    A = int(val)
    operator = "-"
    val = val + "-"
    data.set(val)

def btnmultclicked():
    global A
    global operator,val
    A = int(val)
    operator = "*"
    val = val + "*"
    data.set(val)

def btndivclicked():
    global A
    global operator,val
    A = int(val)
    operator = "/"
    val = val + "/"
    data.set(val)

def btnacpressed():
    global A,operator,val
    val = ""
    A = 0
    operator = ""
    data.set(val)

def result():
    global A,operator,val
    val2 = val
    if operator == "+":
        x = int((val2.split("+")[1]))
        C = A + x
        val = str(C)
        data.set(val)
    if operator == "-":
        x = int((val2.split("-")[1]))
        C = A - x
        val = str(C)
        data.set(val)
    if operator == "*":
        x = int((val2.split("*")[1]))
        C = A * x
        val = str(C)
        data.set(val)
    if operator == "/":
        x = int((val2.split("/")[1]))
        if x == 0:
            messagebox.showerror("Error", "Division By 0 Not Supported")
            A = ""
            val = ""
            data.set(val)
        else:
            C = int(A / x)
            data.set(C)

data = StringVar()
lbl = Label(
    root,
    text = "Label",
    anchor = SE,
    font = ("Verdana", 20),
    textvariable = data,
    background = "#000000",
    fg = "#FFFFFF",
)
lbl.pack(expand = True, fill = "both")

btnrow1 = Frame(root)
btnrow1.pack(expand = True, fill = "both")

btnrow2 = Frame(root)
btnrow2.pack(expand = True, fill = "both")

btnrow3 = Frame(root)
btnrow3.pack(expand = True, fill = "both")

btnrow4 = Frame(root)
btnrow4.pack(expand = True, fill = "both")


btn1 = Button(
    btnrow1,
    text = "1",
    font = ("Verdana", 22),
    relief = GROOVE,
    border = 0,
    command = btn1isclicked,
)
btn1.pack(side = LEFT, expand = True, fill = "both",)

btn2 = Button(
    btnrow1,
    text = "2",
    font = ("Verdana", 22),
    relief = GROOVE,
    border = 0,
    command = btn2isclicked,
)
btn2.pack(side = LEFT, expand = True, fill = "both",)

btn3 = Button(
    btnrow1,
    text = "3",
    font = ("Verdana", 22),
    relief = GROOVE,
    border = 0,
    command = btn3isclicked,
)
btn3.pack(side = LEFT, expand = True, fill = "both",)

btnplus = Button(
    btnrow1,
    text = "+",
    font = ("Verdana", 22),
    relief = GROOVE,
    border = 0,
    command = btnplusclicked,
)
btnplus.pack(side = LEFT, expand = True, fill = "both",)


btn4 = Button(
    btnrow2,
    text = "4",
    font = ("Verdana", 22),
    relief = GROOVE,
    border = 0,
    command = btn4isclicked,
)
btn4.pack(side = LEFT, expand = True, fill = "both",)

btn5 = Button(
    btnrow2,
    text = "5",
    font = ("Verdana", 22),
    relief = GROOVE,
    border = 0,
    command = btn5isclicked,
)
btn5.pack(side = LEFT, expand = True, fill = "both",)

btn6 = Button(
    btnrow2,
    text = "6",
    font = ("Verdana", 22),
    relief = GROOVE,
    border = 0,
    command = btn6isclicked,
)
btn6.pack(side = LEFT, expand = True, fill = "both",)

btnminus = Button(
    btnrow2,
    text = "-",
    font = ("Verdana", 22),
    relief = GROOVE,
    border = 0,
    command = btnminusclicked,
)
btnminus.pack(side = LEFT, expand = True, fill = "both",)


btn7 = Button(
    btnrow3,
    text = "7",
    font = ("Verdana", 22),
    relief = GROOVE,
    border = 0,
    command = btn7isclicked,
)
btn7.pack(side = LEFT, expand = True, fill = "both",)

btn8 = Button(
    btnrow3,
    text = "8",
    font = ("Verdana", 22),
    relief = GROOVE,
    border = 0,
    command = btn8isclicked,
)
btn8.pack(side = LEFT, expand = True, fill = "both",)

btn9 = Button(
    btnrow3,
    text = "9",
    font = ("Verdana", 22),
    relief = GROOVE,
    border = 0,
    command = btn9isclicked,
)
btn9.pack(side = LEFT, expand = True, fill = "both",)

btnmult = Button(
    btnrow3,
    text = "*",
    font = ("Verdana", 22),
    relief = GROOVE,
    border = 0,
    command = btnmultclicked,
)
btnmult.pack(side = LEFT, expand = True, fill = "both",)



btnc = Button(
    btnrow4,
    text = "AC",
    font = ("Verdana", 22),
    relief = GROOVE,
    border = 0,
    command = btnacpressed(),
)
btnc.pack(side = LEFT, expand = True, fill = "both",)

btn0 = Button(
    btnrow4,
    text = "0",
    font = ("Verdana", 22),
    relief = GROOVE,
    border = 0,
    command = btn0isclicked,
)
btn0.pack(side = LEFT, expand = True, fill = "both",)

btnequal = Button(
    btnrow4,
    text = "=",
    font = ("Verdana", 22),
    relief = GROOVE,
    border = 0,
    command = result,
)
btnequal.pack(side = LEFT, expand = True, fill = "both",)

btndiv = Button(
    btnrow4,
    text = "/",
    font = ("Verdana", 22),
    relief = GROOVE,
    border = 0,
    command = btndivclicked,
)
btndiv.pack(side = LEFT, expand = True, fill = "both",)

root.mainloop()