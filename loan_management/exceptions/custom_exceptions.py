

class InvalidLoanException(Exception):
    def __init__(self, message="Loan not found with the given ID."):
        super().__init__(message)
