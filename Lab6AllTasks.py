#Task 1
numbers = [2, 3, 2, 5, 3, 2, 5, 8]

result = {}

for num in numbers:
    if num in result:
        result[num] += 1
    else:
        result[num] = 1

print(result)

#Task 2

marks = {
    'Ali': 85,
    'Sara': 95,
    'Ahmed': 95,
    'Noor': 78
}

highest = max(marks.values())

for student, mark in marks.items():
    if mark == highest:
        print(student, mark)
        
#Task 3

data = {'a': 1, 'b': 2, 'c': 3}

reversed_data = {}

for key, value in data.items():
    reversed_data[value] = key

print(reversed_data)

#Task 4

words = ['apple', 'ant', 'banana', 'ball', 'cat']

result = {}

for word in words:
    first_letter = word[0]

    if first_letter in result:
        result[first_letter].append(word)
    else:
        result[first_letter] = [word]

print(result)