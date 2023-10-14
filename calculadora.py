from tkinter import *

def acumulador(str):
    acumulador_string = ""
    string1 = str
    acumulador_string += string1
    print(acumulador_string)

   


janela = Tk()
janela.title("teste do app")
janela.geometry('350x500')
janela.configure(background='#dde')

f_numeros=Frame(janela,borderwidth=1,relief="sunken",background="#fff")
f_numeros.place(x=10,y=10,width=325,height=70)

Var1 = IntVar()

btn1 = Button(janela, text="1", command=lambda:acumulador("1"))
btn1.place(x=10, y=90, width=50, height=50)

btn1 = Button(janela, text="2")
btn1.place(x=60, y=90, width=50, height=50)

btn1 = Button(janela, text="3")
btn1.place(x=110, y=90, width=50, height=50)

btn1 = Button(janela, text="4")
btn1.place(x=10, y=140, width=50, height=50)

btn1 = Button(janela, text="5")
btn1.place(x=60, y=140, width=50, height=50)

btn1 = Button(janela, text="6")
btn1.place(x=110, y=140, width=50, height=50)

btn1 = Button(janela, text="7")
btn1.place(x=10, y=190, width=50, height=50)

btn1 = Button(janela, text="8")
btn1.place(x=60, y=190, width=50, height=50)

btn1 = Button(janela, text="9")
btn1.place(x=110, y=190, width=50, height=50)

btn1 = Button(janela, text="0")
btn1.place(x=60, y=240, width=50, height=50)


janela.mainloop()