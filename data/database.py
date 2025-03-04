import bcrypt
import sqlite3 as sql
import data.queries as queries
from models import User

# specify the name of the database
databaseName = "data/data.db"
database = sql.connect(databaseName, check_same_thread=False)


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
    database.execute(queries.INSERT_USER(), (email, username, hashStr))
    database.commit()
    id = cursor.lastrowid
    cursor.close()
    return User(id, email, username, hash)


def get_user_by_email(email: str):
    cursor = database.cursor()
    cursor.execute(queries.SELECT_USER_BY("email"), [email])
    user = cursor.fetchone()
    cursor.close()
    if user is None:
        return None
    return User(*user)

def get_user_by_username(username: str):
    cursor = database.cursor()
    cursor.execute(queries.SELECT_USER_BY("username"), [username])
    user = cursor.fetchone()
    cursor.close()
    if user is None:
        return None
    return User(*user)