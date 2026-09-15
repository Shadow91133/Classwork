#Task 1
print("This is task 1")

HoursWorked = float(input("Enter Your Work Hours : "))

HourlyRate = float(input("Enter Your Hourly Rate : "))


if HoursWorked <= 40 :
		print("Your Total Pay is :",HoursWorked*HourlyRate)
		
else :
		overtime = HoursWorked - 40
		totalpay = (HourlyRate*40)+(overtime*1.5)		
		print("Your Total Pay is : ",totalpay)	
		
							
												
#Task 2

#Task 2
print("This is Task 2")


StudentName = input("Enter Your Name : ")

StudentRollNum = int(input("Enter Your Roll Number : "))

subjects = [
    "Urdu",
    "English",
    "Programming",
    "Science",
    "Maths",
]
marks = []
for subj in subjects:
    m = float(input(f"Enter marks for {subj}: "))
    marks.append(m)
num_subjects = len(subjects)
total = sum(marks)
percentage = total / num_subjects

if percentage >= 80:
    grade = "A+"
elif percentage >= 70:
    grade = "A"
elif percentage >= 60:
    grade = "B"
elif percentage >= 50:
    grade = "C"
elif percentage >= 40:
    grade = "D"
else:
    grade = "F"

failed_subject = any(m < 40 for m in marks)

if failed_subject or percentage < 40:
    result = "Fail"
else:
    result = "Pass"

print("\n MARKSHEET ")
print(f"StudentName : {StudentName}")
print(f"StudentRollNum : {StudentRollNum}")
for subj, m in zip(subjects, marks):
    print(f"{subj:<38}: {m}")
print(f"Total : {total}")
print(f"Percentage : {percentage:.2f}%")
print(f"Grade : {grade}")
print(f"Result : {result}")
print("--------------")																																												