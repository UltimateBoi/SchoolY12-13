def validate_grade(grade):
    # Check if the grade is within the valid range
    if 0 <= grade <= 100:
        return "Valid grade"
    else:
        return "Invalid grade"