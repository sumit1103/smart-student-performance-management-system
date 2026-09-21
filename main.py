from models.student import Student
from models.task import Task
import json

students = []
tasks = []


def add_student():
    try:
        student_id = int(input("Enter Student ID: "))
        age = int(input("Enter Age: "))
    except ValueError:
        print("Please enter valid numeric values.")
        return

    name = input("Enter Name: ")
    email = input("Enter Email: ")
    course = input("Enter Course: ")

    subjects = []
    marks = []

    for i in range(3):
        subject = input(f"Enter Subject {i + 1}: ")

        try:
            mark = float(input(f"Enter Marks for {subject}: "))

            if mark < 0 or mark > 100:
                print("Marks should be between 0 and 100.")
                return

        except ValueError:
            print("Please enter a valid mark.")
            return

        subjects.append(subject)
        marks.append(mark)

    student = Student(
        student_id,
        name,
        age,
        email,
        course,
        subjects,
        marks
    )

    students.append(student)

    print("\nStudent added successfully!")


def view_students():
    if not students:
        print("\nNo students found.")
        return

    print("\nStudent List")

    for student in students:
        print("--------------------")
        print("ID:", student.student_id)
        print("Name:", student.name)
        print("Age:", student.age)
        print("Email:", student.email)
        print("Course:", student.course)
        print("Subjects:", student.subjects)
        print("Marks:", student.marks)


def search_student():
    if not students:
        print("\nNo students found.")
        return

    search_value = input(
        "Enter Student ID, Name, or Course: "
    ).lower()

    found = False

    for student in students:
        if (
            str(student.student_id).lower() == search_value
            or student.name.lower() == search_value
            or student.course.lower() == search_value
        ):
            print("\nStudent Found")
            print("ID:", student.student_id)
            print("Name:", student.name)
            print("Age:", student.age)
            print("Email:", student.email)
            print("Course:", student.course)

            found = True

    if not found:
        print("Student not found.")


def calculate_performance():
    if not students:
        print("\nNo students found.")
        return

    for student in students:
        print("\n--------------------")
        print("Student:", student.name)
        print("Total:", student.calculate_total())

        try:
            print("Average:", f"{student.calculate_average():.2f}")
        except ZeroDivisionError:
            print("Average: Cannot calculate")

        print("Highest:", student.calculate_highest())
        print("Lowest:", student.calculate_lowest())
        print("Grade:", student.calculate_grade())


def add_task():
    task_id = input("Enter Task ID: ")
    task_name = input("Enter Task Name: ")
    description = input("Enter Description: ")
    deadline = input("Enter Deadline: ")
    priority = input("Enter Priority: ")

    task = Task(
        task_id,
        task_name,
        description,
        deadline,
        "Pending",
        priority
    )

    tasks.append(task)

    print("\nTask added successfully!")


def view_tasks():
    if not tasks:
        print("\nNo tasks found.")
        return

    print("\nTask List")

    for task in tasks:
        print("--------------------")
        print("Task ID:", task.task_id)
        print("Task:", task.task_name)
        print("Description:", task.description)
        print("Deadline:", task.deadline)
        print("Status:", task.status)
        print("Priority:", task.priority)


def complete_task():
    if not tasks:
        print("\nNo tasks found.")
        return

    task_id = input("Enter Task ID to complete: ")

    for task in tasks:
        if task.task_id == task_id:
            task.status = "Completed"
            print("Task marked as completed.")
            return

    print("Task not found.")


def delete_task():
    if not tasks:
        print("\nNo tasks found.")
        return

    task_id = input("Enter Task ID to delete: ")

    for task in tasks:
        if task.task_id == task_id:
            tasks.remove(task)
            print("Task deleted successfully.")
            return

    print("Task not found.")


def filter_tasks():
    if not tasks:
        print("\nNo tasks found.")
        return

    print("\n1. Pending Tasks")
    print("2. Completed Tasks")

    choice = input("Enter your choice: ")

    if choice == "1":
        status = "Pending"
    elif choice == "2":
        status = "Completed"
    else:
        print("Invalid choice.")
        return

    found = False

    for task in tasks:
        if task.status == status:
            print("--------------------")
            print("Task ID:", task.task_id)
            print("Task:", task.task_name)
            print("Status:", task.status)
            print("Priority:", task.priority)
            found = True

    if not found:
        print("No tasks found with this status.")


def delete_student():
    if not students:
        print("\nNo students found.")
        return

    try:
        student_id = int(input("Enter Student ID to delete: "))
    except ValueError:
        print("Please enter a valid Student ID.")
        return

    for student in students:
        if student.student_id == student_id:
            students.remove(student)
            print("Student deleted successfully.")
            return

    print("Student not found.")


def save_data():
    student_data = []
    task_data = []

    for student in students:
        student_data.append({
            "id": student.student_id,
            "name": student.name,
            "age": student.age,
            "email": student.email,
            "course": student.course,
            "subjects": student.subjects,
            "marks": student.marks
        })

    for task in tasks:
        task_data.append({
            "task_id": task.task_id,
            "task_name": task.task_name,
            "description": task.description,
            "deadline": task.deadline,
            "status": task.status,
            "priority": task.priority
        })

    try:
        with open("data/students.json", "w") as file:
            json.dump(student_data, file, indent=4)

        with open("data/tasks.json", "w") as file:
            json.dump(task_data, file, indent=4)

        print("Data saved successfully.")

    except FileNotFoundError:
        print("Data folder not found.")


while True:

    print("\n==============================")
    print("Student Management System")
    print("==============================")

    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Calculate Performance")
    print("5. Add Task")
    print("6. View Tasks")
    print("7. Complete Task")
    print("8. Delete Student")
    print("9. Save Data")
    print("10. Exit")
    print("11. Delete Task")
    print("12. Filter Tasks")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_student()

    elif choice == "2":
        view_students()

    elif choice == "3":
        search_student()

    elif choice == "4":
        calculate_performance()

    elif choice == "5":
        add_task()

    elif choice == "6":
        view_tasks()

    elif choice == "7":
        complete_task()

    elif choice == "8":
        delete_student()

    elif choice == "9":
        save_data()

    elif choice == "10":
        print("Exiting program...")
        break

    elif choice == "11":
        delete_task()

    elif choice == "12":
        filter_tasks()

    else:
        print("Invalid choice. Please try again.")