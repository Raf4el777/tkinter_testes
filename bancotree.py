import sqlite3
from sqlite3 import Error
import os

infoAPP=os.path.dirname(__file__)
nomeBanco=infoAPP+"\\banco2.db"

def conexao():
    con = None
    try:
        con = sqlite3.connect(nomeBanco)
    except   Error as ex:    
        print(ex)
    return con

def dql(query): #selet
    vcon= conexao()
    c=vcon.cursor()
    c.execute(query)    
    res=c.fetchall()
    vcon.close
    return res

def dml(query): #insert, update, delet
    try:
        vcon= conexao()
        c=vcon.cursor()
        c.execute(query)
        vcon.commit()
        vcon.close()
    except Error as ex:
        print(ex)