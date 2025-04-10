from abc import ABC, abstractmethod

from dao.ILoanRepository import ILoanRepository


class ICustomerRepository(ILoanRepository, ABC):
    @abstractmethod
    def add_customer(self):
        pass
