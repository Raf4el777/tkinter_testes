from tkinter import *


janela = Tk()
janela.title("teste do app")
janela.geometry('500x300')
janela.configure(background='#dde')

Label(janela,text="valor").pack()

sc_escalo=Scale(janela,from_=0,to=100,orient=HORIZONTAL)
sc_escalo.pack()
sc_escalo.set(50)

janela.mainloop()