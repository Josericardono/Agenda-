from tkinter import *
from tkinter import messagebox

class Cadastro:
    def __init__(self, master=None):
        self.master = master
        self.master.title("Cadastro de Usuário")
        self.master.geometry("400x300")  # Ajuste o tamanho da janela conforme necessário

        self.fontePadrao = ("Arial", "12")

        # Frame para a imagem
        self.janelaimg = Frame(master, padx=20, pady=5)
        self.janelaimg.pack()

        # Verifique se o caminho da imagem está correto
        self.img = PhotoImage(file="img/login.png")
        self.lblimg = Label(self.janelaimg, image=self.img)
        self.lblimg.pack()

        # Frame para o campo de usuário
        self.janela2 = Frame(master, padx=20)
        self.janela2.pack()

        self.nomeLabel = Label(self.janela2, text="Usuário:", font=self.fontePadrao, width=10)
        self.nomeLabel.pack(side=LEFT)
        self.nome = Entry(self.janela2, width=25, font=self.fontePadrao)
        self.nome.pack(side=LEFT)

        # Frame para o campo de senha
        self.janela3 = Frame(master, padx=20)
        self.janela3.pack()

        self.telLabel = Label(self.janela3, text="Senha:", font=self.fontePadrao, width=10)
        self.telLabel.pack(side=LEFT)
        self.tel = Entry(self.janela3, width=25, font=self.fontePadrao, show="*")  # Mostra a senha como asteriscos
        self.tel.pack(side=LEFT)

        # Frame para o botão
        self.janela4 = Frame(master, padx=20)
        self.janela4.pack()

        self.inserir = Button(self.janela4, text="Login", font=("Calibri", "12"), width=14, command=self.login)
        self.inserir.pack(side=LEFT)

    def login(self):
        usuario = self.nome.get()
        senha = self.tel.get()

        # Aqui você pode adicionar a lógica de autenticação com o banco de dados
        if usuario == "" or senha == "":
            messagebox.showwarning("Aviso", "Usuário e senha não podem estar vazios.")
        else:
            # Simulando uma verificação simples (substitua isso pela lógica real)
            if usuario == "admin" and senha == "admin":
                messagebox.showinfo("Sucesso", "Login bem-sucedido!")
            else:
                messagebox.showerror("Erro", "Usuário ou senha inválidos.")

if __name__ == "__main__":
    root = Tk()
    app = Cadastro(root)
    root.mainloop()
