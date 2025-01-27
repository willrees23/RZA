class User:
    def __init__(self, id: str, email: str, username: str, password: str):
        self.id = id
        self.email = email
        self.username = username
        self.password = password


class ZooBooking:
    def __init__(self, id, secret, userId, dateTime, adults, children, used):
        self.id = id
        self.secret = secret
        self.userId = userId
        self.dateTime = dateTime
        self.adults = adults
        self.children = children
        self.used = used
