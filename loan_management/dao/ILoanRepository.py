# dao/ILoanRepository.py

from abc import ABC, abstractmethod
from entity.loan import Loan

class ILoanRepository(ABC):

    @abstractmethod
    def apply_loan(self, loan: Loan) -> bool:
        pass

    @abstractmethod
    def loan_status(self) -> None:
        pass


    @abstractmethod
    def calculate_interest(self, principal: float, rate: float, term: int) -> float:
        pass




    @abstractmethod
    def get_all_loans(self) -> None:
        pass

    @abstractmethod
    def get_loan_by_id(self) -> None:
        pass
    @abstractmethod
    def calculate_emi_by_id(self) -> None:
        pass

    @abstractmethod
    def calculate_interest_by_id(self) -> float:
        pass

