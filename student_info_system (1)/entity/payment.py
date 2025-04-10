class Payment:
    def __init__(self, payment_id=None, student_id=None, amount=None, payment_date=None):
        self.__payment_id = payment_id
        self.__student_id = student_id
        self.__amount = amount
        self.__payment_date = payment_date

    def get_payment_id(self):
        return self.__payment_id

    def set_payment_id(self, payment_id):
        self.__payment_id = payment_id

    def get_student_id(self):
        return self.__student_id

    def set_student_id(self, student_id):
        self.__student_id = student_id

    def get_amount(self):
        return self.__amount

    def set_amount(self, amount):
        self.__amount = amount

    def get_payment_date(self):
        return self.__payment_date

    def set_payment_date(self, payment_date):
        self.__payment_date = payment_date
