class Enrollment:
    def __init__(self, enrollment_id=None, student_id=None, course_id=None, enrollment_date=None):
        self.__enrollment_id = enrollment_id
        self.__student_id = student_id
        self.__course_id = course_id
        self.__enrollment_date = enrollment_date

    def get_enrollment_id(self):
        return self.__enrollment_id

    def set_enrollment_id(self, enrollment_id):
        self.__enrollment_id = enrollment_id

    def get_student_id(self):
        return self.__student_id

    def set_student_id(self, student_id):
        self.__student_id = student_id

    def get_course_id(self):
        return self.__course_id

    def set_course_id(self, course_id):
        self.__course_id = course_id

    def get_enrollment_date(self):
        return self.__enrollment_date

    def set_enrollment_date(self, enrollment_date):
        self.__enrollment_date = enrollment_date
