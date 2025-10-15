def payment(amount):
    if amount <= 0:
        return "Invalid amount"
    return f"Processed payment of ${amount}"