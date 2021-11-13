# -*- coding: utf-8 -*-
from app import db
from sqlalchemy import ForeignKey
from models.locationview import LocationView


class Beer(db.Model):
    __tablename__ = 'beers'

    id = db.Column(db.Integer, db.Identity(start=1), primary_key=True)
    name = db.Column(db.String, nullable=False)
    brand = db.Column(db.String, nullable=False)
    date_released = db.Column(db.DateTime, nullable=False)

    location_id = db.Column(db.Integer,
            ForeignKey('locations.id'),
            nullable=False)

    ingredients = db.relationship('Ingredient',
                                  backref='beer',
                                  lazy='dynamic',
                                  cascade="all, delete")

    def __init__(self, name, brand, date_released, location_id):
        self.name = name
        self.brand = brand
        self.date_released = date_released
        self.location_id = location_id

    def __repr__(self):
        return '<id {}>'.format(self.id)

    def serialize(self):
        """
            Extract ingredients detail
        """
        ingredients_data = []
        for i in self.ingredients.all():
            i_data = {}
            i_data['id'] = i.id
            i_data['name'] = i.name
            ingredients_data.append(i_data)

        location_beer = LocationView.query.filter_by(id=self.location_id).first()
        beers_data = {
            'id': self.id,
            'name': self.name,
            'brand': self.brand,
            'origin': location_beer.name,
            'location': location_beer.location,
            'dateReleased': self.date_released.strftime('%Y-%m-%dT%H:%M:%S'),
            'ingredients': ingredients_data,
            'locationId': self.location_id
        }
        return beers_data
