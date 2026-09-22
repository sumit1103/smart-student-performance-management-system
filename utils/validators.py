def validate_marks(marks):
    for mark in marks:
        if mark < 0 or mark > 100:
            return False

    return True