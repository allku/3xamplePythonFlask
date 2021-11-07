from models.beer import Beer
from models.ingredient import Ingredient
from datetime import date
from app import db


class BeerSeed:

    @staticmethod
    def create():
        """
            Create a new beer with ingredients
            Use the command in terminal:
            $ flask seed
        """
        now = date.today()
        beer1 = Beer(name='Pilsener',
                     brand='Cerveceria Nacional',
                     origin='Ecuador',
                     date_released=now)

        beer1.ingredients.append(Ingredient(name='Malta'))
        beer1.ingredients.append(Ingredient('Agua'))

        db.session.add(beer1)
        db.session.commit()
        print("Beers seeder end")
