from flask import Flask, render_template, request
import numpy as np
import random

app = Flask(__name__)

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

@app.route("/", methods=["GET", "POST"])
def index():
    probability = None
    num_simulations = None
    
    if request.method == "POST":
        num_simulations = int(request.form["num_simulations"])
        probability = simul(num_simulations)

    return render_template("index.html", probability=probability, num_simulations=num_simulations)

if __name__ == "__main__":
    app.run(debug=True)
