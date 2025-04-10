class Course:
    def __init__(self, course_id=None, course_name=None, credits=None, teacher_id=None):
        self.__course_id = course_id
        self.__course_name = course_name
        self.__credits = credits
        self.__teacher_id = teacher_id

    def get_course_id(self):
        return self.__course_id

    def set_course_id(self, course_id):
        self.__course_id = course_id

    def get_course_name(self):
        return self.__course_name

    def set_course_name(self, course_name):
        self.__course_name = course_name

    def get_credits(self):
        return self.__credits

    def set_credits(self, credits):
        self.__credits = credits

    def get_teacher_id(self):
        return self.__teacher_id

    def set_teacher_id(self, teacher_id):
        self.__teacher_id = teacher_id
