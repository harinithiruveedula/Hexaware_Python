class Teacher:
    def __init__(self, teacher_id=None, first_name=None, last_name=None, email=None):
        self.__teacher_id = teacher_id
        self.__first_name = first_name
        self.__last_name = last_name
        self.__email = email

    def get_teacher_id(self):
        return self.__teacher_id

    def set_teacher_id(self, teacher_id):
        self.__teacher_id = teacher_id

    def get_first_name(self):
        return self.__first_name

    def set_first_name(self, first_name):
        self.__first_name = first_name

    def get_last_name(self):
        return self.__last_name

    def set_last_name(self, last_name):
        self.__last_name = last_name

    def get_email(self):
        return self.__email

    def set_email(self, email):
        self.__email = email
