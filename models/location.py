# -*- coding: utf-8 -*-
from app import db
from sqlalchemy import ForeignKey


class Location(db.Model):
    __tablename__ = 'locations'


    id = db.Column(db.Integer, db.Identity(start=1), primary_key=True)
    name = db.Column(db.String, nullable=False)
    observation = db.Column(db.String)
    status = db.Column(db.String, nullable=False)
    location_id = db.Column(db.Integer, ForeignKey(
        'locations.id',
        ondelete='CASCADE')
        )

    parent = db.relationship(
            'Location',
            backref="location", 
            remote_side=id,
            cascade="all, delete"
            )
    
    beers = db.relationship('Beer',
                                  backref='location',
                                  lazy='dynamic')

    def __init__(self, name, observation, status, parent=None):
        self.name = name
        self.observation = observation
        self.status = status
        self.parent = parent

    def __repr__(self):
        return '<id {}>'.format(self.id)
