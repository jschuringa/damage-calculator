from flask import Flask, request, abort, render_template
from flask_bootstrap import Bootstrap
from weapon.weapon import Axe, Mace, Sword

app = Flask(__name__, template_folder= "templates")
app.debug = True
boostrap = Bootstrap(app)

@app.route("/")
def home():
    return render_template("dmgform.html")

@app.route('/get_damage', methods=['POST'])
def get_damage_information():
    wep_type = request.form["wepType"]
    min_dmg = int(request.form["minDmg"])
    max_dmg = int(request.form["maxDmg"])
    wep_str = int(request.form["wepStr"])
    ele_type = request.form["eleType"]
    ele_dmg = int(request.form["eleDmg"])
    pc_lvl = int(request.form["level"])
    
    wep = None
    if wep_type == "mace":
        wep = Mace(min_dmg, max_dmg, wep_str, ele_type, ele_dmg)
    elif wep_type == "axe":
        wep  = Axe(min_dmg, max_dmg, wep_str, ele_type, ele_dmg)
    elif wep_type == "sword":
        wep = Sword(min_dmg, max_dmg, wep_str, ele_type, ele_dmg)
    else:
        abort("400", "Invalid weapon type specified.")
    
    return render_template("dmgresults.html", attacks=wep.get_damage_dict(pc_lvl))