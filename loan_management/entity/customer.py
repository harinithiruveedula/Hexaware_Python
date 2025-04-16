

class Customer:
    def __init__(self, customer_id=None, name=None, email=None, phone_number=None, address=None, credit_score=None):
        self.__customer_id = customer_id
        self.__name = name
        self.__email = email
        self.__phone_number = phone_number
        self.__address = address
        self.__credit_score = credit_score

    def get_customer_id(self):
        return self.__customer_id
    def set_customer_id(self, customer_id):
        self.__customer_id = customer_id

    def get_name(self):
        return self.__name
    def set_name(self, name):
        self.__name = name

    def get_email(self):
        return self.__email
    def set_email(self, email):
        self.__email = email

    def get_phone_number(self):
        return self.__phone_number
    def set_phone_number(self, phone_number):
        self.__phone_number = phone_number

    def get_address(self):
        return self.__address
    def set_address(self, address):
        self.__address = address

    def get_credit_score(self):
        return self.__credit_score
    def set_credit_score(self, credit_score):
        self.__credit_score = credit_score

    def __str__(self):
        return (f"Customer[ID={self.__customer_id}, Name={self.__name}, Email={self.__email}, "
                f"Phone={self.__phone_number}, Address={self.__address}, CreditScore={self.__credit_score}]")
