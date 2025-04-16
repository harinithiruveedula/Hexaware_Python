

class InvalidLoanException(Exception):
    def __init__(self, message="Loan not found with the given ID."):
        super().__init__(message)

class InvalidCustomerException(Exception):
    def __init__(self, message="Customer not found or invalid."):
        super().__init__(message)
