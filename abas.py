from tkinter import *
from tkinter import ttk

janela = Tk()
janela.title("teste do app")
janela.geometry('500x300')
janela.configure(background='#dde')

nb=ttk.Notebook(janela)
nb.place(x=0,y=0,width=500,height=300)

tbl=Frame(nb)
tb2=Frame(nb)
nb.add(tbl,text="Aba1")
nb.add(tb2,text="Aba2")
Button(tbl,text="teste").pack()
Button(tb2,text="teste").pack()

janela.mainloop()