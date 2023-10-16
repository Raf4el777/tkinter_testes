from tkinter import *
from tkinter import ttk

def inserir():
    print()

def deletar():
    print()

def obter():
    print()    


janela = Tk()
janela.title("teste do app")
janela.geometry('600x300')
janela.configure(background='#dde')

lbid=Label(janela,text="ID",anchor=W)
lbid.grid(column=0,row=0)
vid=Entry(janela)
vid.grid(column=0,row=1)
lbn=Label(janela,text="NOME",anchor=W)
lbn.grid(column=1,row=0)
vn=Entry(janela)
vn.grid(column=1,row=1)
lbf=Label(janela,text="FONE",anchor=W)
lbf.grid(column=2,row=0)
vf=Entry(janela)
vf.grid(column=2,row=1)
tv=ttk.Treeview(janela,columns=('id','Name','tell'),show="headings")
tv.column('id',minwidth=0,width=50)
tv.column('Name',minwidth=0,width=250)
tv.column('tell',minwidth=0,width=100)
tv.heading('id',text="ID")
tv.heading('Name',text="NOME")
tv.heading('tell',text="TELEFONE")
tv.grid(column=0,row=3,columnspan=3,pady=5)

btn_in=Button(janela,text="iinserir",command=inserir)
btn_in.grid(column=0,row=2)
btn_de=Button(janela,text="deletar",command=deletar)
btn_de.grid(column=1,row=2)
btn_ob=Button(janela,text="obter",command=obter)
btn_ob.grid(column=2,row=2)


janela.mainloop()