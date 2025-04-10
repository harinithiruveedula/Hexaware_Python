
import math
from dao.ILoanRepository import ILoanRepository
from util.DBConnection import DBConnection
from entity.loan import Loan
from exceptions.custom_exceptions import InvalidLoanException

class LoanRepositoryImpl(ILoanRepository):

    def apply_loan(self) -> bool:
        try:
            print("\n------ Apply for Loan ------")
            loan_id=int(input("Enter loan id: "))
            customer_id = int(input("Enter Customer ID: "))
            principal_amount = float(input("Enter Principal Amount: "))
            interest_rate = float(input("Enter Interest Rate (%): "))
            loan_term = int(input("Enter Loan Term (in months): "))
            loan_type = input("Enter Loan Type (HomeLoan/CarLoan): ")

            confirmation = input("Do you want to submit the loan application? (Yes/No): ").strip().lower()
            if confirmation != "yes":
                print("Loan application cancelled.")
                return False

            loan = Loan(
                loan_id=loan_id,
                customer_id=customer_id,
                principal_amount=principal_amount,
                interest_rate=interest_rate,
                loan_term=loan_term,
                loan_type=loan_type,
                loan_status="Pending"
            )

            conn = DBConnection.get_connection()
            cursor = conn.cursor()

            insert_query = """
                INSERT INTO loan.Loan (loan_id,customer_id, principal_amount, interest_rate, loan_term, loan_type, loan_status)
                VALUES (?,?, ?, ?, ?, ?,?)
            """
            cursor.execute(insert_query, (
                loan.get_loan_id(),
                loan.get_customer_id(),
                loan.get_principal_amount(),
                loan.get_interest_rate(),
                loan.get_loan_term(),
                loan.get_loan_type(),
                loan.get_loan_status()
            ))

            conn.commit()
            print("Loan application submitted successfully (Status: Pending).")
            return True

        except Exception as e:
            print("Error during loan application:", e)
            return False

    def calculate_interest_by_id(self) -> float:
        try:
            loan_id = int(input("Enter Loan ID to calculate interest: "))

            conn = DBConnection.get_connection()
            cursor = conn.cursor()

            cursor.execute("SELECT principal_amount, interest_rate, loan_term FROM loan.Loan WHERE loan_id = ?",
                           (loan_id,))
            result = cursor.fetchone()

            if not result:
                raise InvalidLoanException()

            principal, rate, term = result
            interest = (principal * (rate / 100) * term) / 12

            print(f"Interest for Loan ID {loan_id} = {interest:.2f}")
            return interest

        except InvalidLoanException as e:
            print("", e)
        except Exception as e:
            print("Error calculating interest by ID:", e)


    def calculate_interest(self) -> float:
        try:
            print("\n-- Calculate Interest Manually --")
            principal = float(input("Enter Principal Amount: "))
            rate = float(input("Enter Interest Rate (%): "))
            term = int(input("Enter Loan Term (in months): "))

            interest = (principal * (rate / 100) * term) / 12
            print("hey here is ur Intrest")
            print(f"Calculated Interest = {interest}")
            return interest

        except Exception as e:
            print("Error calculating manual interest:", e)
            return 0.0

    def loan_status(self):
        try:
            loan_id = int(input("Enter Loan ID to check status: "))

            conn = DBConnection.get_connection()
            cursor = conn.cursor()

            # Step 1: Get customer_id from Loan table
            cursor.execute("SELECT customer_id FROM loan.Loan WHERE loan_id = ?", (loan_id,))
            result = cursor.fetchone()

            if not result:
                print("Loan not found.")
                return

            customer_id = result[0]

            # Step 2: Get credit score from Customer table
            cursor.execute("SELECT credit_score FROM loan.Customer WHERE customer_id = ?", (customer_id,))
            credit_result = cursor.fetchone()

            if not credit_result:
                print("Customer not found.")
                return

            credit_score = credit_result[0]
            status = "Approved" if credit_score >= 650 else "Rejected"

            # Step 3: Update loan_status in Loan table
            cursor.execute("UPDATE loan.Loan SET loan_status = ? WHERE loan_id = ?", (status, loan_id))
            conn.commit()

            print(f"Loan ID {loan_id} is {status} based on credit score ({credit_score}).")

        except Exception as e:
            print("Error processing loan status:", e)

    def calculate_emi_by_id(self) -> float:
        try:
            loan_id = int(input("Enter Loan ID to calculate EMI: "))

            conn = DBConnection.get_connection()
            cursor = conn.cursor()

            cursor.execute("SELECT principal_amount, interest_rate, loan_term FROM loan.Loan WHERE loan_id = ?",
                           (loan_id,))
            result = cursor.fetchone()

            if not result:
                raise InvalidLoanException()

            principal, annual_rate, term = result
            monthly_rate = annual_rate / (12 * 100)  # Convert annual rate to monthly decimal

            emi = self.__calculate_emi_value(principal, monthly_rate, term)
            print(f"EMI for Loan ID {loan_id} is {emi:.2f}")
            return emi

        except InvalidLoanException as e:
            print("", e)
        except Exception as e:
            print("Error calculating EMI:", e)

    def calculate_emi(self) -> float:
        try:
            print("\n-- Calculate EMI Manually --")
            principal = float(input("Enter Principal Amount: "))
            annual_rate = float(input("Enter Annual Interest Rate (%): "))
            term = int(input("Enter Loan Term (months): "))

            monthly_rate = annual_rate / (12 * 100)

            emi = self.__calculate_emi_value(principal, monthly_rate, term)
            print(f"EMI = ₹{emi:.2f}")
            return emi

        except Exception as e:
            print("Error calculating EMI manually:", e)
            return 0.0

    def loan_repayment(self) -> None:
        try:
            loan_id = int(input("Enter Loan ID for repayment: "))
            amount_paid = float(input("Enter repayment amount: ₹"))

            conn = DBConnection.get_connection()
            cursor = conn.cursor()

            # Fetch loan details
            cursor.execute("SELECT principal_amount, interest_rate, loan_term FROM loan.Loan WHERE loan_id = ?",
                           (loan_id,))
            result = cursor.fetchone()

            if not result:
                print("Loan not found.")
                return

            principal, annual_rate, term = result
            monthly_rate = annual_rate / (12 * 100)

            # Calculate EMI
            emi = self.__calculate_emi_value(principal, monthly_rate, term)

            if amount_paid < emi:
                print(f"Amount ₹{amount_paid:.2f} is less than a single EMI of {emi:.2f}. Payment rejected.")
                return

            no_of_emis_paid = int(amount_paid // emi)
            total_paid = no_of_emis_paid * emi

            print(
                f"You can pay {no_of_emis_paid} EMIs of ₹{emi:.2f} with ₹{amount_paid:.2f} (Total Paid: ₹{total_paid:.2f})")

        except Exception as e:
            print("Error during repayment:", e)

    def get_all_loans(self) -> None:
        try:
            conn = DBConnection.get_connection()
            cursor = conn.cursor()

            query = """
            SELECT loan_id, customer_id, principal_amount, interest_rate, loan_term, loan_type, loan_status
            FROM loan.Loan
            """
            cursor.execute(query)
            loans = cursor.fetchall()

            if not loans:
                print("No loans found.")
                return

            print("\nAll Loans:")
            for loan in loans:
                print("----------------------------------")
                print(f"Loan ID      : {loan[0]}")
                print(f"Customer ID  : {loan[1]}")
                print(f"Principal    : {loan[2]:,.2f}")
                print(f"Interest Rate: {loan[3]}%")
                print(f"Loan Term    : {loan[4]} months")
                print(f"Loan Type    : {loan[5]}")
                print(f"Status       : {loan[6]}")

        except Exception as e:
            print("Error fetching loans:", e)



    def get_loan_by_id(self) -> None:
        try:
            loan_id = int(input("Enter Loan ID to fetch details: "))

            conn = DBConnection.get_connection()
            cursor = conn.cursor()

            cursor.execute("""
                SELECT loan_id, customer_id, principal_amount, interest_rate, 
                       loan_term, loan_type, loan_status
                FROM loan.Loan WHERE loan_id = ?
            """, (loan_id,))
            loan = cursor.fetchone()

            if not loan:
                raise InvalidLoanException()

            print(r"\Here are your Loan Details")
            print("----------------------------------")
            print(f"Loan ID      : {loan[0]}")
            print(f"Customer ID  : {loan[1]}")
            print(f"Principal    : {loan[2]:,.2f}")
            print(f"Interest Rate: {loan[3]}%")
            print(f"Loan Term    : {loan[4]} months")
            print(f"Loan Type    : {loan[5]}")
            print(f"Status       : {loan[6]}")

        except InvalidLoanException as e:
            print("", e)

        except Exception as e:
            print("Error fetching loan:", e)


    def __calculate_emi_value(self, P, R, N):
        try:
            emi = (P * R * math.pow(1 + R, N)) / (math.pow(1 + R, N) - 1)
            return emi
        except ZeroDivisionError:
            return 0.0