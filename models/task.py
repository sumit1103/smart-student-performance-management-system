class Task:
    """Represent a task assigned to a student."""

    def __init__(
        self,
        task_id,
        task_name,
        description,
        deadline,
        status,
        priority
    ):
        """Initialize task details."""
        self.task_id = task_id
        self.task_name = task_name
        self.description = description
        self.deadline = deadline
        self.status = status
        self.priority = priority