from flask import Flask, jsonify, request

from config import config
from models import db, Invitado


def create_app(enviroment):
    app = Flask(__name__)

    app.config.from_object(enviroment)

    with app.app_context():
        db.init_app(app)
        db.create_all()

    return app


enviroment = config['development']
app = create_app(enviroment)


@app.route('/invitados/', methods=['POST'])
def create_invitados():
    json = request.get_json(force=True)

    if json.get('nombre') is None:
        return jsonify({'message': 'Bad request'}), 400

    invitado = Invitado.create(json['nombre'])

    return jsonify({'invitado': invitado.json()})



@app.route('/invitados', methods=['GET'])
def get_invitados():
    invitados = [invitado.json() for invitado in Invitado.query.all()]
    return jsonify({'invitados': invitados})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
