#Task 1
my_list = [3, 1, 0, 9, 5, 2, 6, 4, 9, 8, 7]

smallest = my_list[0]

for number in my_list:
    if number < smallest:
        smallest = number
        
print("The smallest number is:", smallest)

#Task 2
my_list = [3, 1, 0, 9, 5, 2, 6, 4, 9, 8, 7]


total_sum = 0


for number in my_list:
    total_sum += number
average = total_sum / len(my_list)

print("The average is:", average)

#Task 3

students = ["Ali", "Ahmed", "Sara", "Ayesha", "Bilal"]

search_name = input("Enter a student name: ")

if search_name in students:
    print("Student Found")
else:
    print("Student Not Found")
    
#Task 4
shopping_list= []

print("Please enter 5 items for your shopping list:")

for i in range(5):
    item = input(f"Item {i+1}: ")
    shopping_list.append(item)

print("\nYour complete shopping list:")
print(shopping_list)
