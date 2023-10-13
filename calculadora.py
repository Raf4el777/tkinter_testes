from tkinter import *

def calculadora(numero, operação):
    print(operação)
    print(numero)

janela = Tk()
janela.title("teste do app")
janela.geometry('350x500')
janela.configure(background='#dde')

f_numeros=Frame(janela,borderwidth=1,relief="sunken",background="#fff")
f_numeros.place(x=10,y=10,width=325,height=70)

btn1 = Button(janela, text="1", command= lambda:calculadora(1, 0))
btn1.place(x=10, y=90, width=50, height=50)


janela.mainloop()