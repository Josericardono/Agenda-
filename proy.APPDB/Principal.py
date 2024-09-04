import tkinter
from tkinter import *

class menu:
    def __init__(self,master=None):
        self.janela = Frame(master)
        self.fontePadrao = ("arial", "12")
        self.janela.pack()
        self.titulo = Label(self.janela, text="Agenda")
        self.titulo["font"] = ("Arial", 20, "bold")
        self.titulo.pack()

        self.usuarios = Button(self.janela)
        self.usuarios.pack (sid=LEFT)
        self.usuarios["text"] = "Usuários"
        self.usuarios["font"] = ("Calibri", "12")
        self.usuarios["width"] = 14
        self.usuarios.pack()

        self.cidades = Button(self.janela)
        self.cidades.pack(sid=LEFT)
        self.cidades["text"] = "Cidades"
        self.cidades["font"] = ("Calibri", "12")
        self.cidades["width"] = 14
        self.cidades.pack()

        self.clientes = Button(self.janela)
        self.clientes.pack(sid=LEFT)
        self.clientes["text"] = "Clientes"
        self.clientes["font"] = ("Calibri", "12")
        self.clientes["width"] = 14
        self.clientes.pack()

        self.fechar = Button(self.janela)
        self.fechar.pack(sid=LEFT)
        self.fechar["text"] = "Fechar"
        self.fechar["font"] = ("Calibri", "12")
        self.fechar["width"] = 14
        self.fechar.pack()


root = Tk()
menu(root)
root.mainloop()