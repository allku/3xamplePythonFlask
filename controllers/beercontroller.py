# -*- coding: utf-8 -*-
from flask_restful import Resource
from flask import jsonify, request
from app import db
from models.beer import Beer
from models.ingredient import Ingredient


class BeersController(Resource):
    def get(self):
        try:
            beers = Beer.query.all()
            print(beers)
            return jsonify([b.serialize() for b in beers])
        except Exception as e:
            return str(e), 501


class BeerController(Resource):
    def post(self):
        try:
            data = request.get_json()
            # Validate is missing
            name = data['name']
            brand = data['brand']
            origin = data['origin']
            date_released = data['dateReleased']

            beer = Beer(name, brand, origin, date_released)

            for i in data['ingredients']:
                beer.ingredients.append(Ingredient(i['name']))

            db.session.add(beer)
            db.session.commit()

            beer_one = Beer.query.filter_by(id=beer.id).first()

            return jsonify(beer_one.serialize())

            # return {
            #     'id': beer.id,
            #     'name': beer.name,
            #     'brand': beer.brand,
            #     'origin': beer.origin,
            #     'dateReleased': beer.date_released.strftime('%Y-%m-%d')
            # }

        except Exception as e:
            return str(e), 501


class BeerControllerById(Resource):
    def get(self, id):
        try:
            beer = Beer.query.filter_by(id=id).first()

            if beer is None:
                return None, 404

            return jsonify(beer.serialize())
        except Exception as e:
            return str(e), 501

    def put(self, id):
        try:
            beer = Beer.query.filter_by(id=id).first()

            if beer is None:
                return None, 404

            data = request.get_json()
            # Validate is missing
            name = data['name']
            brand = data['brand']
            origin = data['origin']
            date_released = data['dateReleased']

            beer.name = name
            beer.brand = brand
            beer.origin = origin
            beer.date_released = date_released

            db.session.commit()

            return jsonify(beer.serialize())
        except Exception as e:
            return str(e), 501

    def delete(self, id):
        try:
            beer = Beer.query.filter_by(id=id).first()

            if beer is None:
                return None, 404

            db.session.delete(beer)
            db.session.commit()

            return {
                'id': beer.id,
                'name': beer.name
            }
        except Exception as e:
            return str(e), 501
