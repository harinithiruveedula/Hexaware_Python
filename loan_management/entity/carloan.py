from entity.loan import Loan
class CarLoan(Loan):
    def __init__(self, loan_id=None, customer_id=None, principal_amount=None, interest_rate=None,
                 loan_term=None, loan_type="CarLoan", loan_status=None,
                 car_model=None, car_value=None):
        super().__init__(loan_id, customer_id, principal_amount, interest_rate, loan_term, loan_type, loan_status)
        self.__car_model = car_model
        self.__car_value = car_value

    def get_car_model(self):
        return self.__car_model
    def set_car_model(self, model):
        self.__car_model = model

    def get_car_value(self):
        return self.__car_value
    def set_car_value(self, value):
        self.__car_value = value

    def __str__(self):
        base = super().__str__()
        return f"{base}, CarModel={self.__car_model}, CarValue={self.__car_value}"
