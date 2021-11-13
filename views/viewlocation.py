# -*- coding: utf-8 -*-
from app import db
from sqlalchemy import text


class ViewLocation:

    @staticmethod
    def create():
        """
            Create view location 
            Use the command in terminal:
            $ flask view create
        """
        file = open('sql/v_locations.sql')
        ddl_view = text(file.read())
        print(ddl_view)

        db.session.execute('drop table if exists v_locations')
        db.session.execute(ddl_view)
        db.session.commit()
        print('Create view v_locations')

    @staticmethod
    def drop():
        """
            Drop view location 
            Use the command in terminal:
            $ flask view drop
        """
        db.session.execute('drop view if exists v_locations')
        db.session.commit()
        print('Drop view v_locations')

