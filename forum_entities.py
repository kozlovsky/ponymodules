# This module contains entities for some specific application domain,
# namely - for the forum

from datetime import datetime
from pony.orm import *
from base_entities import db, User

class Forum(db.Entity):
    name = Required(str, unique=True)
    topics = Set("Topic")

class Topic(db.Entity):
    forum = Required(Forum)
    name = Required(str)
    text = Required(str)
    author = Required(User)  # or Required(db.User), or Required("User")
    created = Required(datetime, default=datetime.now)
    comments = Set("Comment")

class Comment(db.Entity):
    topic = Required(Topic)
    text = Required(str)
    author = Required(User)  # or Required(db.User), or Required("User")
    created = Required(datetime, default=datetime.now)
