#Aplicativo de Gerenciamento de Tarefas: Crie um aplicativo que permite aos usuários 
#adicionar, editar e excluir tarefas.
#Você pode implementar recursos como categorização, data de vencimento e prioridade
from tkinter import *

App = Tk()
App.title("Gerenciador de Tarefas")
App.geometry('350x250')
App.configure(background='#dde')

Label(App,text="Data de inicio").place(x=10,y=5)
en_inicio=Entry(App)
en_inicio.place(x=10,y=30,width=200,height=20)
Label(App,text="Data de termino").place(x=10,y=55)
en_fim=Entry(App)
en_fim.place(x=10,y=80,width=200,height=20)
Label(App,text="Descrição da tarefa").place(x=10,y=105)
en_tarefa = Text(App)
en_tarefa.place(x=10,y=130,width=300,height=100)


App.mainloop()