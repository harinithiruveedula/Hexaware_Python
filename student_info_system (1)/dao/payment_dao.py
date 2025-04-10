from abc import ABC, abstractmethod

class PaymentDAO(ABC):
    @abstractmethod
    def get_student(self):
        pass

    @abstractmethod
    def get_payment_amount(self):
        pass

    @abstractmethod
    def get_payment_date(self):
        pass
    @abstractmethod
    def add_payment(self):
        pass
