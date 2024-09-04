from Banco import Banco

class Usuarios:
    def __init__(self, idusuario=0, nome="", telefone="", email="", usuario="", senha=""):
        self.banco = Banco()  # Usa a conexão do banco diretamente na instância da classe
        self.idusuario = idusuario
        self.nome = nome
        self.telefone = telefone
        self.email = email
        self.usuario = usuario
        self.senha = senha

    def insertUser(self):
        try:
            c = self.banco.conexao.cursor()
            c.execute(
                "INSERT INTO tbl_usuarios (nome, telefone, email, usuario, senha) VALUES (?, ?, ?, ?, ?)",
                (self.nome, self.telefone, self.email, self.usuario, self.senha)
            )
            self.banco.conexao.commit()
            c.close()
            return "Usuário cadastrado com sucesso!"
        except Exception as e:
            return f"Ocorreu um erro na inserção do usuário: {e}"

    def updateUser(self):
        try:
            c = self.banco.conexao.cursor()
            c.execute(
                "UPDATE tbl_usuarios SET nome = ?, telefone = ?, email = ?, usuario = ?, senha = ? WHERE idusuario = ?",
                (self.nome, self.telefone, self.email, self.usuario, self.senha, self.idusuario)
            )
            self.banco.conexao.commit()
            c.close()
            return "Usuário atualizado com sucesso!"
        except Exception as e:
            return f"Ocorreu um erro na alteração do usuário: {e}"

    def deleteUser(self):
        try:
            c = self.banco.conexao.cursor()
            c.execute("DELETE FROM tbl_usuarios WHERE idusuario = ?", (self.idusuario,))
            self.banco.conexao.commit()
            c.close()
            return "Usuário excluído com sucesso!"
        except Exception as e:
            return f"Ocorreu um erro na exclusão do usuário: {e}"

    def selectUser(self, idusuario):
        try:
            c = self.banco.conexao.cursor()
            c.execute("SELECT * FROM tbl_usuarios WHERE idusuario = ?", (idusuario,))
            linha = c.fetchone()
            c.close()
            if linha:
                self.idusuario = linha[0]
                self.nome = linha[1]
                self.telefone = linha[2]
                self.email = linha[3]
                self.usuario = linha[4]
                self.senha = linha[5]
                return linha
            else:
                return None
        except Exception as e:
            raise RuntimeError(f"Ocorreu um erro na busca do usuário: {e}")

    def selectAllUsers(self):
        try:
            c = self.banco.conexao.cursor()
            c.execute("SELECT * FROM tbl_usuarios")
            linhas = c.fetchall()
            c.close()
            return linhas
        except Exception as e:
            raise RuntimeError(f"Ocorreu um erro na recuperação dos usuários: {e}")
