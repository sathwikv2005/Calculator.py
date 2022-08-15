from tkinter import *

operators = ['+','-','*','/']
def btnpress(n):
    try:
       text = Output.get()
       result = text + n
       if n in operators:
          lastletter = text[-1]
          if lastletter in operators:
            result = text[:-1] + n
       Output.delete(0,END)
       Output.insert(0,result)         
    except Exception: 
        Output.delete(0, END)
        Output.insert(0, 'Error! Enter a number please!')
        return



def clear():
    try:
       Output.delete(0,END)
       Output.insert(0,'')
    except Exception: 
        Output.delete(0, END)
        Output.insert(0, 'Error! Enter a number please!')
        return


def backspace():
    try:
       text = Output.get()[:-1]
       Output.delete(0,END)
       Output.insert(0,text)
    except Exception: 
        Output.delete(0, END)
        Output.insert(0, 'Error! Enter a number please!')
        return


def calculate():
    try:
        text1 = Output.get()
        result = eval(text1)
        Output.delete(0, END)
        Output.insert(0, result)
    except Exception:
        Output.delete(0, END)
        Output.insert(0, 'Error! Enter a number please!')
        return
    #logic =>

root = Tk()
root.title('Calculator')
root.geometry('500x220')

Output = Entry(root)
Output.config(bg='#58D3F7')
Output.place(x=150,y=10,width=215)


#row 1
btn7 = Button(root, width= 5, text='7', command=lambda:btnpress('7'))
btn7.config(bg='orange')
btn7.place(x=150,y=50)
btn8 = Button(root, width= 5, text='8', command=lambda:btnpress('8'))
btn8.config(bg='orange')
btn8.place(x=210,y=50)
btn9 = Button(root, width= 5, text='9', command=lambda:btnpress('9'))
btn9.config(bg='orange')
btn9.place(x=270,y=50)
btnd = Button(root, width= 5, text='/', command=lambda:btnpress('/'))
btnd.config(bg='orange')
btnd.place(x=320,y=50)

#row2
btn4 = Button(root, width= 5, text='4', command=lambda:btnpress('4'))
btn4.config(bg='orange')
btn4.place(x=150,y=80)
btn5 = Button(root, width= 5, text='5', command=lambda:btnpress('5'))
btn5.config(bg='orange')
btn5.place(x=210,y=80)
btn4 = Button(root, width= 5, text='4', command=lambda:btnpress('4'))
btn4.config(bg='orange')
btn4.place(x=270,y=80)
btnx = Button(root, width= 5, text='*', command=lambda:btnpress('*'))
btnx.config(bg='orange')
btnx.place(x=320,y=80)

#row3
btn1 = Button(root, width= 5, text='1', command=lambda:btnpress('1'))
btn1.config(bg='orange')
btn1.place(x=150,y=110)
btn2 = Button(root, width= 5, text='2', command=lambda:btnpress('2'))
btn2.config(bg='orange')
btn2.place(x=210,y=110)
btn3 = Button(root, width= 5, text='3', command=lambda:btnpress('3'))
btn3.config(bg='orange')
btn3.place(x=270,y=110)
btnmin = Button(root, width= 5, text='-', command=lambda:btnpress('-'))
btnmin.config(bg='orange')
btnmin.place(x=320,y=110)

#row4
btn00 = Button(root, width= 5, text='00', command=lambda:btnpress('00'))
btn00.config(bg='orange')
btn00.place(x=150,y=140)
btn0 = Button(root, width= 5, text='0', command=lambda:btnpress('0'))
btn0.config(bg='orange')
btn0.place(x=210,y=140)
btn02 = Button(root, width= 5, text='0', command=lambda:btnpress('0'))
btn02.config(bg='orange')
btn02.place(x=270,y=140)
btnplus = Button(root, width= 5, text='+', command=lambda:btnpress('+'))
btnplus.config(bg='orange')
btnplus.place(x=320,y=140)

#row5
bbtn = Button(root, text='Backspace', command=backspace)
bbtn.config(bg='red')
bbtn.place(x=150,y=180)
cbtn = Button(root, text='Clear', command=clear)
cbtn.config(bg='red')
cbtn.place(x=240,y=180)
cabtn = Button(root, text='Calculate!', command=calculate)
cabtn.config(bg='red')
cabtn.place(x=300,y=180)



root.mainloop()