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
        country = Location(name='Ecuador',
                observation=None,
                status='Activo')

        province = Location(name='Imbabura',
                observation=None,
                status='Activo',
                parent=country)

        city = Location(name='Ibarra',
                observation=None,
                status='Activo',
                parent=province)


        db.session.add(country)

        now = date.today()
        beer1 = Beer(name='Pilsener',
                     brand='Cerveceria Nacional',
                     origin='Ecuador',
                     date_released=now)

        beer1.ingredients.append(Ingredient(name='Malta'))
        beer1.ingredients.append(Ingredient('Agua'))

        db.session.add(beer1)
        db.session.commit()
        print("Data seeder end")
