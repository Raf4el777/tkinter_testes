from tkinter import *


janela = Tk()
janela.title("teste do app")
janela.geometry('500x300')
janela.configure(background='#dde')

lbf_esp=LabelFrame(janela,text="Esportes",borderwidth=1,relief="flat")
lbf_esp.place(x=10,y=10,width=300,height=100)

Label(lbf_esp,text="Futebol").pack()

Label(lbf_esp,text="basquete").pack()

Label(lbf_esp,text="volei").pack()

janela.mainloop()