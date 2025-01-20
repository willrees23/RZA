import sqlite3 as sql
import queries

# specify the name of the database
databaseName = "data/data.db"
database = None


def isSetup():
    return database != None


# sets up the database
# connects & creates tables if needed
def setup():
    if isSetup():
        return
    database = sql.connect(databaseName)
    database.execute(queries.CREATE_USERS_TABLE)
    database.execute(queries.CREATE_ZOO_BOOKINGS_TABLE)
    database.execute(queries.CREATE_HOTEL_RESERVATIONS_TABLE)


# TODO - testing, remove
setup()
