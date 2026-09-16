class Student:

    #constructor to initialize student details
    def __init__(self, student_id, name, email, mobile, course, marks):

        #store the Student's data and save
        self.student_id = student_id
        self.name = name
        self.email = email
        self.mobile = mobile
        self.course = course
        self.marks = marks

    # Calculate the total marks of the student.
    def calculate_total(self):
        return sum(self.marks)

    # Calculate the average marks of the student.
    def calculate_average(self):
        return sum(self.marks) / len(self.marks)

    # Calculate the highest marks of the student.
    def calculate_highest(self):
        return max(self.marks)

    # Calculate the lowest marks of the student.
    def calculate_lowest(self):
        return min(self.marks)

    # Calculate the grade of the student.
    def calculate_grade(self):
        average = self.calculate_average()
        if average >= 90:
            return "A"
        elif average >= 80:
            return "B"
        elif average >= 70:
            return "C"
        elif average >= 60:
            return "D"
        else:
            return "F"

#tested by Object 1
student1 = Student(101, "Rahul", "rahul@gmail.com", 9988776688, "Python", [88, 89, 98])

#create 2nd student object
student2 = Student(102, "Ramesh", "ramesh@gmail.com", 9988776699, "Python", [78, 80, 85])

#create 3rd student object
student3 = Student(103, "Suresh", "suresh@gmail.com", 9988776677, "Python", [85, 87, 90])

#print the student's information
print("ID:", student1.student_id)
print("Name:", student1.name)
print("Email:", student1.email)
print("Mobile:", student1.mobile)
print("Course:", student1.course)
print("Marks:", student1.marks)

print("Total:", student1.calculate_total())
print("Average:", f"{student1.calculate_average():.2f}")
print("Highest:", student1.calculate_highest())
print("Lowest:", student1.calculate_lowest())
print("Grade:", student1.calculate_grade())

print("\nStudent 2:")
print("ID:", student2.student_id)
print("Name:", student2.name)
print("Email:", student2.email)
print("Mobile:", student2.mobile)
print("Course:", student2.course)
print("Marks:", student2.marks)

print("Total:", student2.calculate_total())
print("Average:", f"{student2.calculate_average():.2f}")
print("Highest:", student2.calculate_highest())
print("Lowest:", student2.calculate_lowest())
print("Grade:", student2.calculate_grade())

print("\nStudent 3:")
print("ID:", student3.student_id)
print("Name:", student3.name)
print("Email:", student3.email)
print("Mobile:", student3.mobile)
print("Course:", student3.course)
print("Marks:", student3.marks)

print("Total:", student3.calculate_total())
print("Average:", f"{student3.calculate_average():.2f}")
print("Highest:", student3.calculate_highest())
print("Lowest:", student3.calculate_lowest())
print("Grade:", student3.calculate_grade())