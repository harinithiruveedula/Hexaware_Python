from abc import ABC, abstractmethod

class ITeacherDAO(ABC):

    @abstractmethod
    def update_teacher_info(self) -> bool:
        pass

    @abstractmethod
    def display_teacher_info(self) -> None:
        pass

    @abstractmethod
    def get_assigned_courses(self) -> None:
        pass
    @abstractmethod
    def assign_course_to_teacher(self) ->None:
         pass
