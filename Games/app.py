from flask import Flask
from flask import render_template, redirect, request
import os

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/setup", methods=["GET", "POST"])
def setup():

    if request.method == "POST":

        gen = request.form["gen_field"]
        score = request.form["score_field"]
        speed = request.form["speed_field"]
        line = request.form["line"]
        save = request.form["save"]

        os.system(f"python Flappy.py {save} {gen} {score} {speed} {line}")

        return redirect("http://127.0.0.1:5000", code=302)

    return redirect("http://127.0.0.1:5000", code=302)

if __name__ == "__main__":
    app.run()