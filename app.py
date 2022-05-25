from flask import Flask, render_template, g
import sqlite3

DATABASE = "banco.bd"     #caminho pro bancodedadosBD
SECRET_KEY = "chavedobd"  #senha secreta do BD

app = Flask("Hello")      #cria um app
app.config.from_object(__name__)

def conecta_bd():
    return sqlite3.connect(DATABASE)

#ABRE/FECHA A CONECÇAO  COM O BANCO
@app.before_request    
def antes_requisicao():
    g.bd = conecta_bd()

@app.teardown_request
def depois_requesiçao(e):
    g.bd.close() 


@app.route("/")       #rota raiz
def exibir_entradas():    
    sql = "SELECT titulo, texto, criado_em FROM entradas ORDER BY id DESC"
    cur = g.bd.execute(sql)
    entradas = []
    for titulo, texto, criado_em in cur.fetchall():
        entradas.append({"titulo": titulo, "texto": texto, "criado_em": criado_em})
    return render_template("layout.html", entradas=entradas)



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

