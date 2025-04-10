from abc import ABC, abstractmethod

class IEnrollmentDAO(ABC):

    @abstractmethod
    def get_student_by_enrollment(self) -> None:
        """Retrieves the student associated with a particular enrollment"""
        pass


    @abstractmethod
    def get_course_by_enrollment(self) -> None:
        pass
    @abstractmethod
    def get_all_enrollments(self):
        pass
    @abstractmethod
    def add_enrollment(self):
        pass
