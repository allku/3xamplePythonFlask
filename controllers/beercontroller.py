# -*- coding: utf-8 -*-
from flask_restful import Resource
from flask import jsonify, request
from app import db
from models.beer import Beer
from models.ingredient import Ingredient
from validators.beerschema import beer_schema


class BeersController(Resource):
    def get(self):
        """
            Get all beers
            :return: json array
        """
        try:
            beers = Beer.query.all()
            print(beers)
            return jsonify([b.serialize() for b in beers])
        except Exception as e:
            return str(e), 501


class BeerController(Resource):
    def post(self):
        """
            Save a new beer with ingredients detail from body parameters
            :return: json object
        """
        try:
            data = request.get_json()
            # Validate body parameters
            errors = beer_schema.validate(data)
            print(errors)
            if errors:
                return {
                           'message': str(errors)
                       }, 500

            name = data['name']
            brand = data['brand']
            date_released = data['dateReleased']
            location_id = data['locationId']

            beer = Beer(name, brand, date_released, location_id)
            # Extract ingredients detail from data
            for i in data['ingredients']:
                beer.ingredients.append(Ingredient(i['name']))

            db.session.add(beer)
            db.session.commit()

            beer_one = Beer.query.filter_by(id=beer.id).first()

            return jsonify(beer_one.serialize())

        except Exception as e:
            return str(e), 501


class BeerControllerById(Resource):
    def get(self, id):
        """
            Get one beer
            :param id: id of beer
            :return: json object
        """
        try:
            beer = Beer.query.filter_by(id=id).first()

            if beer is None:
                return None, 404

            return jsonify(beer.serialize())
        except Exception as e:
            return str(e), 501

    def put(self, id):
        """
            Update a beer without ingredients detail from body parameters
            :param id: id of beer
            :return: json object
        """
        try:
            beer = Beer.query.filter_by(id=id).first()

            if beer is None:
                return None, 404

            data = request.get_json()
            # Validate is missing
            name = data['name']
            brand = data['brand']
            date_released = data['dateReleased']
            location_id = data['locationId']

            beer.name = name
            beer.brand = brand
            beer.date_released = date_released
            beer.location_id = location_id

            db.session.commit()

            return jsonify(beer.serialize())
        except Exception as e:
            return str(e), 501

    def delete(self, id):
        """
            Delete a beer
            :param id: id of beer
            :return: json object
        """
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
