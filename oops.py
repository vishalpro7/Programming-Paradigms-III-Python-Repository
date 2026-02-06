# --------- BANK ACCOUNT CLASSES ---------

class BankAccount:
    def __init__(self, account_holder, initial_balance):
        # Public data member
        self.account_holder = account_holder
        
        # Private data member (Encapsulation)
        self.__balance = initial_balance

    # Method to deposit money
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"₹{amount} deposited successfully.")
            print(f"Updated Balance: ₹{self.__balance}")
        else:
            print("Deposit amount must be positive.")

    # Method to withdraw money
    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
            print(f"₹{amount} withdrawn successfully.")
            print(f"Remaining Balance: ₹{self.__balance}")
        else:
            print("Error: Insufficient balance.")

    # Getter method to access private balance
    def get_balance(self):
        return self.__balance


# --------- SUBCLASS: SAVINGS ACCOUNT ---------
class SavingsAccount(BankAccount):
    def __init__(self, account_holder, initial_balance, interest_rate):
        # Call base class constructor
        super().__init__(account_holder, initial_balance)
        self.interest_rate = interest_rate

    # Overriding withdraw method (Polymorphism)
    def withdraw(self, amount):
        if amount > 20000:
            print("Error: Maximum withdrawal limit is ₹20,000 per transaction.")
        else:
            super().withdraw(amount)

    # Method to add interest
    def add_interest(self):
        interest = self.get_balance() * (self.interest_rate / 100)
        self.deposit(interest)
        print(f"Interest of ₹{interest:.2f} added.")


# --------- DEMO ---------
if __name__ == "__main__":
    # Create a Savings Account
    sa = SavingsAccount("Alice", 50000, 5)  # 5% interest rate

    # Display initial balance
    print(f"Account Holder: {sa.account_holder}")
    print(f"Initial Balance: ₹{sa.get_balance()}\n")

    # Deposit money
    sa.deposit(10000)
    print()

    # Withdraw money within limit
    sa.withdraw(15000)
    print()

    # Withdraw money exceeding limit
    sa.withdraw(25000)
    print()

    # Add interest
    sa.add_interest()
    print()

    # Final balance
    print(f"Final Balance: ₹{sa.get_balance()}")






# ===============================
# Exercise 2: Employee Payroll System
# ===============================

# Base class
class Employee:
    def __init__(self, name, emp_id):
        # Protected data members
        self._name = name
        self._emp_id = emp_id

    # Method to calculate salary (to be overridden)
    def calculate_salary(self):
        print("Salary calculation not defined for base Employee class.")

    # Method to display employee details
    def display_details(self):
        print(f"Employee Name: {self._name}")
        print(f"Employee ID: {self._emp_id}")


# Full-time employee subclass
class FullTimeEmployee(Employee):
    def __init__(self, name, emp_id, monthly_salary):
        super().__init__(name, emp_id)
        self.monthly_salary = monthly_salary

    # Overriding calculate_salary
    def calculate_salary(self):
        return self.monthly_salary


# Part-time employee subclass
class PartTimeEmployee(Employee):
    def __init__(self, name, emp_id, hours_worked, rate_per_hour):
        super().__init__(name, emp_id)
        self.hours_worked = hours_worked
        self.rate_per_hour = rate_per_hour

    # Overriding calculate_salary
    def calculate_salary(self):
        return self.hours_worked * self.rate_per_hour


# ===============================
# Testing Exercise 2 (Polymorphism)
# ===============================
if __name__ == "__main__":
    employees = [
        FullTimeEmployee("Pitambar", 101, 50000),
        PartTimeEmployee("Manoj", 102, 120, 400)
    ]

    for emp in employees:
        print("\n------------------------")
        emp.display_details()
        print("Employee Type:", emp.__class__.__name__)
        print("Calculated Salary: ₹", emp.calculate_salary())
