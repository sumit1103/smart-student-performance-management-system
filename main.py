from models.student import Student, calculate_total, create_student

student_id = int(input("Enter Student ID: "))
name = input("Enter Name: ")
age = int(input("Enter Age: "))
email = input("Enter Email: ")
course = input("Enter Course: ")

subjects = []
marks = []

for i in range(3):
    subject = input(f"Enter Subject {i + 1}: ")
    mark = int(input(f"Enter Marks for {subject}: "))

    subjects.append(subject)
    marks.append(mark)

student1 = Student(
    student_id,
    name,
    age,
    email,
    course,
    subjects,
    marks
)

print("\nStudent Details")
print("ID:", student1.student_id)
print("Name:", student1.name)
print("Age:", student1.age)
print("Email:", student1.email)
print("Course:", student1.course)
print("Subjects:", student1.subjects)
print("Marks:", student1.marks)

print("Total:", student1.calculate_total())
print("Average:", f"{student1.calculate_average():.2f}")
print("Highest:", student1.calculate_highest())
print("Lowest:", student1.calculate_lowest())
print("Grade:", student1.calculate_grade())


# List
student_names = ["Rahul", "Priya", "Amit"]
print("\nStudents:", student_names)


# Tuple
course_info = ("Python", "3 Months")
print("Course Info:", course_info)


# Set
unique_subjects = {"Python", "SQL", "Python", "Git"}
print("Unique Subjects:", unique_subjects)


# Dictionary
student_info = {
    "id": "ST101",
    "name": "Rahul",
    "age": 21
}
print("Student Info:", student_info)


# Students data for comprehensions
students = [
    {"name": "Rahul", "average": 91.67, "grade": "A+"},
    {"name": "Priya", "average": 85.50, "grade": "A"},
    {"name": "Amit", "average": 72.00, "grade": "B"},
    {"name": "Neha", "average": 88.00, "grade": "A"}
]


# List comprehension
top_students = [
    student for student in students
    if student["average"] > 80
]

print("\nTop Students:", top_students)


# Dictionary comprehension
student_scores = {
    student["name"]: student["average"]
    for student in students
}

print("Student Scores:", student_scores)


# Set comprehension
grades = {
    student["grade"]
    for student in students
}

print("Unique Grades:", grades)