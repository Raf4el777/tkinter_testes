#Aplicativo de Gerenciamento de Tarefas: Crie um aplicativo que permite aos usuários 
#adicionar, editar e excluir tarefas.
#Você pode implementar recursos como categorização, data de vencimento e prioridade
from tkinter import *

App = Tk()
App.title("Gerenciador de Tarefas")
App.geometry('1480x720')
App.configure(background='#dde')

fr_quadro=Frame(App,borderwidth=1,relief="sunken",background="#fff")
#relief (flat,solid,suken,raised)
fr_quadro.place(x=5,y=5,width=150,height=700)

Label(fr_quadro,text="menu de terefas",font=("Arial", 15)).pack()

btn_Menu=Button(fr_quadro,text="Adicionar",font=("Arial", 20),relief="flat",background="#fff")
btn_Menu.pack()

btn_Menu=Button(fr_quadro,text="Editar",font=("Arial", 20),relief="flat",background="#fff")
btn_Menu.pack()

btn_Menu=Button(fr_quadro,text="Excluir",font=("Arial", 20),relief="flat",background="#fff")
btn_Menu.pack()

App.mainloop()