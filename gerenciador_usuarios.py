import sqlite3


class GerenciadorUsuarios:

    def __init__(self, nome_banco="usuarios.db"):
        self.nome_banco = nome_banco
        self._criar_tabela()

    def _criar_tabela(self):
        conexao = sqlite3.connect(self.nome_banco)
        conexao.execute("""
            CREATE TABLE IF NOT EXISTS usuario (
                id         INTEGER PRIMARY KEY AUTOINCREMENT,
                nome       TEXT NOT NULL,
                cpf        TEXT NOT NULL UNIQUE,
                idade      INTEGER NOT NULL,
                nascimento TEXT NOT NULL
            )
        """)
        conexao.commit()
        conexao.close()

    def inserir_usuario(self, nome, cpf, idade, nascimento):
        conexao = sqlite3.connect(self.nome_banco)
        conexao.execute(
            "INSERT INTO usuario (nome, cpf, idade, nascimento) VALUES (?, ?, ?, ?)",
            (nome, cpf, idade, nascimento)
        )
        conexao.commit()
        conexao.close()
        print(f"Usuário '{nome}' inserido com sucesso.")

    def listar_usuarios(self):
        conexao = sqlite3.connect(self.nome_banco)
        usuarios = conexao.execute("SELECT * FROM usuario").fetchall()
        conexao.close()

        if not usuarios:
            print("Nenhum usuário cadastrado.")
            return

        print(f"\n{'ID':<5} {'Nome':<25} {'CPF':<18} {'Idade':<7} {'Nascimento'}")
        print("-" * 65)
        for u in usuarios:
            print(f"{u[0]:<5} {u[1]:<25} {u[2]:<18} {u[3]:<7} {u[4]}")
        print()

    def deletar_usuario(self, usuario_id):
        conexao = sqlite3.connect(self.nome_banco)
        conexao.execute("DELETE FROM usuario WHERE id = ?", (usuario_id,))
        conexao.commit()
        conexao.close()
        print(f"Usuário com id={usuario_id} removido.")

    def popular_banco(self):
        usuarios = [
            ("Matheus", "111.222.333-44", 22, "2002-04-10"),
            ("Silva",   "222.333.444-55", 30, "1994-08-23"),
            ("Neymar",  "333.444.555-66", 32, "1992-02-05"),
            ("Messi",   "444.555.666-77", 36, "1987-06-24"),
        ]
        conexao = sqlite3.connect(self.nome_banco)
        conexao.executemany(
            "INSERT INTO usuario (nome, cpf, idade, nascimento) VALUES (?, ?, ?, ?)",
            usuarios
        )
        conexao.commit()
        conexao.close()
        print("Usuários inseridos com sucesso.")


db = GerenciadorUsuarios()
db.popular_banco()
db.listar_usuarios()
