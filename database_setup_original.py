
###   Database Definiation ####
import os
import sys
from flask import Flask

from flask_sqlalchemy import SQLAlchemy

from sqlalchemy import(Column,ForeignKey,Integer,String)

from sqlalchemy.ext.declarative import(declarative_base)

from sqlalchemy.orm import relationship

from sqlalchemy import create_engine

Base = declarative_base()

##app = Flask(_name_)
##app.config['SQLALCHEMY_DATABASE_URL'] = 'sqlite:///restaurantmenu.db'
##db = SQLAlchemy(app)

###   Class Definition ####

class Restaurant(Base):
    ###   table Definition ####
    _tablename_ = 'restaurant'

    ###   Column Definition ####
    name = column(String(80),nullable=False)
    id = column(Integer,primary_key = True)
    

class MenuItem(Base):
    ###   table Definition ####
    tablename_ = 'menu_item'

    ###   Column Definition ####
    name = column(String(80),nullable = False)
    id = column(Integer,primary_key= True)
    course = column(String(250))
    description =  column(string(250))
    price = column(String(8))

    restaurant_id = column(Integer,ForeignKey(restaurant.id))

    ###   relationship Definition ####
    restaurant = relationship(Restaurant)
   
## Create a database ##

## db.create_all()

engine = create_engine('sqlite:///restaurant.db')
Base.metadata.create_all(engine)

print "done"
