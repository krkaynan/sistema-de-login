from flask import Flask, render_template, request, redirect, url_for, flash
import sqlite3

app = Flask(__name__)
app.secret_key = 'sua_chave_secreta'

class BackEnd:
    def conecta_db(self):
        try:
            self.conn = sqlite3.connect("Sistema_cadastros.db")
            self.cursor = self.conn.cursor()
        except Exception as e:
            return str(e)

    def desconecta_db(self):
        self.conn.close()

    def cria_tabela(self):
        self.conecta_db()
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS Usuarios(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                Username TEXT NOT NULL,
                Email TEXT NOT NULL,
                Senha TEXT NOT NULL,
                Confirma_Senha TEXT NOT NULL
            );
        """)
        self.conn.commit()
        self.desconecta_db()

    def cadastrar_usuario(self, username, email, senha, confirma_senha):
        try:
            self.conecta_db()
            if not username or not email or not senha or not confirma_senha:
                raise ValueError("Todos os campos devem ser preenchidos.")
            if len(username) < 3:
                raise ValueError("O nome de usuário deve ter pelo menos 3 caracteres.")
            if len(senha) < 3:
                raise ValueError("A senha deve ter pelo menos 3 caracteres.")
            if senha != confirma_senha:
                raise ValueError("As senhas não correspondem.")
            
            self.cursor.execute("INSERT INTO Usuarios (Username, Email, Senha, Confirma_Senha) VALUES (?, ?, ?, ?)",
                                (username, email, senha, confirma_senha))
            self.conn.commit()
            self.desconecta_db()
            return True
        except ValueError as e:
            self.desconecta_db()
            return str(e)
        except Exception as e:
            self.desconecta_db()
            return str(e)

    def verifica_login(self, username, senha):
        self.conecta_db()
        self.cursor.execute("SELECT * FROM Usuarios WHERE Username = ? AND Senha = ?", (username, senha))
        user = self.cursor.fetchone()
        self.desconecta_db()
        return user


# Criar a tabela ao iniciar a aplicação
def init_db():
    backend = BackEnd()
    backend.cria_tabela()

# Rota de login
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        senha = request.form["senha"]
        backend = BackEnd()
        user = backend.verifica_login(username, senha)
        if user:
            flash(f"Bem-vindo, {username}!", "success")
            return redirect(url_for("login"))
        else:
            flash("Dados de login incorretos.", "error")
    return render_template("login.html")

# Rota de cadastro
@app.route("/cadastro", methods=["GET", "POST"])
def cadastro():
    if request.method == "POST":
        username = request.form["username"]
        email = request.form["email"]
        senha = request.form["senha"]
        confirma_senha = request.form["confirma_senha"]
        backend = BackEnd()
        resultado = backend.cadastrar_usuario(username, email, senha, confirma_senha)
        if resultado is True:
            flash(f"{username}, seu cadastro foi realizado com sucesso!", "success")
            return redirect(url_for("login"))
        else:
            flash(resultado, "error")
    return render_template("cadastro.html")

if __name__ == "__main__":
    # Inicializar banco de dados antes de rodar a aplicação
    init_db()
    
    app.run(debug=True)
