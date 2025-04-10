

class Loan:
    def __init__(self, loan_id=None, customer_id=None, principal_amount=None,
                 interest_rate=None, loan_term=None, loan_type=None, loan_status=None):
        self.__loan_id = loan_id
        self.__customer_id = customer_id
        self.__principal_amount = principal_amount
        self.__interest_rate = interest_rate
        self.__loan_term = loan_term
        self.__loan_type = loan_type
        self.__loan_status = loan_status

    def get_loan_id(self):
        return self.__loan_id
    def set_loan_id(self, loan_id):
        self.__loan_id = loan_id

    def get_customer_id(self):
        return self.__customer_id
    def set_customer_id(self, customer_id):
        self.__customer_id = customer_id

    def get_principal_amount(self):
        return self.__principal_amount
    def set_principal_amount(self, amount):
        self.__principal_amount = amount

    def get_interest_rate(self):
        return self.__interest_rate
    def set_interest_rate(self, rate):
        self.__interest_rate = rate

    def get_loan_term(self):
        return self.__loan_term
    def set_loan_term(self, term):
        self.__loan_term = term

    def get_loan_type(self):
        return self.__loan_type
    def set_loan_type(self, loan_type):
        self.__loan_type = loan_type

    def get_loan_status(self):
        return self.__loan_status
    def set_loan_status(self, status):
        self.__loan_status = status

    def __str__(self):
        return (f"Loan[ID={self.__loan_id}, CustomerID={self.__customer_id}, Principal={self.__principal_amount}, "
                f"Interest={self.__interest_rate}, Term={self.__loan_term}, Type={self.__loan_type}, Status={self.__loan_status}]")
