from dao.course_dao_impl import CourseDAOImpl
from entity.enrollment import Enrollment
from datetime import datetime
from dao.student_dao import StudentDAO

from util.DBConnection import DBConnection


class StudentDAOImpl(StudentDAO):
    def __init__(self):
        self.conn = DBConnection.get_connection()

    def enroll_in_course(self):
        try:
            # Show available courses first
            print("\n Available Courses:")
            course_dao = CourseDAOImpl()
            courses = course_dao.get_all_courses()

            if not courses:
                print("No courses available.")
                return

            for course in courses:
                print(f"Course ID: {course.get_course_id()}, Name: {course.get_course_name()}, Credits: {course.get_credits()}")

            # Now take user input
            student_id = int(input("Enter Student ID: "))
            course_id = int(input("Enter Course ID to enroll: "))
            enrollment_date = datetime.now()

            cursor = self.conn.cursor()
            insert_query = '''
                INSERT INTO info.enrollments (student_id, course_id, enrollment_date)
                VALUES (?, ?, ?)
            '''
            cursor.execute(insert_query, (student_id, course_id, enrollment_date))
            self.conn.commit()
            print("Student enrolled in course successfully!")

        except Exception as e:
            print(" Error during enrollment:", e)

    def update_student_info(self):
        try:
            student_id = int(input("Enter the Student ID to update: "))

            print("\nWhich field do you want to update?")
            print("1. First Name")
            print("2. Last Name")
            print("3. Date of Birth (YYYY-MM-DD)")
            print("4. Email")
            print("5. Phone Number")

            choice = input("Enter your choice (1-5): ")

            field_map = {
                '1': 'first_name',
                '2': 'last_name',
                '3': 'date_of_birth',
                '4': 'email',
                '5': 'phone_number'
            }

            if choice not in field_map:
                print("Invalid choice.")
                return False

            new_value = input(f"Enter new value for {field_map[choice]}: ")

            # If updating date_of_birth, convert to proper format
            if choice == '3':
                from datetime import datetime
                new_value = datetime.strptime(new_value, "%Y-%m-%d")

            update_query = f"UPDATE info.students SET {field_map[choice]} = ? WHERE student_id = ?"

            cursor = self.conn.cursor()
            cursor.execute(update_query, (new_value, student_id))
            self.conn.commit()

            if cursor.rowcount > 0:
                print(" Student information updated successfully!")
                return True
            else:
                print("No student found with the given ID.")
                return False

        except Exception as e:
            print(" Error updating student info:", e)
            return False

    def make_payment(self):
        try:
            student_id = int(input("Enter the Student ID making the payment: "))
            amount = float(input("Enter payment amount: "))
            payment_date_input = input("Enter payment date (YYYY-MM-DD): ")

            # Convert string to datetime
            payment_date = datetime.strptime(payment_date_input, "%Y-%m-%d")

            insert_query = """
                INSERT INTO info.payments (student_id, amount, payment_date)
                VALUES (?, ?, ?)
            """

            cursor = self.conn.cursor()
            cursor.execute(insert_query, (student_id, amount, payment_date))
            self.conn.commit()

            if cursor.rowcount > 0:
                print(" Payment recorded successfully.")
                return True
            else:
                print("Failed to record the payment.")
                return False

        except Exception as e:
            print("Error recording payment:", e)
            return False

    def display_student_info(self):
        try:
            student_id = int(input("Enter the Student ID to view details: "))

            cursor = self.conn.cursor()

            # Fetch student details
            query = """
                SELECT student_id, first_name, last_name, date_of_birth, email, phone_number
                FROM info.students
                WHERE student_id = ?
            """
            cursor.execute(query, (student_id,))
            row = cursor.fetchone()

            if row:
                print("\n Student Details")
                print("-" * 40)
                print(f"Student ID   : {row.student_id}")
                print(f"First Name   : {row.first_name}")
                print(f"Last Name    : {row.last_name}")
                print(f"Date of Birth: {row.date_of_birth}")
                print(f"Email        : {row.email}")
                print(f"Phone Number : {row.phone_number}")
                print("-" * 40)
                return True
            else:
                print("no student found with that ID.")
                return False

        except Exception as e:
            print("Error displaying student info:", e)
            return False

    def get_enrolled_courses(self):
        try:
            student_id = int(input("Enter the Student ID to see enrolled courses: "))

            cursor = self.conn.cursor()

            query = """
                SELECT c.course_id, c.course_name, c.credits,
                       t.first_name + ' ' + t.last_name AS instructor_name
                FROM info.enrollments e
                JOIN info.courses c ON e.course_id = c.course_id
                JOIN info.teachers t ON c.teacher_id = t.teacher_id
                WHERE e.student_id = ?
            """
            cursor.execute(query, (student_id,))
            rows = cursor.fetchall()

            if rows:
                print("\nEnrolled Courses with Instructor")
                print("-" * 50)
                for row in rows:
                    print(f"Course ID      : {row.course_id}")
                    print(f"Course Name    : {row.course_name}")
                    print(f"Credits        : {row.credits}")
                    print(f"Instructor     : {row.instructor_name}")
                    print("-" * 50)
                return True
            else:
                print("No courses enrolled by the student.")
                return False

        except Exception as e:
            print(" Error fetching enrolled courses:", e)
            return False

    def get_payment_history(self):
        try:
            student_id = int(input("Enter the Student ID to view payment history: "))
            cursor = self.conn.cursor()

            query = """
                SELECT payment_id, amount, payment_date
                FROM info.payments
                WHERE student_id = ?
                ORDER BY payment_date DESC
            """
            cursor.execute(query, (student_id,))
            rows = cursor.fetchall()

            if rows:
                print("\n Payment History")
                print("-" * 40)
                for row in rows:
                    print(f"Payment ID   : {row.payment_id}")
                    print(f"Amount       : {row.amount}")
                    print(f"Date         : {row.payment_date}")
                    print("-" * 40)
                return True
            else:
                print("No payment records found for this student.")
                return False

        except Exception as e:
            print("Error retrieving payment history:", e)
            return False

    def add_student(self):
        try:
            conn = DBConnection.get_connection()
            cursor = conn.cursor()

            print("\n Enter New Student Details:")
            first_name = input("First Name: ")
            last_name = input("Last Name: ")
            dob = input("Date of Birth (YYYY-MM-DD): ")
            email = input("Email: ")
            phone = input("Phone Number: ")

            insert_query = """
            INSERT INTO info.students (first_name, last_name, date_of_birth, email, phone_number)
            VALUES (?, ?, ?, ?, ?)
            """

            cursor.execute(insert_query, (first_name, last_name, dob, email, phone))
            conn.commit()
            print("Student added successfully!")

        except Exception as e:
            print(f"Error adding student: {e}")
