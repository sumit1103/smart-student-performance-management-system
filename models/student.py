from models.user import User


class Student(User):

    def __init__(self, student_id, name, age, email, course, subjects, marks):

        super().__init__(student_id, name, email)

        self.student_id = student_id
        self.age = age
        self.course = course
        self.subjects = subjects
        self.__marks = marks

    def display_role(self):
        return "Role: Student"

    def get_marks(self):
        return self.__marks

    def set_marks(self, marks):
        for mark in marks:
            if mark < 0 or mark > 100:
                raise ValueError("Marks should be between 0 and 100.")

        self.__marks = marks

    def calculate_total(self):
        return sum(self.__marks)

    def calculate_average(self):
        if not self.__marks:
            raise ZeroDivisionError("No marks available.")

        return sum(self.__marks) / len(self.__marks)

    def calculate_highest(self):
        if not self.__marks:
            raise ValueError("No marks available.")

        return max(self.__marks)

    def calculate_lowest(self):
        if not self.__marks:
            raise ValueError("No marks available.")

        return min(self.__marks)

    def calculate_grade(self):
        average = self.calculate_average()

        if average >= 90:
            return "A+"
        elif average >= 80:
            return "A"
        elif average >= 70:
            return "B"
        elif average >= 60:
            return "C"
        elif average >= 50:
            return "D"
        else:
            return "F"


def calculate_total(*marks):
    return sum(marks)


def create_student(**details):
    return details