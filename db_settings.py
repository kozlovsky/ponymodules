# Test database parameters
test = dict(
    args = ['sqlite', 'exampledb.sqlite'],
    kwargs = dict(create_db=True)
    )

# Development database parameters
development = dict(
    args = ['mysql'],
    kwargs = dict(
        user = 'db_user',
        passwd = '123',
        host = 'localhost',
        db = 'exampledb'
        )
    )

# Production database parameters
production = dict(
    args = ['postgres'],
    kwargs = dict(
        user = 'db_user',
        password='123',
        host='localhost',
        database='exampledb'
        )
    )

# We will use these settings
current_settings = test
