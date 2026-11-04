#Task 1
def factorial(n):
    result = 1

    for i in range(1, n + 1):
        result = result * i

    return result


num = int(input("Enter a number: "))
print("Factorial:", factorial(num))

#Task 2
def student_info(name, age, course):
    print("Student Name:", name)
    print("Student Age:", age)
    print("Student Course:", course)


student_info(name="Ali", age=20, course="Python")


#Task 3
def calculate_sum(*args):
    total = 0

    for num in args:
        total += num

    return total


print("Sum:", calculate_sum(10, 20, 30, 40, 50))


#Task 4
def employee_info(**kwargs):
    for key, value in kwargs.items():
        print(key, ":", value)


employee_info(
    name="Ahmed",
    age=25,
    department="IT",
    salary=50000
)
#Task 5
def check_password(password):

    if len(password) < 8:
        return "Password must contain at least 8 characters."

    if not any(char.isupper() for char in password):
        return "Password must contain an uppercase letter."

    if not any(char.islower() for char in password):
        return "Password must contain a lowercase letter."

    if not any(char.isdigit() for char in password):
        return "Password must contain a digit."

    if not any(not char.isalnum() for char in password):
        return "Password must contain a special character."

    return "Password is valid!"


password = input("Enter your password: ")
print(check_password(password))