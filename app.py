from flask import Flask, request, abort, render_template
from flask_bootstrap import Bootstrap
from weapon import weapon

app = Flas(__name__)
bootstrap = Bootstrap(app)

@app.route('/')
def home():
    return render_template('form.html')

@app.route('/get_damage', methods=['POST'])
def get_damage_information():
    minDmg = request.form["minDmg"]
    maxDmg = request.form["maxDmg"]
    wepStr = request.form["wepStr"]
    