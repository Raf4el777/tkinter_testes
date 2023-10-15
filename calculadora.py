from tkinter import *

def inserir(res):
    global numero
    global resu
    global outro
    if res == 0:
        print("")
        lb_num.delete(0,END)
        numero = 0
        resu = 0
        outro = 0
    elif res == "/":
        print("")
        numero = float(lb_num.get())
        print(numero)
        resu = 2
        if numero != False:  
            lb_num.delete(0,END)
    elif res == "+":
        print("")
        numero = float(lb_num.get())
        print(numero)
        resu = 1 
        if numero != False:
            lb_num.delete(0,END)      
    elif res == "-":
        print("")
        numero = float(lb_num.get())
        print(numero)
        resu = 3
        if numero != False:  
            lb_num.delete(0,END)
    elif res == "x":
        print("")  
        numero = float(lb_num.get())
        print(numero)
        resu = 4
        if numero != False:  
            lb_num.delete(0,END)
    elif res == 8:
        print("")
        numero = lb_num.get()
        lb_num.delete(0,END)
        lb_num.insert(0,numero + ".")         
    elif res == 1:
        print("") 
        outro = float(lb_num.get())
        print (outro) 
        if (outro != 0) and (numero != 0):
            total(outro,numero,resu)
    elif res == "0":
        numero = lb_num.get()
        lb_num.delete(0,END)
        lb_num.insert(0, numero + res)                
    else:
        print(res)
        lb_num.insert(res, res)
            


def total(vaolr1, valor, resu):
    global valortotal
    valortotal = 0
    if resu == 1:
        valortotal = vaolr1 + valor
    if resu == 2:
        valortotal = valor / vaolr1 
    if resu == 3:
        valortotal = valor - vaolr1     
    if resu == 4:
        valortotal = valor * vaolr1        
    resultado = str(valortotal)
    lb_num.delete(0, END)
    lb_num.insert(0,resultado)


janela = Tk()
janela.title("Calculadora")
janela.geometry('350x450')
janela.configure(background='#dde')

vnum = StringVar()

f_numeros=Frame(janela,borderwidth=1,relief="sunken",background="#fff")
f_numeros.place(x=10,y=10,width=325,height=70)
lb_num=Entry(f_numeros,textvariable=vnum, font=("Arial", 35), background="#fff", text= vnum)
lb_num.pack(side="left",fill=X,expand=True)

btn1 = Button(janela, text="1", command=lambda:inserir("1"))
btn1.place(x=15, y=90, width=75, height=75)

btn1 = Button(janela, text="2", command=lambda:inserir("2"))
btn1.place(x=90, y=90, width=75, height=75)

btn1 = Button(janela, text="3", command=lambda:inserir("3"))
btn1.place(x=165, y=90, width=75, height=75)

btn1 = Button(janela, text="4", command=lambda:inserir("4"))
btn1.place(x=15, y=166, width=75, height=75)

btn1 = Button(janela, text="5", command=lambda:inserir("5"))
btn1.place(x=90, y=166, width=75, height=75)

btn1 = Button(janela, text="6", command=lambda:inserir("6"))
btn1.place(x=165, y=166, width=75, height=75)

btn1 = Button(janela, text="7", command=lambda:inserir("7"))
btn1.place(x=15, y=241, width=75, height=75)

btn1 = Button(janela, text="8", command=lambda:inserir("8"))
btn1.place(x=90, y=241, width=75, height=75)

btn1 = Button(janela, text="9", command=lambda:inserir("9"))
btn1.place(x=165, y=241, width=75, height=75)

btn1 = Button(janela, text="0", command=lambda:inserir("0"))
btn1.place(x=90, y=316, width=75, height=75)

btn3 = Button(janela, text=".", command=lambda:inserir(8))
btn3.place(x=15, y=316, width=75, height=75)

btn4 = Button(janela, text="C", font="Arial",background="#fff", command=lambda:inserir(0))
btn4.place(x=165, y=316, width=75, height=75)

btn5 = Button(janela, text="=", font="Arial",background="#fff", command=lambda:inserir(1))
btn5.place(x=240, y=330, width=75, height=60)

btn2 = Button(janela, text="-", font="Arial",background="#fff", command=lambda:inserir("-"))
btn2.place(x=240, y=270, width=75, height=60)

btn2 = Button(janela, text="+", font="Arial",background="#fff", command=lambda:inserir("+"))
btn2.place(x=240, y=210, width=75, height=60)

btn2 = Button(janela, text="/", font="Arial",background="#fff", command=lambda:inserir("/"))
btn2.place(x=240, y=150, width=75, height=60)

btn2 = Button(janela, text="x", font="Arial",background="#fff", command=lambda:inserir("x"))
btn2.place(x=240, y=90, width=75, height=60)

janela.mainloop()