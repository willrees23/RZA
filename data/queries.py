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
