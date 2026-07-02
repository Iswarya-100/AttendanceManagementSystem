import pandas as pd
from flask import Flask, render_template, request, redirect, url_for

STUDENTS = pd.read_csv("data/students.csv").to_dict(orient="series")
RNOS = STUDENTS["Roll Number"].values
NAMES = STUDENTS["Student Name"].values
nos = []

app = Flask(__name__)

@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")

@app.route("/", methods=["POST"])
def take_attendance():
    return render_template("take_attendance.html", NAMES=NAMES, RNOS=RNOS)
    
    
@app.route("/get_details", methods=["GET", "POST"])
def get_details():
    no = request.form.get("no")
    if no:
        nos.append(no)
    if request.form.get("is_complete") == "complete":
        return render_template("report.html", nos=nos)
    return render_template("take_attendance.html", NAMES=NAMES, RNOS=RNOS)
    
