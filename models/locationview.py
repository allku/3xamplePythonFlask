# -*- coding: utf-8 -*-
from app import db
from sqlalchemy import ForeignKey


class LocationView(db.Model):
    __tablename__ = 'v_locations'
    __table_args__ = {'info': dict(is_view=True)}


    id = db.Column(db.Integer, db.Identity(start=1), primary_key=True)
    name = db.Column(db.String)
    location = db.Column(db.String)
    level = db.Column(db.Integer)
    observation = db.Column(db.String)
    status = db.Column(db.String)
    location_id = db.Column(db.Integer)

    def __repr__(self):
        return '<id {}>'.format(self.id)

    def serialize(self):
        locations = {
                'id': self.id,
                'name': self.name,
                'location': self.location,
                'level': self.level,
                'observation': self.observation,
                'status': self.status,
                'location_parent': self.location_id
                }
        return locations
