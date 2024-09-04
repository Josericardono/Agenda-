from tkinter import *
from tkinter import ttk
from usuario import Usuarios  # Certifique-se de que o módulo usuario está correto

class Application:
    def __init__(self, master=None):
        self.master = master
        self.master.title("Formulário de Usuários")
        self.usuario = Usuarios()

        # Janela 1
        self.janela1 = Frame(master)
        self.janela1.pack(padx=10, pady=10)

        self.msg1 = Label(self.janela1, text="Informe os dados:")
        self.msg1["font"] = ("Verdana", "14", "bold")
        self.msg1.pack()

        # Janela 2
        self.janela2 = Frame(master)
        self.janela2["padx"] = 20
        self.janela2.pack()

        self.idusuario_label = Label(self.janela2, text="ID Usuário:")
        self.idusuario_label.pack(side="left")
        self.idusuario = Entry(self.janela2, width=20)
        self.idusuario.pack(side="left")

        self.busca = Button(self.janela2, text="Buscar", command=self.buscarUsuario)
        self.busca.pack()

        # Janela 3
        self.janela3 = Frame(master)
        self.janela3["padx"] = 20
        self.janela3.pack()

        self.nome_label = Label(self.janela3, text="Nome:")
        self.nome_label.pack(side="left")
        self.nome = Entry(self.janela3, width=20)
        self.nome.pack(side="left")

        # Janela 4
        self.janela4 = Frame(master)
        self.janela4["padx"] = 20
        self.janela4.pack()

        self.telefone_label = Label(self.janela4, text="Telefone:")
        self.telefone_label.pack(side="left")
        self.telefone = Entry(self.janela4, width=20)
        self.telefone.pack(side="left")

        # Janela 5
        self.janela5 = Frame(master)
        self.janela5["padx"] = 20
        self.janela5.pack()

        self.email_label = Label(self.janela5, text="Email:")
        self.email_label.pack(side="left")
        self.email = Entry(self.janela5, width=20)
        self.email.pack(side="left")

        # Janela 6
        self.janela6 = Frame(master)
        self.janela6["padx"] = 20
        self.janela6.pack()

        self.usuario_label = Label(self.janela6, text="Usuário:")
        self.usuario_label.pack(side="left")
        self.usuario_entry = Entry(self.janela6, width=20)
        self.usuario_entry.pack(side="left")

        # Janela 7
        self.janela7 = Frame(master)
        self.janela7["padx"] = 20
        self.janela7.pack()

        self.senha_label = Label(self.janela7, text="Senha:")
        self.senha_label.pack(side="left")
        self.senha = Entry(self.janela7, width=20)
        self.senha.pack(side="left")

        # Janela 8
        self.janela8 = Frame(master)
        self.janela8["padx"] = 20
        self.janela8.pack()

        self.autentic = Label(self.janela8, text="")
        self.autentic["font"] = ("Verdana", "10", "italic", "bold")
        self.autentic.pack()

        # Janela 9
        self.janela9 = Frame(master)
        self.janela9["padx"] = 20
        self.janela9.pack()

        self.botao = Button(self.janela9, width=10, text="Inserir", command=self.inserirUsuario)
        self.botao.pack(side="left")

        self.botao2 = Button(self.janela9, width=10, text="Alterar", command=self.alterarUsuario)
        self.botao2.pack(side="left")

        self.botao3 = Button(self.janela9, width=10, text="Excluir", command=self.excluirUsuario)
        self.botao3.pack(side="left")

        # Janela 10
        self.janela10 = Frame(master)
        self.janela10["padx"] = 20
        self.janela10.pack(pady=10)

        self.tree = ttk.Treeview(self.janela10, columns=("ID", "Nome", "Telefone", "Email", "Usuário"),
                                 show='headings')

        self.tree.heading("ID", text="ID")
        self.tree.heading("Nome", text="Nome")
        self.tree.heading("Telefone", text="Telefone")
        self.tree.heading("Email", text="Email")
        self.tree.heading("Usuário", text="Usuário")
        self.tree.pack()
        self.tree.bind("<<TreeviewSelect>>", self.selecionaUsuario)

        self.atualizarTabela()

    def selecionaUsuario(self, event):
        seleciona_item = self.tree.selection()
        if seleciona_item:
            item = seleciona_item[0]
            values = self.tree.item(item, 'values')
            self.idusuario.delete(0, END)
            self.idusuario.insert(INSERT, values[0])
            self.nome.delete(0, END)
            self.nome.insert(INSERT, values[1])
            self.telefone.delete(0, END)
            self.telefone.insert(INSERT, values[2])
            self.email.delete(0, END)
            self.email.insert(INSERT, values[3])
            self.usuario_entry.delete(0, END)
            self.usuario_entry.insert(INSERT, values[4])

    def atualizarTabela(self):
        try:
            usuarios = self.usuario.selectAllUsers()  # Chama o método sem argumentos
            self.tree.delete(*self.tree.get_children())
            for u in usuarios:
                self.tree.insert("", "end", values=(u[0], u[1], u[2], u[3], u[4]))
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao atualizar tabela: {e}")

    def buscarUsuario(self):
        user = Usuarios()
        idusuario = self.idusuario.get()
        resultado = user.selectUser(idusuario)
        if resultado:
            self.autentic["text"] = "Usuário encontrado"
            self.idusuario.delete(0, END)
            self.idusuario.insert(INSERT, resultado[0])
            self.nome.delete(0, END)
            self.nome.insert(INSERT, resultado[1])
            self.telefone.delete(0, END)
            self.telefone.insert(INSERT, resultado[2])
            self.email.delete(0, END)
            self.email.insert(INSERT, resultado[3])
            self.usuario_entry.delete(0, END)
            self.usuario_entry.insert(INSERT, resultado[4])
        else:
            self.autentic["text"] = "Usuário não encontrado"

    def inserirUsuario(self):
        self.usuario.nome = self.nome.get()
        self.usuario.telefone = self.telefone.get()
        self.usuario.email = self.email.get()
        self.usuario.usuario = self.usuario_entry.get()
        self.usuario.senha = self.senha.get()
        self.autentic["text"] = self.usuario.insertUser()
        self.limparCampos()
        self.atualizarTabela()

    def alterarUsuario(self):
        self.usuario.idusuario = self.idusuario.get()
        self.usuario.nome = self.nome.get()
        self.usuario.telefone = self.telefone.get()
        self.usuario.email = self.email.get()
        self.usuario.usuario = self.usuario_entry.get()
        self.usuario.senha = self.senha.get()
        self.autentic["text"] = self.usuario.updateUser()
        self.limparCampos()
        self.atualizarTabela()

    def excluirUsuario(self):
        self.usuario.idusuario = self.idusuario.get()
        self.autentic["text"] = self.usuario.deleteUser()
        self.limparCampos()
        self.atualizarTabela()

    def limparCampos(self):
        self.idusuario.delete(0, END)
        self.nome.delete(0, END)
        self.telefone.delete(0, END)
        self.email.delete(0, END)
        self.usuario_entry.delete(0, END)
        self.senha.delete(0, END)
        self.tree.delete(*self.tree.get_children())

if __name__ == "__main__":
    root = Tk()
    app = Application(root)
    root.mainloop()
