# Task 1
total_marks = 0
num_subjects = 5

print(f"Please enter the marks for {num_subjects} subjects (out of 100 each):")


for i in range(1, num_subjects + 1):
    while True:
        try:
            
            mark = float(input(f"Enter marks for Subject {i}: "))
            
            
            if 0 <= mark <= 100:
                total_marks += mark
                break
            else:
                print("Invalid input. Marks should be between 0 and 100.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")


max_possible_marks = num_subjects * 100
percentage = (total_marks / max_possible_marks) * 100


if percentage >= 40:
    status = "Pass"
else:
    status = "Fail"


if percentage >= 90:
    grade = "A+"
elif percentage >= 80:
    grade = "A"
elif percentage >= 70:
    grade = "B"
elif percentage >= 60:
    grade = "C"
elif percentage >= 50:
    grade = "D"
elif percentage >= 40:
    grade = "E"
else:
    grade = "F"


print("\n--- Results Summary ---")
print(f"Total Marks: {total_marks} / {max_possible_marks}")
print(f"Percentage:  {percentage:.2f}%")
print(f"Grade:       {grade}")
print(f"Status:      {status}")



# Task 2

student_name = input("Enter the student's name: ")

print(f"Name in uppercase: {student_name.upper()}")
print(f"Name in lowercase: {student_name.lower()}")
print(f"Number of characters: {len(student_name)}")

if student_name:
    print(f"First character: {student_name[0]}")
    print(f"Last character: {student_name[-1]}")
else:
    print("The name entered is empty, so there are no first or last characters.")
    
# Task 3


numbers = []

print("Please enter 10 numbers:")
for i in range(10):
    while True:
        try:
            num = float(input(f"Enter number {i + 1}: "))
            numbers.append(num)
            break
        except ValueError:
            print("Invalid input. Please enter a valid number.")


total_sum = sum(numbers)
average = total_sum / len(numbers)
largest = max(numbers)
smallest = min(numbers)


even_count = sum(1 for num in numbers if num.is_integer() and num % 2 == 0)
odd_count = sum(1 for num in numbers if num.is_integer() and num % 2 != 0)


print("\n--- Results ---")
print(f"Sum: {total_sum}")
print(f"Average: {average}")
print(f"Largest number: {largest}")
print(f"Smallest number: {smallest}")
print(f"Number of even numbers: {even_count}")
print(f"Number of odd numbers: {odd_count}")

#Task 4 

balance = 50000

while True:
    
    print("\n========== ATM MENU ==========")
    print("1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")
    print("==============================")
    
    
    choice = input("Select an option (1-4): ").strip()
    
    if choice == "1":
        
        print(f"\nYour current balance is: ${balance:,.2f}")
        
    elif choice == "2":
        
        try:
            amount = float(input("\nEnter amount to deposit: $"))
            if amount > 0:
                balance += amount
                print(f"Successfully deposited ${amount:,.2f}.")
                print(f"New balance: ${balance:,.2f}")
            else:
                print("Error: Deposit amount must be greater than zero.")
        except ValueError:
            print("Error: Please enter a valid numerical amount.")
            
    elif choice == "3":
        
        try:
            amount = float(input("\nEnter amount to withdraw: $"))
            if amount <= 0:
                print("Error: Withdrawal amount must be greater than zero.")
            elif amount > balance:
                print(f"Error: Insufficient funds! Your balance is ${balance:,.2f}")
            else:
                balance -= amount
                print(f"Successfully withdrew ${amount:,.2f}.")
                print(f"Remaining balance: ${balance:,.2f}")
        except ValueError:
            print("Error: Please enter a valid numerical amount.")
            
    elif choice == "4":
        
        print("\nThank you for using the ATM. Goodbye!")
        break
        
    else:
        print("\nInvalid choice! Please select a valid option from 1 to 4.")


#Task 5

while True:
    try:
        n = int(input("Enter a positive integer n: "))
        if n > 0:
            break
        print("Please enter a number greater than 0.")
    except ValueError:
        print("Invalid input. Please enter a valid integer.")


for i in range(1, n + 1):
    print(f"\n--- Multiplication Table for {i} ---")
    
    
    for j in range(1, 11):
        print(f"{i} x {j} = {i * j}")
