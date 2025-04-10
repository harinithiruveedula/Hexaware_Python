from dao.payment_dao import PaymentDAO
from util.DBConnection import DBConnection
class PaymentDAOImpl(PaymentDAO):
    def get_student(self):
        try:
            payment_id = int(input("Enter Payment ID to fetch student info: "))
            conn = DBConnection.get_connection()
            cursor = conn.cursor()

            query = """
            SELECT s.student_id, s.first_name, s.last_name, s.email, s.phone_number
            FROM info.payments p
            JOIN info.students s ON p.student_id = s.student_id
            WHERE p.payment_id = ?
            """
            cursor.execute(query, (payment_id,))
            result = cursor.fetchone()

            if result:
                print(f"Student ID: {result.student_id}")
                print(f"Name: {result.first_name} {result.last_name}")
                print(f"Email: {result.email}")
                print(f"Phone: {result.phone_number}")
            else:
                print("No student found for the given Payment ID.")
            conn.close()
        except Exception as e:
            print("Error retrieving student:", e)

    def get_payment_amount(self):
        try:
            payment_id = int(input("Enter Payment ID to fetch payment amount: "))
            conn = DBConnection.get_connection()
            cursor = conn.cursor()

            query = "SELECT amount FROM info.payments WHERE payment_id = ?"
            cursor.execute(query, (payment_id,))
            result = cursor.fetchone()

            if result:
                print(f"Payment Amount: {result.amount}")
            else:
                print("No payment found with that ID.")
            conn.close()
        except Exception as e:
            print("Error retrieving payment amount:", e)

    def get_payment_date(self):
        try:
            payment_id = int(input("Enter Payment ID to fetch payment date: "))
            conn = DBConnection.get_connection()
            cursor = conn.cursor()

            query = "SELECT payment_date FROM info.payments WHERE payment_id = ?"
            cursor.execute(query, (payment_id,))
            result = cursor.fetchone()

            if result:
                print(f"Payment Date: {result.payment_date}")
            else:
                print("No payment found with that ID.")
            conn.close()
        except Exception as e:
            print("Error retrieving payment date:", e)

    def add_payment(self):
        try:
            student_id = int(input("Enter student ID: "))
            amount = float(input("Enter payment amount: "))
            payment_date = input("Enter payment date (YYYY-MM-DD): ")
            conn = DBConnection.get_connection()
            cursor = conn.cursor()

            # Validate student
            cursor.execute("SELECT COUNT(*) FROM info.students WHERE student_id = ?", (student_id,))
            if cursor.fetchone()[0] == 0:
                print("Student not found.")
                return

            # Insert payment
            cursor.execute("""
                INSERT INTO info.payments (student_id, amount, payment_date)
                VALUES (?, ?, ?)
            """, (student_id, amount, payment_date))

            conn.commit()
            print("Payment added successfully.")

        except Exception as e:
            print(f"Error while adding payment: {e}")
