# -*- coding: utf-8 -*-
import os
import sys
import logging

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_restful import Api
from flask.cli import AppGroup

app = Flask(__name__)
api = Api(app)
app.config.from_pyfile('config.cfg')
db = SQLAlchemy(app)

# Models
from models.beer import *
from models.ingredient import *
from models.location import *
from models.locationview import *

migrate = Migrate(app, db)

# Routes
from router import define_routers

define_routers()

# Seeders
from seeders.dataseed import DataSeed


@app.cli.command("seed")
def create_data():
    """
        Define seed command, run in terminal:
        $ flask seed
    """
    DataSeed.create()


from views.viewlocation import ViewLocation

view_cli = AppGroup('view')


@view_cli.command("create")
def create_view():
    """
        Create view:
        $ flask view create
    """
    ViewLocation.create()


@view_cli.command("drop")
def drop_view():
    """
        Drop view:
        $ flask view drop
    """
    ViewLocation.drop()


app.cli.add_command(view_cli)

# Logger
filename = os.path.join(os.path.dirname(os.path.realpath(__file__)),
                        'logs',
                        'server.log')
logging.basicConfig(level=logging.DEBUG,
                    format="[%(levelname)s] %(asctime)s %(message)s",
                    handlers=[
                        logging.FileHandler(filename),
                        logging.StreamHandler(sys.stdout)
                    ])
app.logger.info('Start Flask Server')
