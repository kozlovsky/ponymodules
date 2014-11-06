# This is the base module which define db object and some core entities

import datetime
from pony.orm import *

db = Database()  # This database object is used with all entities

# It is also possible to define some common entities here:

class Person(db.Entity):
    name = Required(str)
    dob = Required(datetime.date)

class User(Person):
    login = Required(str, unique=True)
    password = Required(str)
    email = Required(str)

    # the following entities are defined in another module forum_entities.py
    topics = Set("Topic")
    comments = Set("Comment")
