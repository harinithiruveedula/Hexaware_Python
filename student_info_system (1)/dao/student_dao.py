from abc import ABC, abstractmethod

class StudentDAO(ABC):

    @abstractmethod
    def enroll_in_course(self):
        pass

    @abstractmethod
    def update_student_info(self):
        pass

    @abstractmethod
    def make_payment(self):
        pass

    @abstractmethod
    def display_student_info(self):
        pass

    @abstractmethod
    def get_enrolled_courses(self):
        pass

    @abstractmethod
    def get_payment_history(self):
        pass

    def add_student(self):
        pass