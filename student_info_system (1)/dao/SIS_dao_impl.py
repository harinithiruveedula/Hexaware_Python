# dao_impl/sis_dao_impl.py

import pyodbc
from dao.SIS_dao import SISDAO
from entity.student import Student
from entity.course import Course
from entity.teacher import Teacher
from util.DBConnection import DBConnection
from datetime import datetime

class SISDAOImpl(SISDAO):

    def __init__(self):
        self.conn = DBConnection.get_connection()
        self.cursor = self.conn.cursor()

    def enroll_student_in_course(self) -> bool:
        try:
            student_id = int(input("Enter Student ID to enroll: "))
            course_id = int(input("Enter Course ID: "))
            query = "INSERT INTO info.enrollments (student_id, course_id) VALUES (?, ?)"
            self.cursor.execute(query, (student_id, course_id))
            self.conn.commit()
            print("Student enrolled successfully!")
            return True
        except Exception as e:
            print("Error enrolling student:", e)
            return False

    def assign_teacher_to_course(self) -> bool:
        try:
            teacher_id = int(input("Enter Teacher ID to assign: "))
            course_id = int(input("Enter Course ID: "))
            query = "UPDATE info.courses SET teacher_id = ? WHERE course_id = ?"
            self.cursor.execute(query, (teacher_id, course_id))
            self.conn.commit()
            print("Teacher assigned successfully!")
            return True
        except Exception as e:
            print("Error assigning teacher:", e)
            return False

    def record_payment(self) -> bool:
        try:
            student_id = int(input("Enter Student ID: "))
            amount = float(input("Enter Payment Amount: "))
            payment_date = datetime.now()  # or ask for input
            query = "INSERT INTO info.payments (student_id, amount, payment_date) VALUES (?, ?, ?)"
            self.cursor.execute(query, (student_id, amount, payment_date))
            self.conn.commit()
            print("Payment recorded successfully!")
            return True
        except Exception as e:
            print("Error recording payment:", e)
            return False

    def generate_enrollment_report(self):
        try:
            course_id = int(input("Enter Course ID to generate enrollment report: "))
            query = """
                SELECT s.student_id, s.first_name, s.last_name
                FROM info.enrollments e
                JOIN info.students s ON e.student_id = s.student_id
                WHERE e.course_id = ?
            """
            self.cursor.execute(query, (course_id,))
            students = self.cursor.fetchall()
            print(f"\nEnrollment Report for Course ID {course_id}:")
            for s in students:
                print(f"Student ID: {s[0]}, Name: {s[1]} {s[2]}")
        except Exception as e:
            print("Error generating enrollment report:", e)

    def generate_payment_report(self):
        try:
            student_id = int(input("Enter Student ID to generate payment report: "))
            query = """
                SELECT payment_id, amount, payment_date
                FROM info.payments
                WHERE student_id = ?
            """
            self.cursor.execute(query, (student_id,))
            payments = self.cursor.fetchall()
            print(f"\nPayment Report for Student ID {student_id}:")
            for p in payments:
                print(f"Payment ID: {p[0]}, Amount: {p[1]}, Date: {p[2]}")
        except Exception as e:
            print("Error generating payment report:", e)

    def calculate_course_statistics(self):
        try:
            course_id = int(input("Enter Course ID to calculate statistics: "))
            query_enrollments = "SELECT COUNT(*) FROM info.enrollments WHERE course_id = ?"
            self.cursor.execute(query_enrollments, (course_id,))
            total_enrollments = self.cursor.fetchone()[0]

            query_payments = """
                SELECT SUM(amount) FROM info.payments p
                JOIN info.enrollments e ON p.student_id = e.student_id
                WHERE e.course_id = ?
            """
            self.cursor.execute(query_payments, (course_id,))
            total_payments = self.cursor.fetchone()[0] or 0

            print(f"\nStatistics for Course ID {course_id}:")
            print(f"Total Enrollments: {total_enrollments}")
            print(f"Total Payments Received: {total_payments}")
        except Exception as e:
            print("Error calculating course statistics:", e)
