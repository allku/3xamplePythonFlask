# -*- coding: utf-8 -*-
import logging
logger = logging.getLogger(__name__)
from flask_restful import Resource
from flask import jsonify, request
from app import db
from models.locationview import LocationView


class LocationControllerById(Resource):
    def get(self, id):
        """
            Get one location
            :param id: id of beer
            :return: json object
        """
        try:
            location = LocationView.query.filter_by(id=id).first()

            if location is None:
                return {'message': 'Location not found'}, 404
                return None, 404

            return jsonify(location.serialize())
        except Exception as e:
            logger.error(e)
            return {'message': str(e)}, 501
