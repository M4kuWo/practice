from abc import ABC, abstractmethod
import logging

# Configure logging
log_file = "bank_account.log"
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler(log_file),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

# Abstract Base Class
class Account(ABC):
    def __init__(self, account_holder, initial_balance=0):
        self.account_holder = account_holder
        self._balance = initial_balance  # Protected, accessible by subclasses
        logger.info(f"Account created for {self.account_holder} with initial balance: {self._balance}")

    @abstractmethod
    def deposit(self, amount):
        """Add money to the account."""
        pass

    @abstractmethod
    def withdraw(self, amount):
        """Remove money from the account."""
        pass

    @abstractmethod
    def get_balance(self):
        """Return the account balance."""
        pass

# Concrete Class
class BankAccount(Account):
    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            logger.info(f"{self.account_holder} deposited {amount}. New balance: {self._balance}")
        else:
            logger.error(f"{self.account_holder} attempted to deposit a negative amount: {amount}")

    def withdraw(self, amount):
        if 0 < amount <= self._balance:
            self._balance -= amount
            logger.info(f"{self.account_holder} withdrew {amount}. New balance: {self._balance}")
        else:
            logger.warning(f"{self.account_holder} attempted an invalid withdrawal of {amount}")

    def get_balance(self):
        logger.info(f"{self.account_holder}'s balance checked: {self._balance}")
        return self._balance

# Example Usage
if __name__ == "__main__":
    account = BankAccount("Jane Doe", 100)
    account.deposit(50)
    account.withdraw(30)
    print("Current Balance:", account.get_balance())
