#Task 1

fruits = {"apple", "banana", "mango", "orange", "grapes"}

print(fruits)

#Task 2

numbers = [2, 4, 2, 6, 4, 8, 8]

unique_numbers = set(numbers)

print(unique_numbers)

#Task3

numbers = {1, 2, 3, 4, 5}

numbers.add(10)
numbers.remove(3)

print(numbers)

#Task4

numbers = {10, 20, 30, 40, 50}

num = int(input("Enter a number: "))

if num in numbers:
    print("Number exists in the set")
else:
    print("Number does not exist in the set")
    
#Task 5

values = {1, 2, 2, 3, 3, 3, 4}

print(len(values)) 

#Task 6

A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

print("Union (A | B):", A | B)

print("Intersection (A & B):", A & B)

print("Difference (A - B):", A - B)
print("Difference (B - A):", B - A)

print("Symmetric Difference (A ^ B):", A ^ B)
              