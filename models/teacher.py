from models.user import User


class Teacher(User):

    def __init__(self, user_id, name, email, subject, assigned_students):

        super().__init__(user_id, name, email)

        self.subject = subject
        self.assigned_students = assigned_students

    def display_role(self):
        return "Role: Instructor"