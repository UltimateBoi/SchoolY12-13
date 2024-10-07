def validate_grade(grade): #  This function checks if the provided grade is within the valid range (0 to 100). And is a number.
    if not isinstance(grade, (int, float)):  # Check if the input is a number
        return "Invalid input: grade must be a number"
    
    if 0 <= grade <= 100:  # Check if the grade is within the valid range
        return "Valid grade"
    else:
        return "Invalid grade"
