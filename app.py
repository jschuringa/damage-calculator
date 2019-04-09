from flask import Flask, request, abort, render_template
from flask_bootstrap import Bootstrap
from wtforms import Form, SelectField, IntegerField, validators, ValidationError
from weapon.weapon import Axe, Mace, Sword

app = Flask(__name__, template_folder= "templates")
app.debug = True
boostrap = Bootstrap(app)

@app.route("/")
def home():
    form = DamageForm()
    return render_template("dmgform.html", form=form)

@app.route('/get_damage', methods=['POST'])
def get_damage_information():
    form = DamageForm(request.form)
    if request.method == 'POST' and form.validate():
        wep = None
        wep_type = form.wep_type.data

        if wep_type == "mace":
            wep = Mace(form.min_dmg.data, form.max_dmg.data, form.wep_str.data, form.ele_type.data, form.ele_dmg.data)
        elif wep_type == "axe":
            wep  = Axe(form.min_dmg.data, form.max_dmg.data, form.wep_str.data, form.ele_type.data, form.ele_dmg.data)
        elif wep_type == "sword":
            wep = Sword(form.min_dmg.data, form.max_dmg.data, form.wep_str.data, form.ele_type.data, form.ele_dmg.data)

        return render_template("dmgresults.html", attacks=wep.get_damage_dict(form.pc_lvl.data))
    return render_template('dmgform.html', form=form)


def validate_min_max(form, field):
    if(field.data < form.min_dmg.data):
        raise ValidationError("Max damage must be greater than min damage.")

def validate_ele_dmg(form, field):
    if isinstance(field.data,int) and field.data != 0 and (field.data < 5 or field.data > 15):
        raise ValidationError("Element damage must be 0 or between 5 and 15.")

class DamageForm(Form):
    wep_type = SelectField(
        'Weapon Type',
        choices=[("mace", "Mace"), ("axe", "Axe"), ("sword", "Sword")], 
        validators=[validators.DataRequired()])
    min_dmg = IntegerField('Minimum Damage', [validators.DataRequired()])
    max_dmg = IntegerField('Maximum Damage', [validators.DataRequired(), validate_min_max])
    wep_str = IntegerField('Weapon Strength', [validators.DataRequired()])
    ele_type = SelectField(
        'Element Type',
        choices=[("physical", "Physical"), ("fire", "Fire"), ("ice", "Ice")], 
        validators=[validators.DataRequired()])
    ele_dmg = IntegerField('Element Damage', [validators.InputRequired(), validate_ele_dmg])
    pc_lvl = IntegerField('Character Level', [validators.DataRequired()])
