# dao/sis_dao.py

from abc import ABC, abstractmethod
from entity.student import Student
from entity.course import Course
from entity.teacher import Teacher
from datetime import datetime

class SISDAO(ABC):

    @abstractmethod
    def enroll_student_in_course(self, student: Student, course: Course) -> bool:
        pass

    @abstractmethod
    def assign_teacher_to_course(self, teacher: Teacher, course: Course) -> bool:
        pass

    @abstractmethod
    def record_payment(self, student: Student, amount: float, payment_date: datetime) -> bool:
        pass

    @abstractmethod
    def generate_enrollment_report(self, course: Course):
        pass

    @abstractmethod
    def generate_payment_report(self, student: Student):
        pass

    @abstractmethod
    def calculate_course_statistics(self, course: Course):
        pass
