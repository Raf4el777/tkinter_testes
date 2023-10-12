from tkinter import *

def imprimir():
    ve=vesport.get()
    if ve == "futebol":
        print(ve)
    elif ve == "basquete":
        print(ve)
    elif ve == "volei":
        print(ve)
    else:
        print("seleciona algo") 

janela = Tk()
janela.title("teste do app")
janela.geometry('400x400')
janela.configure(background='#dde')

listaEsportes = ['futebol','volei','basquete']
vesport=StringVar()
vesport.set(listaEsportes[0])

op_menu_esports=OptionMenu(janela,vesport,*listaEsportes)
op_menu_esports.pack()

bot=Button(janela,text="imprimir",command=imprimir)
bot.pack()

janela.mainloop()