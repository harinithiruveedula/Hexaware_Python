from util.DBConnection import DBConnection

conn = DBConnection.get_connection()
if conn:
    print("Connected successfully!")
else:
    print(" Connection failed.")
