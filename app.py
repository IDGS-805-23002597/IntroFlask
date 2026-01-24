from flask import Flask, render_template,request

app = Flask(__name__)

@app.route("/")
def index():
    titulo="Flask IDGS-805"
    lista=["JUAN","PEDRO","MARIO"]
    return render_template("index.html",titulo=titulo,lista=lista)

@app.route("/alumnos")
def alumnos():
    return render_template("alumnos.html")

@app.route("/usuarios")
def usuarios():
    return render_template("usuarios.html")


@app.route("/hola")
def hola():
    return "<h1>---Hola Nuevo---</h1>"

@app.route("/user/<int:id>/<string:name>")
def user(id, name):
    return "ID {} NOMBRE: {}".format(id, name)

@app.route("/formulario")
def formulario():
    return '''
       <form>
        <label for="name">Name:</label>
        <input type="text" id="name" name="name" required>

        <label for="name">apaterno:</label>
        <input type="text" id="name" name="name" required>
    </form>

'''
@app.route("/operasBas", methods=["GET","POST"])
def opera1():
    res=0
    if request.method=="POST":
        n1=request.form.get("n1")
        n2=request.form.get("n2")
        res=int(n1)+int(n2)
    return render_template("operasBas.html", res=res)

@app.route("/resultado", methods=["GET","POST"])
def resultado():
    n1=request.form.get("n1")
    n2=request.form.get("n2")
    res=int(n1)+int(n2)
    return "La suma de {} + {} = {}".format(n1,n2,res)


if __name__ == '__main__':
    app.run(debug=True)