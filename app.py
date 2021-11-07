# -*- coding: utf-8 -*-
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_restful import Api

app = Flask(__name__)
api = Api(app)
app.config.from_pyfile('config.cfg')
db = SQLAlchemy(app)

from models.beer import *
from models.ingredient import *

migrate = Migrate(app, db)

from controllers.index import *
from controllers.beercontroller import *

api.add_resource(Index, '/')
# GET all beers
api.add_resource(BeersController, '/example/rest/v1/beers')
# # GET, PUT and DELETE one beer by id
api.add_resource(BeerControllerById, '/example/rest/v1/beer/<int:id>')
# # POST beer (Create beer or new beer)
api.add_resource(BeerController, '/example/rest/v1/beer')


from seeders.beerseed import BeerSeed


@app.cli.command("seed")
def create_beers():
    """
        Define seed command, run in terminal:
        $ flask seed
    """
    BeerSeed.create()


@app.errorhandler(404)
def invalid_route(e):
    """
        Define custom 404 in json when not exist route
    """
    return jsonify({
        'errorCode': 404,
        'message': 'Route not found'
    })
