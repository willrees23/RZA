import bcrypt
import sqlite3 as sql
import data.queries as queries
from models import User

# specify the name of the database
databaseName = "data/data.db"
database = sql.connect(databaseName)


# sets up the database
# connects & creates tables if needed
def setup():
    database.execute(queries.CREATE_USERS_TABLE)
    database.execute(queries.CREATE_ZOO_BOOKINGS_TABLE)
    database.execute(queries.CREATE_HOTEL_RESERVATIONS_TABLE)


def create_user(email: str, username: str, password: str):
    cursor = database.cursor()
    bytes = password.encode("utf-8")
    hash = bcrypt.hashpw(bytes, bcrypt.gensalt())
    hashStr = hash.decode("utf-8")
    database.execute(queries.INSERT_USER(email, username, hashStr))
    database.commit()
    id = cursor.lastrowid
    cursor.close()
    return User(id, email, username, hash)
