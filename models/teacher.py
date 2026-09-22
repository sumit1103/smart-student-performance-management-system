from models.user import User


class Teacher(User):
    """Represent a teacher and their assigned students."""

    def __init__(self, user_id, name, email, subject, assigned_students):
        """Initialize teacher details."""
        super().__init__(user_id, name, email)

        self.subject = subject
        self.assigned_students = assigned_students

    def display_role(self):
        """Return the role of the user."""
        return "Role: Instructor"