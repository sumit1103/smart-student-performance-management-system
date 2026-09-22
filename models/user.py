class User:
    """Represent common information shared by students and teachers."""

    def __init__(self, user_id, name, email):
        self.user_id = user_id
        self.name = name
        self.email = email