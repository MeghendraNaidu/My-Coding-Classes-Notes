class User:
    def __init__(self, user_id, name, email, password_hash, role):
        self.user_id = user_id
        self.name = name
        self.email = email
        self.password_hash = password_hash
        self.role = role
