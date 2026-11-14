#Task 1 

class Car:
    def __init__(self, brand, color):
        self.brand = brand
        self.color = color

    def start(self):
        print("The car is starting.")


car1 = Car("Toyota", "Red")
car1.start()


#Task 2

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def display_info(self):
        print("Title:", self.title)
        print("Author:", self.author)


book1 = Book("Python Basics", "John Smith")
book2 = Book("The Great Adventure", "Alice Brown")
book3 = Book("Learning OOP", "David Wilson")

book1.display_info()
print()

book2.display_info()
print()

book3.display_info()


# Task 3

class Calculator:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def addition(self):
        return self.num1 + self.num2

    def subtraction(self):
        return self.num1 - self.num2

    def multiplication(self):
        return self.num1 * self.num2

    def division(self):
        if self.num2 != 0:
            return self.num1 / self.num2
        else:
            return "Cannot divide by zero"


calculator = Calculator(20, 5)

print("Addition:", calculator.addition())
print("Subtraction:", calculator.subtraction())
print("Multiplication:", calculator.multiplication())
print("Division:", calculator.division())


#Task 4

class BankAccount:
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(amount, "deposited successfully.")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(amount, "withdrawn successfully.")
        else:
            print("Insufficient balance.")

    def display_balance(self):
        print("Account Holder:", self.account_holder)
        print("Current Balance:", self.balance)


account1 = BankAccount("Ali", 1000)

account1.deposit(500)
account1.withdraw(300)
account1.display_balance()