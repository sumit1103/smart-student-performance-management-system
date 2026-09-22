from models.student import Student
from models.teacher import Teacher


student = Student(
    101,
    "Rahul",
    20,
    "rahul@gmail.com",
    "Python",
    ["Math", "Science", "English"],
    [88, 89, 98]
)

teacher = Teacher(
    201,
    "Anil",
    "anil@gmail.com",
    "Python",
    [101]
)


print("Student Details")
print("ID:", student.user_id)
print("Name:", student.name)
print("Email:", student.email)
print("Course:", student.course)

print("\nTeacher Details")
print("ID:", teacher.user_id)
print("Name:", teacher.name)
print("Email:", teacher.email)
print("Subject:", teacher.subject)
print("Assigned Students:", teacher.assigned_students)


print("\nPolymorphism")
print(student.display_role())
print(teacher.display_role())


print("\nEncapsulation")
print("Current Marks:", student.get_marks())

student.set_marks([90, 92, 95])

print("Updated Marks:", student.get_marks())