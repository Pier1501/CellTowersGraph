from dotenv import dotenv_values

NEO_URL = "bolt://"

class DatabaseData:
    def __init__(self, user_ref = "DATABASE_USER", link_ref = "DATABASE_LINK", password_ref = "DATABASE_PASSWORD"):
        self.db_values = dotenv_values(".env")
        self.password = self.db_values[password_ref]
        self.user = self.db_values[user_ref]
        self.get_connection = NEO_URL + self.db_values[link_ref]