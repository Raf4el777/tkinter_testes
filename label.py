from tkinter import *
import os

pastaApp=os.path.dirname(__file__)

janela = Tk()
janela.title("teste do app")
janela.geometry('680x350')
janela.configure(background='#dde')

lb_frame=Frame(janela,borderwidth=1,relief="sunken",background="#dde")
lb_frame.place(x=10,y=10,width=300,height=150)

lb = Label(lb_frame,text="testes no label",background="#007",foreground="#fff",font=("Arial", 15))
lb.pack(side="left",fill=X, expand=True)
#eu coloquei uma foto
img_logo = PhotoImage(file=pastaApp+"\\giphy.gif")
lb_foto=Label(janela,image=img_logo)
lb_foto.pack(side="right")
janela.mainloop()