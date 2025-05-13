# Importamos las clases y funciones necesarias de Flask
from flask import Flask, render_template, request, redirect, url_for, session, flash
import os  # Para generar una clave secreta segura

# Creamos una instancia de la aplicación Flask
app = Flask(__name__)

# Configuramos una clave secreta aleatoria para las sesiones
# os.urandom(24) genera 24 bytes aleatorios (mucho más seguro que una cadena fija)
app.secret_key = os.urandom(24)

# Definimos la ruta principal ("/") que responde a peticiones GET por defecto
@app.route("/")
def inicio():
    # Renderiza la plantilla HTML 'inicio.html'
    return render_template("inicio.html")

# Ruta para mostrar el formulario (GET)
@app.route("/formulario")
def formulario():
    # Renderiza la plantilla 'formulario.html'
    return render_template("formulario.html")

# Ruta para procesar el formulario (solo acepta POST)
@app.route("/procesar", methods=['POST'])
def procesar():
    # Verificamos si todos los campos requeridos están presentes en el formulario
    if not all([request.form.get('pais'), request.form.get('capital'), request.form.get('email')]):
        # Mostramos un mensaje flash de error si faltan campos
        flash("Por favor complete todos los campos", "error")
        # Redirigimos de vuelta al formulario
        return redirect(url_for('formulario'))

    # Actualizamos la sesión con los datos del formulario
    session.update({
        "pais": request.form.get("pais"),      # Obtenemos el país del formulario
        "capital": request.form.get("capital"), # Obtenemos la capital del formulario
        "email": request.form.get("email")      # Obtenemos el email del formulario
    })

    # Redirigimos a la página de resultados
    return redirect(url_for("mostrar_resultado"))

# Ruta para mostrar los resultados (GET)
@app.route("/resultado")
def mostrar_resultado():
    # Verificamos si todos los datos requeridos están en la sesión
    if not all(key in session for key in ['pais', 'capital', 'email']):
        # Si faltan datos, redirigimos al formulario
        return redirect(url_for('formulario'))

    # Renderizamos la plantilla 'resultado.html' pasando los datos de la sesión
    return render_template("resultado.html", session_data=session)

# Punto de entrada principal (solo se ejecuta si este archivo es el principal)
if __name__ == "__main__":
    # Ejecutamos la aplicación en modo debug (muestra errores detallados)
    app.run(debug=True)