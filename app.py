from flask import Flask, render_template

app = Flask("Hello")  #cria um app

@app.route("/")  #rota raiz
@app.route("/hello")  #regisra uma rota e chama uma funçao def
def hello():
    return render_template("hello.html")
#def hello():
#    return "Hello Claire!!"

#TODO
#@app.route("/bye")
#def bye():
#   return render_template("bye.html")

#def bye():
#    return "BYE CLAIRE, BYE CLAIRE... BYE CLAIRE!!"    

