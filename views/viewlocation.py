# -*- coding: utf-8 -*-
from app import db
from sqlalchemy import text

class ViewLocation:

    @staticmethod
    def create():
        """
            Create view location 
            Use the command in terminal:
            $ flask view
        """
        file = open('sql/v_locations.sql')
        ddl_view = text(file.read())
        print(ddl_view)

        db.session.execute('drop table v_locations')
        db.session.execute(ddl_view)
        db.session.commit()
        print('Create view v_locations')
