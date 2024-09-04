from Banco import Banco

class Cidades:
    def __init__(self, idcidade=0, cidade="", uf=""):
        self.banco = Banco()
        self.idcidade = idcidade
        self.cidade = cidade
        self.uf = uf

    def insertCidade(self):
        try:
            c = self.banco.conexao.cursor()
            c.execute("INSERT INTO tbl_cidades (cidade, uf) VALUES (?, ?)",
                      (self.cidade, self.uf))
            self.banco.conexao.commit()
            c.close()
            return "Cidade inserida com sucesso!"
        except Exception as e:
            return f"Erro ao inserir cidade: {e}"

    def updateCidade(self):
        try:
            c = self.banco.conexao.cursor()
            c.execute("UPDATE tbl_cidades SET cidade = ?, uf = ? WHERE idcidade = ?",
                      (self.cidade, self.uf, self.idcidade))
            self.banco.conexao.commit()
            c.close()
            return "Cidade atualizada com sucesso!"
        except Exception as e:
            return f"Erro ao atualizar cidade: {e}"

    def deleteCidade(self):
        try:
            c = self.banco.conexao.cursor()
            c.execute("DELETE FROM tbl_cidades WHERE idcidade = ?", (self.idcidade,))
            self.banco.conexao.commit()
            c.close()
            return "Cidade excluída com sucesso!"
        except Exception as e:
            return f"Erro ao excluir cidade: {e}"

    def selectCidade(self, idcidade):
        try:
            c = self.banco.conexao.cursor()
            c.execute("SELECT * FROM tbl_cidades WHERE idcidade = ?", (idcidade,))
            linha = c.fetchone()
            c.close()
            if linha:
                self.idcidade = linha[0]
                self.cidade = linha[1]
                self.uf = linha[2]
                return linha
            else:
                return None
        except Exception as e:
            raise RuntimeError(f"Erro ao buscar cidade: {e}")

    def selectAllCidades(self):
        try:
            c = self.banco.conexao.cursor()
            c.execute("SELECT * FROM tbl_cidades")
            linhas = c.fetchall()
            c.close()
            return linhas
        except Exception as e:
            raise RuntimeError(f"Erro ao recuperar cidades: {e}")
