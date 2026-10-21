students_dict = {
    "Alice": "A",
    "Bob": "B",
    "Charlie": "C"
}

name = input("Enter student name: ")

if name in students_dict:
    print("Current grade:", students_dict[name])
    grade = input("Enter updated grade: ")
    students_dict[name] = grade
    print("Grade updated successfully!")
else:
    grade = input("Enter new student's grade: ")
    students_dict[name] = grade
    print("New student added successfully!")

print("\nAll Student Grades:")

for name, grade in students_dict.items():
    print(name, ":", grade)
