from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import bancotree

def popular():
    tv.delete(*tv.get_children())
    vquery="SELECT * FROM tabela_dados order by ID"
    linhas=bancotree.dql(vquery)
    for i in linhas:
        tv.insert("","end",values=i)

def pesquisar():
    tv.delete(*tv.get_children())
    vquery="SELECT * FROM tabela_dados WHERE NOME LIKE '%"+pesq.get()+"%'"
    linhas=bancotree.dql(vquery)
    for i in linhas:
        tv.insert("","end",values=i)

def inserir():
    if vid.get() != "" and vn.get() != "" and  vf.get() != "":
        print("Dados gravados")
        vnome = vn.get()
        vidade = vid.get()
        vOBS = vf.get()
        vquery = "INSERT INTO tabela_dados (ID, NOME, TELEFONE) VALUES ('"+vidade+"', '"+vnome+"', '"+vOBS+"')"
        bancotree.dml(vquery) 
    else:
        print("ERRO")
    ############
    if vid.get() == "" or vn.get() == "" or  vf.get() == "":
        messagebox.showinfo(title="ERRO", message="campo não preencido")
        return
    popular()
    vid.delete(0,END)
    vn.delete(0,END)
    vf.delete(0,END)
    vid.focus()
        

def deletar():
    try:
        itemSele=tv.selection()[0]
        tv.delete(itemSele)
    except:
        messagebox.showinfo(title="ERRO", message="Selecione o elemento para deleta-lo")    

def obter():
    try:
        itemSele=tv.selection()[0]
        valores=tv.item(itemSele,"values")
        print(valores)
        #especifico print(valores[0,1 ou 2])
    except:
        messagebox.showinfo(title="ERRO", message="Selecione o elemento a ser obtido")        


janela = Tk()
janela.title("teste do app")
janela.geometry('420x350')
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

btn_in=Button(janela,text="inserir",command=inserir)
btn_in.grid(column=0,row=2)
btn_de=Button(janela,text="deletar",command=deletar)
btn_de.grid(column=1,row=2)
btn_ob=Button(janela,text="obter",command=obter)
btn_ob.grid(column=2,row=2)

btn_pe=Button(janela,text="pesquisar",command=pesquisar)
btn_pe.grid(column=1,row=4)
pesq = Entry(janela)
pesq.grid(column=2,row=4)

Button(janela,text="mostrar todos",command=popular).grid(column=0,row=4)


janela.mainloop()