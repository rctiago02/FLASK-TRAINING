from flask import Flask, render_template, request, redirect,url_for

app = Flask(__name__)

diccionario = {}

@app.route("/")
def home():
    return render_template("inicio.html")



@app.route("/formulario")
def mostrar_formulario():
    return render_template("formulario.html")

@app.route("/procesar", methods=["POST"])
def procesar_formulario():
    nombre = request.form.get("nombre")
    apellido = request.form.get("apellido")
    email = request.form.get("email")

    diccionario["nombre"] = nombre
    diccionario["apellido"] = apellido
    diccionario["email"] = email
    print("Datos recibidos:", diccionario)
    return redirect(url_for("mostrar_resultados"))

@app.route("/mostrar_resultados")
def mostrar_resultados():
    return render_template("mostrar_resultados.html", diccionario_en_html=diccionario)


@app.route("/saludo/<nombre>")
def saludar(nombre):
    return f"<h1>Hola, {diccionario["nombre"]}!</h1><h2>Llena el formulario para que salude a otra persona</h2><a href='/'><button type='button'>Ir al comienzo</button></a>"


print(diccionario)

if __name__ == "__main__":
    app.run(debug=True)