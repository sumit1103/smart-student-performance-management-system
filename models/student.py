from models.user import User


class Student(User):
    """Represent a student and manage academic performance."""

    def __init__(self, student_id, name, age, email, course, subjects, marks):
        """Initialize student details and marks."""
        super().__init__(student_id, name, email)

        self.student_id = student_id
        self.age = age
        self.course = course
        self.subjects = subjects
        self.__marks = marks

    def display_role(self):
        """Return the role of the user."""
        return "Role: Student"

    def get_marks(self):
        """Return the student's marks."""
        return self.__marks

    def set_marks(self, marks):
        """Update marks after validating the values."""
        for mark in marks:
            if mark < 0 or mark > 100:
                raise ValueError("Marks should be between 0 and 100.")

        self.__marks = marks

    def calculate_total(self):
        """Calculate the total marks."""
        return sum(self.__marks)

    def calculate_average(self):
        """Calculate the average marks."""
        if not self.__marks:
            raise ZeroDivisionError("No marks available.")

        return sum(self.__marks) / len(self.__marks)

    def calculate_highest(self):
        """Return the highest mark."""
        if not self.__marks:
            raise ValueError("No marks available.")

        return max(self.__marks)

    def calculate_lowest(self):
        """Return the lowest mark."""
        if not self.__marks:
            raise ValueError("No marks available.")

        return min(self.__marks)

    def calculate_grade(self):
        """Return the grade based on the average marks."""
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
    """Calculate total marks using variable positional arguments."""
    return sum(marks)


def create_student(**details):
    """Create student details using keyword arguments."""
    return details