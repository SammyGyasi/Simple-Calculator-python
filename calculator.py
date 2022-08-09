from tkinter import *
from tokenize import Number


global e1
global e2
global resultText

def Add():
    result =int(e1.get()) + int(e2.get())
    resultText.set(result)


def Minus():
    result =int(e1.get()) - int(e2.get())
    resultText.set(result)



def Multiplication():
    result =int(e1.get()) * int(e2.get())
    resultText.set(result)


def Div():
    result =int(e1.get()) / int(e2.get())
    resultText.set(result)


root =Tk()
root.title("Calculator")
root.geometry("300x200")

resultText = StringVar()
Label(root, text ="Number 1").place(x=10,y=10)
Label(root, text ="Number 2").place(x=10,y=40)
Label(root, text ="Result:").place(x=10,y=60)

e1 =Entry(root)
e1.place(x=100,y=10)
e2 =Entry(root)
e2.place(x=100,y=40)

result = Label(root, text="", textvariable=resultText).place(x=100,y=80)

Button(root, text="+",command =Add, height=1,width=2).place(x=10,y=100)
Button(root, text="-",command =Minus, height=1,width=2).place(x=40,y=100)
Button(root, text="*",command =Multiplication, height=1,width=2).place(x=80,y=100)
Button(root, text="/",command =Div, height=1,width=2).place(x=120,y=100)

Number1 =Entry(root)
Number2 =Entry(root)

root.mainloop()




