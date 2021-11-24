# -*- coding: utf-8 -*-
from app import api, app

from controllers.index import *
from controllers.beercontroller import *
from controllers.locationcontroller import *


def define_routers():
    api.add_resource(Index, '/')
    # GET all beers
    api.add_resource(BeersController, '/example/rest/v1/beers')
    # GET, PUT and DELETE one beer by id
    api.add_resource(BeerControllerById, '/example/rest/v1/beer/<int:id>')
    # POST beer (Create beer or new beer)
    api.add_resource(BeerController, '/example/rest/v1/beer')

    # GET one location by id
    api.add_resource(LocationControllerById, '/example/rest/v1/location/<int:id>')

    @app.errorhandler(404)
    def invalid_route(e):
        """
            Define custom 404 in json when not exist route
        """
        app.logger.error('Route not found')
        return jsonify({
            'message': 'Route not found ' + str(e)
        }), 404
