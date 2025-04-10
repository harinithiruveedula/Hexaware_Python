from abc import ABC, abstractmethod

class CourseDAO(ABC):

    @abstractmethod
    def get_all_courses(self):

        pass

    @abstractmethod
    def assign_teacher(self) -> bool:
        pass

    @abstractmethod
    def update_course_info(self) -> bool:

        pass

    @abstractmethod
    def display_course_info(self) -> bool:

        pass

    @abstractmethod
    def get_teacher(self) -> bool:
        
        pass
