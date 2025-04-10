
from dao.loan_repository_impl import LoanRepositoryImpl
from dao.customer_repositoty_impl import CustomerRepositoryImpl

def main():
    loan_repo = LoanRepositoryImpl()
    customer_repo = CustomerRepositoryImpl()

    while True:
        print("\n========== Loan Management System ==========")
        print("1. Apply for Loan")
        print("2. Calculate Interest")
        print("3. Know Interest by ur Loan_ID")
        print("4. Check Loan Status Based on Credit Score")
        print("5. Calculate EMI by Loan ID")
        print("6. Calculate your EMI Just by Entering (P, R, N)")
        print("7. Make Loan Repayment by Amount")
        print("8. View All Loans")
        print("9. Get Loan Details by ID")
        print("10.Add new Customer")

        print("0. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            loan_repo.apply_loan()
        elif choice == '2':
            loan_repo.calculate_interest()
        elif choice == '3':
            loan_repo.calculate_interest_by_id()
        elif choice == '4':
            loan_repo.loan_status()
        elif choice == '5':
            loan_repo.calculate_emi_by_id()
        elif choice == '6':
            loan_repo.calculate_emi()
        elif choice == '7':
            loan_repo.loan_repayment()
        elif choice == '8':
            loan_repo.get_all_loans()
        elif choice == '9':
            loan_repo.get_loan_by_id()
        elif choice == '10':
            customer_repo.add_customer()
        elif choice == '0':
            print("Exiting Loan Management System.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
