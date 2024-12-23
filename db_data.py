from dotenv import dotenv_values

NEO_URL = "bolt://"

class DatabaseData:
    def __init__(self):
        self.db_values = dotenv_values(".env")

    def get_password(self, password_ref = "DATABASE_PASSWORD"):
        return self.db_values[password_ref]

    def get_connection(self, link_ref = "DATABASE_LINK"):
        return NEO_URL + self.db_values[link_ref]
    
    def get_user(self, name_ref = "DATABASE_USER"):
        return self.db_values[name_ref]