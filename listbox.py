from tkinter import *


janela = Tk()
janela.title("teste do app")
janela.geometry('500x300')
janela.configure(background='#dde')

lt_esporte=['skate','rock','pesca']

lb_esp=Listbox(janela)
for esportes in lt_esporte:
    lb_esp.insert(END,esportes)

lb_esp.pack()

janela.mainloop()