from tkinter import *


janela = Tk()
janela.title("teste do app")
janela.geometry('500x300')
janela.configure(background='#dde')

sp_box = Spinbox(janela,from_=1,to=10)
sp_box.pack()

janela.mainloop()