def withdraw(amount, balance):
    # Check if the amount is within the allowed range
    if amount < 0 or amount > 500:
        return "Error: The amount must be between $0 and $500."
    
    # Check if there are sufficient funds in the balance
    if amount > balance:
        return "Error: Insufficient funds."
    
    # If both checks pass, perform the withdrawal
    balance -= amount
    return f"Success: You have withdrawn ${amount:.2f}. Your new balance is ${balance:.2f}."