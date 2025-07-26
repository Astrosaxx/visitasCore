from flask import Flask, render_template, redirect, request, session

app = Flask(__name__)
app.secret_key = '12rhc01298120c4981' 

@app.route("/", methods=["GET"])
def index():
    if 'visitas' not in session:
        session['visitas'] = 0
    if 'reinicios' not in session:
        session['reinicios'] = 0

    return render_template("index.html", visitas=session['visitas'], reinicios=session['reinicios'])

@app.route("/sumar", methods=["POST"])
def sumar():
    session['visitas'] = session.get('visitas', 0) + 1
    return redirect("/")

@app.route("/sumar2", methods=["POST"])
def sumar2():
    session['visitas'] = session.get('visitas', 0) + 2
    return redirect("/")

@app.route("/sumar_personalizado", methods=["POST"])
def sumar_personalizado():
    cantidad = int(request.form.get("cantidad", 0))
    session['visitas'] = session.get('visitas', 0) + cantidad
    return redirect("/")

@app.route("/reiniciar", methods=["POST"])
def reiniciar():
    session['visitas'] = 0
    session['reinicios'] = session.get('reinicios', 0) + 1
    return redirect("/")

@app.route("/destruir_sesion")
def destruir_sesion():
    session.clear()
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)
