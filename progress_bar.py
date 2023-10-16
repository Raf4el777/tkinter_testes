from tkinter import *
from tkinter import ttk
def valBARRA(m):
    cont=0
    etapas=m/100
    while cont<etapas:
        cont=cont+1
        i=0
        while i<1000000:
            i=i+1    
        valor.set(cont)
        janela.update()    
    

janela = Tk()
janela.title("teste do app")
janela.geometry('500x300')
janela.configure(background='#dde')
valor=DoubleVar()
valor.set(0)
pb=ttk.Progressbar(janela,variable=valor,maximum=100)
pb.pack()
btn=Button(janela,text="prencher",command=valBARRA(10000))
btn.pack()

#feature kkk

janela.mainloop()