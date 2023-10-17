#Aplicativo de Gerenciamento de Tarefas: Crie um aplicativo que permite aos usuários 
#adicionar, editar e excluir tarefas.
#Você pode implementar recursos como categorização, data de vencimento e prioridade
from tkinter import *
from tkinter import ttk
import bancotarefas
from tkinter import messagebox


def add():
    import info_tarefas
    info_tarefas.inserir()

def popular():
    tv.delete(*tv.get_children())
    vquery="SELECT * FROM tabela order by data"
    linhas=bancotarefas.dql(vquery)
    for i in linhas:
        tv.insert("","end",values=i)    


def pesquisar():
    tv.delete(*tv.get_children())
    vquery="SELECT * FROM tabela WHERE descricao LIKE '%"+vpesq.get()+"%'"
    linhas=bancotarefas.dql(vquery)
    for i in linhas:
        tv.insert("","end",values=i)


def deletar():
    try:
        itemSele=tv.selection()[0]
        tv.delete(itemSele)
    except:
        messagebox.showinfo(title="ERRO", message="Selecione o elemento para deleta-lo")    

App = Tk()
App.title("Gerenciador de Tarefas")
App.geometry('700x400')
App.configure(background='#dde')

fr_quadro=Frame(App,borderwidth=1,relief="sunken",background="#fff")
#relief (flat,solid,suken,raised)
fr_quadro.place(x=5,y=5,width=150,height=700)

Label(fr_quadro,text="menu de terefas",font=("Arial", 15)).pack()

btn_Menu=Button(fr_quadro,text="Adicionar",font=("Arial", 20),relief="flat",background="#fff",command=add)
btn_Menu.pack()



btn_Menu=Button(fr_quadro,text="Excluir",font=("Arial", 20),relief="flat",background="#fff",command=deletar)
btn_Menu.pack()

tarefas = LabelFrame(App,text="Tarefas",borderwidth=1,relief="flat")
tarefas.place(x=200,y=20,width=500,height=250)
tv=ttk.Treeview(tarefas,columns=('data','descricao','nome'),show="headings")
tv.column('data',minwidth=0,width=100)
tv.column('nome',minwidth=0,width=70)
tv.column('descricao',minwidth=0,width=250)
tv.heading('data',text="DATA")
tv.heading('descricao',text="DESCRICAO")
tv.heading('nome',text="NOME")
tv.pack()

pesquisar_tarefa = LabelFrame(App,text="Pesquisar tarefas",borderwidth=1,relief="flat")
pesquisar_tarefa.place(x=200,y=290,width=450,height=75)
Button(pesquisar_tarefa,text="Pesqisar",command=pesquisar).grid(column=1,row=0)
vpesq=Entry(pesquisar_tarefa)
vpesq.grid(column=0,row=0,)
Button(pesquisar_tarefa,text="Mostrar todas",command=popular).grid(column=2,row=0)

App.mainloop()