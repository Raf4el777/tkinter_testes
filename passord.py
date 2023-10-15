from tkinter import *

def impSenha():
    print("Senha digitado:"+vsenha.get())

janela = Tk()
janela.title("teste do app")
janela.geometry('500x300')
janela.configure(background='#dde')

vsenha = StringVar()

p_senha = Entry(janela,textvariable=vsenha,show="*")
p_senha.pack()

Button(janela,text="Mostrar",command=impSenha).pack()

janela.mainloop()