#Aplicativo de Gerenciamento de Tarefas: Crie um aplicativo que permite aos usuários 
#adicionar, editar e excluir tarefas.
#Você pode implementar recursos como categorização, data de vencimento e prioridade
from tkinter import *
import bancotarefas
from tkinter import  messagebox


def inserir():
    if en_data.get() != "" and en_data.get() != "// | //" and en_tarefa.get('1.0', END) != "" and  en_fim.get() != "":
        print("Dados gravados")
        vdat = en_data.get()
        vnome = en_tarefa.get('1.0', END)
        vdesq = en_fim.get()
        vquery = "INSERT INTO tabela (data, descricao, nome) VALUES ('"+vdat+"', '"+vdesq+"', '"+vnome+"')"
        bancotarefas.dml(vquery) 
    else:
        print("ERRO")
    ############
    if en_data.get() == "" or en_fim.get() == "" or  en_tarefa.get('1.0', END) == "":
        messagebox.showinfo(title="ERRO", message="campo não preencido")
        return
    en_data.delete(0,END)
    en_tarefa.delete('1.0',END)
    en_fim.delete(0,END)
    en_data.focus()

App = Tk()
App.title("Gerenciador de Tarefas")
App.geometry('350x250')
App.configure(background='#dde')

vdata = StringVar()
Label(App,text="Data de inicio | data de termino").place(x=10,y=5)
en_data=Entry(App,textvariable=vdata)
en_data.place(x=10,y=30,width=200,height=20)
vdata.set("// | //")

Label(App,text="Nome da tarefa").place(x=10,y=55)
en_fim=Entry(App)
en_fim.place(x=10,y=80,width=200,height=20)
Label(App,text="Descricao da tarefa").place(x=10,y=105)
en_tarefa = Text(App)
en_tarefa.place(x=10,y=130,width=300,height=100)

btn = Button(App,text="Inserir",command=inserir)
btn.place(x=250,y=50)

App.mainloop()