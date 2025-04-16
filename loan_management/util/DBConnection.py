import pyodbc
from util.PropertyUtil import PropertyUtil

class DBConnection:
    connection = None

    @staticmethod
    def get_connection():
        if DBConnection.connection is None:
            try:
                conn_str = PropertyUtil.get_property_string()
                DBConnection.connection = pyodbc.connect(conn_str)
                print(" Database connection established!")
            except Exception as e:
                print("Database connection error:", e)
        return DBConnection.connection
