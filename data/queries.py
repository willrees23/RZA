# File which stores all of the query strings that will be used in the database.py file
# Stored separately to keep clutter out of the main database file

# Create users table query.
CREATE_USERS_TABLE = """
CREATE TABLE IF NOT EXISTS "users" (
	"id"	INTEGER NOT NULL UNIQUE,
	"email"	TEXT NOT NULL UNIQUE,
	"username"	TEXT NOT NULL UNIQUE,
	"password"	TEXT NOT NULL,
	PRIMARY KEY("id" AUTOINCREMENT)
);
"""

CREATE_ZOO_BOOKINGS_TABLE = """
CREATE TABLE IF NOT EXISTS "zoo_bookings" (
	"id"	INTEGER NOT NULL UNIQUE,
	"secret"	TEXT NOT NULL,
	"userId"	INTEGER NOT NULL,
	"dateTime"	NUMERIC NOT NULL,
	"adults"	INTEGER NOT NULL,
	"children"	INTEGER NOT NULL,
	"used"	INTEGER NOT NULL,
	PRIMARY KEY("id" AUTOINCREMENT)
);
"""

CREATE_HOTEL_RESERVATIONS_TABLE = """
CREATE TABLE IF NOT EXISTS "hotel_reservations" (
	"id"	INTEGER NOT NULL UNIQUE,
	"room"	INTEGER NOT NULL,
	"userId"	INTEGER NOT NULL,
	"startDateTime"	NUMERIC NOT NULL,
	"endDateTime"	NUMERIC NOT NULL,
	"adults"	INTEGER NOT NULL,
	"children"	INTEGER NOT NULL,
	PRIMARY KEY("id" AUTOINCREMENT)
);
"""


def INSERT(table: str, *args: str):
    # check if amount of arguments are even
    # if not, this function won't work, so error
    if len(args) % 2 != 0:
        print("Args not even")
        return
    # split the args into two halves
    length = len(args)
    firstH = args[0 : length // 2]
    secondH = args[length // 2 :]
    query = "INSERT INTO {} {} VALUES {}".format(table, firstH, secondH)
    print(query)
    return query


def INSERT_USER(email: str, username: str, password: str):
    return INSERT("users", "email", "username", "password", email, username, password)


def SELECT_USER_BY(by: str, s: str):
    query = "SELECT * FROM users WHERE {}='{}';".format(by, s)
    print(query)
    pass
