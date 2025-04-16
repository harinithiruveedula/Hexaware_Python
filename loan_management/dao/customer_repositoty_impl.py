# dao/customer_repository_impl.py

from util.DBConnection import DBConnection

class CustomerRepositoryImpl:
    def add_customer(self):
        try:
            print("\n------ Add New Customer ------")

            name = input("Enter Name: ")
            email = input("Enter Email Address: ")
            phone_number = input("Enter Phone Number: ")
            address = input("Enter Address: ")
            credit_score = int(input("Enter Credit Score: "))

            conn = DBConnection.get_connection()
            cursor = conn.cursor()

            query = """
                INSERT INTO loan.Customer (name, email, phone_number, address, credit_score)
                VALUES (?, ?, ?, ?, ?)
            """
            cursor.execute(query, (name, email, phone_number, address, credit_score))
            conn.commit()
            print("Customer added successfully!")

        except Exception as e:
            print("Error adding customer:", e)
