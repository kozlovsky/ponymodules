# This is the example of main program file which imports entities,
# connects to the database, drops/creates specified tables
# and populate some data to the database

from pony.orm import *  # or just import db_session, etc.
import all_entities  # This command make sure that all entities are imported
from base_entities import db  # Will bind this database

from db_settings import current_settings  # binding params

db.bind(*current_settings['args'], **current_settings['kwargs'])

from db_utils import connect
from db_loading import populate_database

if __name__ == '__main__':
    sql_debug(True)
    connect(db, drop_and_create='ALL') # drop_and_create=['Topic', 'Comment'])
    populate_database()
