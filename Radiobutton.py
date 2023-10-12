from tkinter import *
def imprimir():
    ve=vesport.get()
    if ve == "f":
        print(ve)
    elif ve == "b":
        print(ve)
    elif ve == "v":
        print(ve)
    else:
        print("seleciona algo")    


janela = Tk()
janela.title("teste do app")
janela.geometry('900x600')
janela.configure(background='#dde')

vesport=StringVar()
vecor=StringVar()



lb_esportes=Label(janela,text="Esportes")
lb_esportes.pack()

rb_futebol=Radiobutton(janela,text="Futebol",value="f",variable=vesport)
rb_futebol.pack()

rb_Basquete=Radiobutton(janela,text="Basquete",value="b",variable=vesport)
rb_Basquete.pack()

rb_Volei=Radiobutton(janela,text="Volei",value="v",variable=vesport)
rb_Volei.pack()

btn_Sport=Button(janela,text="esprte selecionado", command=imprimir)
btn_Sport.pack()

lb_cores=Label(janela,text="Selecionar cores")
lb_cores.pack()

rb_verde=Radiobutton(janela,text="verde",value="#0f0",variable=vecor)
rb_verde.pack()

rb_vermelho=Radiobutton(janela,text="vermelho",value="# f00",variable=vecor)
rb_vermelho.pack()

btn_cores=Button(janela,text="cocr selecionada", command=imprimir)
btn_cores.pack()

janela.mainloop()