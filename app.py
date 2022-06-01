from flask import Flask, render_template, g, request, flash, session, redirect, url_for, abort
import sqlite3

DATABASE = "banco.bd"     #caminho pro bancodedadosBD
SECRET_KEY = "chavedobd"  #senha secreta do BD

app = Flask("Hello")      #cria um app
app.config.from_object(__name__)

def conecta_bd():
    return sqlite3.connect(DATABASE)

#ABRE/FECHA A CONEXAO  COM O BANCO
@app.before_request    
def antes_requisicao():
    g.bd = conecta_bd()

@app.teardown_request
def depois_requesiçao(e):
    g.bd.close() 


@app.route("/")       #ROTA RAIZ
def exibir_entradas():    
    sql = "SELECT titulo, texto, criado_em FROM entradas ORDER BY id DESC"
    cur = g.bd.execute(sql)
    entradas = []
    for titulo, texto, criado_em in cur.fetchall():
        entradas.append({"titulo": titulo, "texto": texto, "criado_em": criado_em})
    return render_template("exibir_entradas.html", entradas=entradas)


#OUTRAS ROTAS
@app.route('/inserir', methods=["POST"])
def inserir_entradas():
    if not session.get('logado'):
        abort(401)
    titulo = request.form['titulo']
    texto = request.form['texto']
    sql = "INSERT INTO entradas(titulo, texto) VALUES (?, ?)"
    g.bd.execute(sql, [titulo, texto]) 
    g.bd.commit()  
    flash("Nova entrada gravada com Sucesso!")
    return redirect(url_for("exibir_entradas"))



@app.route('/login', methods=["GET", "POST"])
def login():
    erro = None
    if request.method == "POST":
        if request.form['username'] == "admin" and request.form['password'] == "admin":
            session['logado'] = True
            flash("Login Successfully!")
            return redirect(url_for('exibir_entradas'))
        erro = "Usuário ou Senha inválidos"
    return render_template("login.html", erro=erro)   


@app.route('/logout')
def logout():
    session.pop('logado', None)
    flash("You're now Logout!")
    return redirect(url_for("exibir_entradas")) 



#rota com o site da claire PRIMEIRO TESTE DE SITE
@app.route('/hello')   
def hello():
    return render_template("hello.html")









#TESTES ANTERIORES

#@app.route("/hello")  #regisra uma rota e chama uma funçao def
#def hello():
#    return render_template("hello.html")



#def hello():
#    return "Hello Claire!!"

#TODO
#@app.route("/bye")
#def bye():
#   return render_template("bye.html")

#def bye():
#    return "BYE CLAIRE, BYE CLAIRE... BYE CLAIRE!!"    

