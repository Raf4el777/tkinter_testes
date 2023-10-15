from tkinter import *
from tkinter import ttk

def printa():
    ve=cb_esportes.get()
    print(ve)

janela = Tk()
janela.title("teste do app")
janela.geometry('500x300')
janela.configure(background='#dde')

listEsports=['Futebol','Volei','basquete']

lb_esports=Label(janela,text="Esportes")
lb_esports.pack()

cb_esportes=ttk.Combobox(janela,values=listEsports)
cb_esportes.set("Futebol")
cb_esportes.pack()
Button(janela,text="imprimir",command=printa).pack()


janela.mainloop()