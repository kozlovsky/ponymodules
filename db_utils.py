# This function will generate mapping for the specified database
# and drop/create tables for the entities with specified names

def connect(db, drop_and_create=None):
    if not drop_and_create:
        db.generate_mapping(create_tables=True)
    elif drop_and_create == 'ALL':
        db.generate_mapping(check_tables=False)
        db.drop_all_tables(with_all_data=True)
        db.create_tables()
    else:
        db.generate_mapping(check_tables=False)
        for entity_name in drop_and_create:
            entity = getattr(db, entity_name)
            entity.drop_table(with_all_data=True)
        db.create_tables()
