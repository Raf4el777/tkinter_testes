from tkinter import *
import banco
#print(x)
def gravardados():
    if tb_nome.get() != "":
        print("Dados gravados")
        vnome = tb_nome.get()
        vidade = tb_idade.get()
        vOBS = tb_OBS.get('1.0', END)
        vquery = "INSERT INTO tb_usuarios (nome, idade, OBS) VALUES ('"+vnome+"', '"+vidade+"', '"+vOBS+"')"
        banco.dml(vquery)
        tb_nome.delete(0,END)
        tb_idade.delete(0,END)
        tb_OBS.delete("1.0",END)
    else:
        print("ERRO")



janela = Tk()
janela.title("teste do app")
janela.geometry('900x600')
janela.configure(background='#dde')
Label(janela,background='#fff',text='nome').place(x=10,y=10)
tb_nome = Entry(janela)
tb_nome.place(x=10,y=30,width=200,height=20)
Label(janela,background='#fff',text='idade').place(x=10,y=60)
tb_idade = Entry(janela)
tb_idade.place(x=10,y=80,width=100,height=20)
Label(janela,background='#fff',text='OBS').place(x=10,y=100)
tb_OBS = Text(janela)
tb_OBS.place(x=10,y=120,width=200,height=80)
Button(janela, text='gravar', command= gravardados ).place(x=10,y=250)
Button(janela, text='sair', command=janela.destroy).place(x=80,y=250)
janela.mainloop()