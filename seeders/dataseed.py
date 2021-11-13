# -*- coding: utf-8 -*-
from models.beer import Beer
from models.ingredient import Ingredient
from models.location import Location
from datetime import date
from app import db


class DataSeed:

    @staticmethod
    def create():
        """
            Create a new beer with ingredients, and others datas
            Use the command in terminal:
            $ flask seed
        """
        planet = Location(name='Tierra',
                          observation=None,
                          status='Activo')

        continent1 = Location(name='America',
                              observation=None,
                              status='Activo',
                              parent=planet)

        country1 = Location(name='Ecuador',
                            observation=None,
                            status='Activo',
                            parent=continent1)

        continent2 = Location(name='Europa',
                              observation=None,
                              status='Activo',
                              parent=planet)

        country2 = Location(name='Alemania',
                            observation=None,
                            status='Activo',
                            parent=continent2)

        db.session.add(planet)
        db.session.commit()

        now = date.today()
        beer1 = Beer(name='Calenturienta',
                     brand='Cerveceria de Mi Hogar',
                     date_released=now,
                     location_id=country1.id)

        beer1.ingredients.append(Ingredient(name='Malta'))
        beer1.ingredients.append(Ingredient('Agua'))

        db.session.add(beer1)
        db.session.commit()
        print("Data seeder end")
