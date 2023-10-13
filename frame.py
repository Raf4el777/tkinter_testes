from tkinter import *
from tkinter import messagebox

def mostrarMgs():
    messagebox.showinfo(title="informação",message='informação teste')
          
janela = Tk()
janela.title("teste do app")
janela.geometry('400x400')

vnum_ctext=StringVar()

fr_quadro=Frame(janela,borderwidth=1,relief="sunken",background="#325")
#relief (flat,solid,suken,raised)
fr_quadro.place(x=10,y=10,width=300,height=150)

Label(fr_quadro,text="tipo de caixa (1, 2, 3)").pack()
tb_num=Entry(fr_quadro,textvariable=vnum_ctext)
vnum_ctext.set("1")
tb_num.pack()

btn_msg=Button(fr_quadro,text="entrada",command=mostrarMgs)
btn_msg.pack()


qt=Button(janela,text="sair",command=quit)
qt.place(x=40,y=170)

janela.mainloop()