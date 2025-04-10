# entity/sis.py
from entity.student import Student
from entity.course import Course
from entity.teacher import Teacher
from datetime import datetime

class SIS:
    def __init__(self):
        pass  # You may keep configurations if needed later

    def enroll_student_in_course(self, student: Student, course: Course):
        pass

    def assign_teacher_to_course(self, teacher: Teacher, course: Course):
        pass

    def record_payment(self, student: Student, amount: float, payment_date: datetime):
        pass

    def generate_enrollment_report(self, course: Course):
        pass

    def generate_payment_report(self, student: Student):
        pass

    def calculate_course_statistics(self, course: Course):
        pass
