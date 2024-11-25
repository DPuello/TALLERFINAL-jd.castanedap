from flask import Blueprint, render_template, jsonify
from models.huron import Huron
from models.boa_constrictor import BoaConstrictor
from models.perro import Perro
from models.gato import Gato


app_blueprint = Blueprint('app', __name__)


@app_blueprint.route('/')
def index():
    return render_template('index.html')


@app_blueprint.route('/huron')
def huron():
    huron1 = Huron("Huron", 10, 100, "México", 1000)
    return jsonify(sonido=huron1.hacer_sonido(), animal="Huron")


@app_blueprint.route('/boa_constrictor')
def boa_constrictor():
    boa_constrictor1 = BoaConstrictor(
        "Boa Constrictor", 10, 100, "México", 1000, 0)
    return jsonify(sonido=boa_constrictor1.hacer_sonido(),
                   animal="Boa Constrictor")


@app_blueprint.route('/perro')
def perro():
    perro1 = Perro("Perro", 10, 100)
    return jsonify(sonido=perro1.hacer_sonido(), animal="Perro")


@app_blueprint.route('/gato')
def gato():
    gato1 = Gato("Gato", 10, 100)
    return jsonify(sonido=gato1.hacer_sonido(), animal="Gato")
