#Task 1
name = input("Enter your name: ")
age = int(input("Enter your age: "))
program = input("Enter your program of study: ")
marks = float(input("Enter your marks: "))

student_info = (name, age, program, marks)

print("\nStored Student Information:")
print(student_info)

#Task 2
sentence = input("Enter a sentence: ")


num_characters = len(sentence)


words = sentence.split()
num_words = len(words)


num_spaces = sentence.count(' ')


num_vowels = 0
num_digits = 0
vowels = "aeiouAEIOU"


for char in sentence:
    if char in vowels:
        num_vowels += 1
    elif char.isdigit():
        num_digits += 1


print(f"\n--- Sentence Analysis ---")
print(f"Number of characters: {num_characters}")
print(f"Number of words:      {num_words}")
print(f"Number of vowels:     {num_vowels}")
print(f"Number of spaces:     {num_spaces}")
print(f"Number of digits:     {num_digits}")

#Task 3


employee_list = []

for i in range(1, 4):
    print(f"--- Enter details for Employee {i} ---")
    name = input("Enter Name: ")
    age = int(input("Enter Age: "))
    salary = float(input("Enter Salary: "))
    print()  
    
    
    employee_tuple = (name, age, salary)
    
    
    employee_list.append(employee_tuple)


print("--- Stored Employee List ---")
print(employee_list)

#Task 4

numbers = (10, 15, 20, 25, 30, 35, 40)


even_count = 0
odd_count = 0


for num in numbers:
    if num % 2 == 0:
        even_count += 1
    else:
        odd_count += 1


print(f"Number of even numbers: {even_count}")
print(f"Number of odd numbers:  {odd_count}")









