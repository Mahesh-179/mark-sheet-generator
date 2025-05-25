from prettytable import PrettyTable
# 0. Heading Display
print("===========================================================")
print("             PYTHON MARKSHEET GENERATOR                    ")
print("===========================================================\n")

# 1. Take student information
user_name = input("Enter your name: ").capitalize()
user_class = input("Enter your class name: ").capitalize()
user_dob = input("Enter your Date of Birth (YYYY-MM-DD): ")

# 2. Subject list
subjects = ["Science", "Social", "Mathematics", "Nepali", "English", "Optional", "Health"]
marks = {}
total = 0

# 3. Input marks one by one
for subject in subjects:
    mark = int(input(f"Enter marks for {subject}: "))
    marks[subject] = mark
    total += mark

# 4. Calculate percentage
percentage = total / len(subjects)

# 5. Display student info
print("\n=============== STUDENT DETAILS ===============")
print(f"Name       : {user_name}")
print(f"Class      : {user_class}")
print(f"DOB        : {user_dob}")

# 6. Generate and display marks table
markstable = PrettyTable()
markstable.field_names = ["Subject", "Marks"]

for subject in subjects:
    markstable.add_row([subject, marks[subject]])

print("\n---------------- MARKSHEET ----------------")
print(markstable)
print(f"Total Marks: {total}")
print(f"Percentage : {percentage:.2f}%")


# 7.Grade Division 
if percentage >=80:
    print("You have passed with Distinction")
elif percentage >= 70:
    print("You have passed with First Division")
elif percentage >= 60:
    print("You have passed with Second Division")
elif percentage >= 50:
    print("You have passed with Third Division")
elif percentage >= 40:
    print("YOU HAVE FAILED")