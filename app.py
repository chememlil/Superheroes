from flask import Flask, jsonify, request, abort
from flask_migrate import Migrate
from extensions import db
from models import Hero, Power, HeroPower

app = Flask(__name__)

# Configure the database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///instance/heroes.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the extensions after app is configured
db.init_app(app)
migrate = Migrate(app, db)

# GET /heroes - Return list of heroes
@app.route('/heroes', methods=['GET'])
def get_heroes():
    heroes = Hero.query.all()
    heroes_data = [{'id': hero.id, 'name': hero.name, 'super_name': hero.super_name} for hero in heroes]
    return jsonify(heroes_data), 200

# GET /heroes/:id - Return hero with powers or 404
@app.route('/heroes/<int:id>', methods=['GET'])
def get_hero(id):
    hero = Hero.query.get(id)
    if not hero:
        return jsonify({"error": "Hero not found"}), 404
    
    hero_powers = [
        {
            'hero_id': hp.hero_id,
            'id': hp.id,
            'power': {
                'id': hp.power.id,
                'name': hp.power.name,
                'description': hp.power.description
            },
            'power_id': hp.power_id,
            'strength': hp.strength
        }
        for hp in hero.hero_powers
    ]
    hero_data = {
        'id': hero.id,
        'name': hero.name,
        'super_name': hero.super_name,
        'hero_powers': hero_powers
    }
    return jsonify(hero_data), 200

# GET /powers - Return list of powers
@app.route('/powers', methods=['GET'])
def get_powers():
    powers = Power.query.all()
    powers_data = [{'id': power.id, 'name': power.name, 'description': power.description} for power in powers]
    return jsonify(powers_data), 200

# GET /powers/:id - Return power by id or 404
@app.route('/powers/<int:id>', methods=['GET'])
def get_power(id):
    power = Power.query.get(id)
    if not power:
        return jsonify({"error": "Power not found"}), 404
    power_data = {
        'id': power.id,
        'name': power.name,
        'description': power.description
    }
    return jsonify(power_data), 200

# PATCH /powers/:id - Update power description or return 404/validation error
@app.route('/powers/<int:id>', methods=['PATCH'])
def update_power(id):
    power = Power.query.get(id)
    if not power:
        return jsonify({"error": "Power not found"}), 404

    data = request.get_json()
    if 'description' not in data or not isinstance(data['description'], str):
        return jsonify({"errors": ["validation errors"]}), 400
    
    power.description = data['description']
    db.session.commit()
    
    updated_power = {
        'id': power.id,
        'name': power.name,
        'description': power.description
    }
    return jsonify(updated_power), 200

# POST /hero_powers - Create new HeroPower or return validation error
@app.route('/hero_powers', methods=['POST'])
def create_hero_power():
    data = request.get_json()
    
    if not all(key in data for key in ['strength', 'power_id', 'hero_id']):
        return jsonify({"errors": ["validation errors"]}), 400
    
    hero = Hero.query.get(data['hero_id'])
    power = Power.query.get(data['power_id'])
    
    if not hero or not power:
        return jsonify({"errors": ["validation errors"]}), 400
    
    hero_power = HeroPower(strength=data['strength'], hero_id=hero.id, power_id=power.id)
    db.session.add(hero_power)
    db.session.commit()
    
    hero_power_data = {
        'id': hero_power.id,
        'hero_id': hero.id,
        'power_id': power.id,
        'strength': hero_power.strength,
        'hero': {
            'id': hero.id,
            'name': hero.name,
            'super_name': hero.super_name
        },
        'power': {
            'id': power.id,
            'name': power.name,
            'description': power.description
        }
    }
    return jsonify(hero_power_data), 201

@app.route('/')
def index():
    return 'Hello, Hero World!'

if __name__ == '__main__':
    app.run(debug=True, port=5003)
