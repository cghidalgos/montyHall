from flask import Flask, render_template, request, session, redirect, url_for
import numpy as np
import random

app = Flask(__name__)
app.secret_key = "montyhall_secret_key"

def simul(ns):
    cont_high_prob = 0
    for _ in range(ns):
        first_choice = random.randint(1, 3)
        correct_door = random.randint(1, 3)
        
        remaining_doors = [door for door in [1, 2, 3] if door != correct_door]
        if first_choice in remaining_doors:
            remaining_doors.remove(first_choice)
        
        open_door = remaining_doors[0]
        second_choice = [door for door in [1, 2, 3] if door not in (first_choice, open_door)][0]

        if second_choice == correct_door:
            cont_high_prob += 1

    return round(cont_high_prob / ns, 4)

@app.route("/simu", methods=["GET", "POST"])
def simu():
    probability = None
    num_simulations = None
    
    if request.method == "POST":
        num_simulations = int(request.form["num_simulations"])
        probability = simul(num_simulations)

    return render_template("simu.html", probability=probability, num_simulations=num_simulations)


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        session["nombre"] = request.form["nombre"]

        session["juegos_totales"] = 0
        session["ganadas_cambiando"] = 0
        session["perdidas_cambiando"] = 0
        session["ganadas_sin_cambiar"] = 0
        session["perdidas_sin_cambiar"] = 0

        return redirect(url_for("juego"))
    
    return render_template("index.html")

@app.route("/juego", methods=["GET", "POST"])
def juego():
    if request.method == "POST":
        session["eleccion_inicial"] = int(request.form["puerta"])
        session["premio"] = random.randint(1, 3)

        puertas_posibles = [1, 2, 3]
        puertas_posibles.remove(session["premio"])
        if session["eleccion_inicial"] in puertas_posibles:
            puertas_posibles.remove(session["eleccion_inicial"])

        session["puerta_abierta"] = random.choice(puertas_posibles)
        return redirect(url_for("decision"))

    return render_template("juego.html",nombre=session["nombre"],)

@app.route("/decision", methods=["GET", "POST"])
def decision():
    if request.method == "POST":
        eleccion = request.form["decision"]

        if eleccion == "cambiar":
            opciones_restantes = [1, 2, 3]
            opciones_restantes.remove(session["eleccion_inicial"])
            opciones_restantes.remove(session["puerta_abierta"])
            session["eleccion_final"] = opciones_restantes[0]
        else:
            session["eleccion_final"] = session["eleccion_inicial"]

        return redirect(url_for("resultado"))

    return render_template("decision.html",
                           nombre=session["nombre"],
                           puerta_abierta=session["puerta_abierta"],
                           eleccion_inicial=session["eleccion_inicial"])

@app.route("/resultado")
def resultado():
    session["juegos_totales"] += 1 

    if session["eleccion_final"] == session["premio"]:
        ganaste = True
        if session["eleccion_final"] == session["eleccion_inicial"]:
            session["ganadas_sin_cambiar"] += 1
        else:
            session["ganadas_cambiando"] += 1
    else:
        ganaste = False
        if session["eleccion_final"] == session["eleccion_inicial"]:
            session["perdidas_sin_cambiar"] += 1
        else:
            session["perdidas_cambiando"] += 1

    return render_template("resultado.html",
                           nombre=session["nombre"],
                           ganaste=ganaste,
                           premio=session["premio"],
                           eleccion_final=session["eleccion_final"])

@app.route("/estadisticas")
def estadisticas():
    return render_template("estadisticas.html",
                           juegos_totales=session["juegos_totales"],
                           ganadas_cambiando=session["ganadas_cambiando"],
                           perdidas_cambiando=session["perdidas_cambiando"],
                           ganadas_sin_cambiar=session["ganadas_sin_cambiar"],
                           perdidas_sin_cambiar=session["perdidas_sin_cambiar"])

@app.route("/reiniciar", methods=["POST"])
def reiniciar():
    nombre = session.get("nombre")
    juegos_totales = session.get("juegos_totales")
    ganadas_cambiando = session.get("ganadas_cambiando")
    perdidas_cambiando = session.get("perdidas_cambiando")
    ganadas_sin_cambiar = session.get("ganadas_sin_cambiar")
    perdidas_sin_cambiar = session.get("perdidas_sin_cambiar")
    session.clear()
    session["nombre"] = nombre
    session["juegos_totales"] = juegos_totales
    session["ganadas_cambiando"] = ganadas_cambiando
    session["perdidas_cambiando"] = perdidas_cambiando
    session["ganadas_sin_cambiar"] = ganadas_sin_cambiar
    session["perdidas_sin_cambiar"] = perdidas_sin_cambiar
    return redirect("/juego")

if __name__ == "__main__":
    app.run(debug=True)
