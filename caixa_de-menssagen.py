from tkinter import *
from tkinter import messagebox

def mostrarMgs(tipomsg,msg):
    if (tipomsg == '1'):
        messagebox.showinfo(title='informação',message=msg)
    elif (tipomsg == '2'):
        messagebox.showwarning(title='aviso',message=msg)
    elif (tipomsg == '3'):
        messagebox.showerror(title='Erro',message=msg) 
    else:
        messagebox.showerror(title='Error 404',message="digite 1 2 ou 3")       

def msgReset():
    res=messagebox.askyesno("resetar?","tem certeza que quer resetar?")
    if(res==True):
        tb_num.delete(0,END) 
        tb_num.insert(0,"1")       

vnum_msg="test menssagebox"

janela = Tk()
janela.title("teste do app")
janela.geometry('400x400')

vnum_ctext=StringVar()


Label(janela,text="tipo de caixa (1, 2, 3)").pack()
tb_num=Entry(janela,textvariable=vnum_ctext)
vnum_ctext.set("1")
tb_num.pack()

btn_msg=Button(janela,text="entrada",command=lambda:mostrarMgs(vnum_ctext.get(),vnum_msg))
btn_msg.pack()

btn_res=Button(janela,text="Resetar",command=msgReset)
btn_res.pack()

Button(janela,text="sair",command=quit).pack()

janela.mainloop()