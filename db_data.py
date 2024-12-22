from dotenv import dotenv_values

NEO_URL = "neo4j+s://"

class DatabaseData:
    def __init__(self):
        self.db_values = dotenv_values(".env")

    def get_password(self, password_ref = "DATABASE_PASSWORD"):
        return self.db_values[password_ref]

    def get_connection(self, link_ref = "DATABASE_LINK"):
        return NEO_URL + self.db_values[link_ref]