# -*- coding: utf-8 -*-
from app import db


class Beer(db.Model):
    __tablename__ = 'beers'

    id = db.Column(db.Integer, db.Identity(start=1), primary_key=True)
    name = db.Column(db.String, nullable=False)
    brand = db.Column(db.String, nullable=False)
    origin = db.Column(db.String, nullable=False)
    date_released = db.Column(db.DateTime, nullable=False)
    ingredients = db.relationship('Ingredient',
                                  backref='beer',
                                  lazy='dynamic',
                                  cascade="all, delete")

    def __init__(self, name, brand, origin, date_released):
        self.name = name
        self.brand = brand
        self.origin = origin
        self.date_released = date_released

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

        beers_data = {
            'id': self.id,
            'name': self.name,
            'brand': self.brand,
            'origin': self.origin,
            'dateReleased': self.date_released.strftime('%Y-%m-%dT%H:%M:%S'),
            'ingredients': ingredients_data
        }
        return beers_data
