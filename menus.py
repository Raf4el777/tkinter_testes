from tkinter import *
import os

infoAPP=os.path.dirname(__file__)

def Semcomando():
    print("nada")

def novoContato():
    #abrin nova janela
    exec(open(infoAPP+"\\testes.py").read(),{'x':10})#passar parametros


janela = Tk()
janela.title("teste do app")
janela.geometry('900x600')
janela.configure(background='#dde')

barradeMenus = Menu(janela)
menuContatos=Menu(barradeMenus, tearoff=0)
menuContatos = Menu(barradeMenus)
menuContatos.add_command(label="Novo",command=novoContato)
menuContatos.add_command(label="Pesquisar",command=Semcomando)
menuContatos.add_command(label="Deletar",command=Semcomando)
menuContatos.add_separator()
menuContatos.add_command(label="Fechar",command=janela.quit)
barradeMenus.add_cascade(label="contatos",menu=menuContatos)

menuManutencao=Menu(barradeMenus,tearoff=0)
menuManutencao.add_command(label="Banco de Dados",command=Semcomando)
barradeMenus.add_cascade(label="Manutenção",menu=menuManutencao)

menuSobre=Menu(barradeMenus,tearoff=0)
menuSobre.add_command(label="Rafa",command=Semcomando)
barradeMenus.add_cascade(label="Sobre",menu=menuSobre)



janela.config(menu=barradeMenus)

janela.mainloop()