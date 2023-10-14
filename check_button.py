from tkinter import *

def futebolClick():
    print("")

def basqueteClick():
    print("")

def voleiClick():
    print("")        

janela = Tk()
janela.title("teste do app")
janela.geometry('400x400')

vfutebol=StringVar()
v_volei=StringVar()
vbasquete=StringVar()

fr_quadro=Frame(janela,borderwidth=1,relief="solid",background="#fff")
fr_quadro.place(x=10,y=10,width=300,height=150)

cb_futebol=Checkbutton(fr_quadro,text='futebol',variable=vfutebol,onvalue="s",offvalue="n",command=futebolClick)
cb_futebol.pack(side="left")

cb_volei=Checkbutton(fr_quadro,text='volei',variable=v_volei,onvalue="s",offvalue="n",command=voleiClick)
cb_volei.pack(side="left")

cb_basquete=Checkbutton(fr_quadro,text='basquete',variable=vbasquete,onvalue="s",offvalue="n",command=basqueteClick)
cb_basquete.pack(side="left")

janela.mainloop()