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


def Clear():
   result=""
   int(e1.delete(0,END)) 
   int(e2.delete(0,END)) 
   resultText.set(result)


gui =Tk()
gui.title("Calculator")
gui.configure(bg="orange")

gui_width = 300
gui_height = 200

# get the screen dimension
screen_width = gui.winfo_screenwidth()
screen_height = gui.winfo_screenheight()

# find the center point
center_x = int(screen_width/2 - gui_width / 2)
center_y = int(screen_height/2 - gui_height / 2)

# set the position of the window to the center of the screen
gui.geometry(f'{gui_width}x{gui_height}+{center_x}+{center_y}')
gui.resizable(False,False)
gui.attributes('-alpha',0.9)  #transparency of the screen
#gui.geometry("300x200")

resultText = StringVar()
Label(gui, text ="Number 1").place(x=10,y=10)
Label(gui, text ="Number 2").place(x=10,y=40)
Label(gui, text ="Result:").place(x=10,y=60)

e1 =Entry(gui)
e1.place(x=100,y=10)
e2 =Entry(gui)
e2.place(x=100,y=40)

result = Label(gui, text="", textvariable=resultText).place(x=100,y=60)

Button(gui, text="+",command =Add, height=1,width=2).place(x=10,y=100)
Button(gui, text="-",command =Minus, height=1,width=2).place(x=40,y=100)
Button(gui, text="*",command =Multiplication, height=1,width=2).place(x=80,y=100)
Button(gui, text="/",command =Div, height=1,width=2).place(x=120,y=100)
Button(gui, text="C",command =Clear, height=1,width=2).place(x=160,y=100)

Number1 =Entry(gui)
Number2 =Entry(gui)

gui.mainloop()




