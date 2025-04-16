

from entity.loan import Loan

class HomeLoan(Loan):
    def __init__(self, loan_id=None, customer_id=None, principal_amount=None, interest_rate=None,
                 loan_term=None, loan_type="HomeLoan", loan_status=None,
                 property_address=None, property_value=None):
        super().__init__(loan_id, customer_id, principal_amount, interest_rate, loan_term, loan_type, loan_status)
        self.__property_address = property_address
        self.__property_value = property_value

    def get_property_address(self):
        return self.__property_address
    def set_property_address(self, address):
        self.__property_address = address

    def get_property_value(self):
         return  self.__property_value
    def set_property_value(self, value):
        self.__property_value = value

    def __str__(self):
        base = super().__str__()
        return f"{base}, PropertyAddress={self.__property_address}, PropertyValue={self.__property_value}"
