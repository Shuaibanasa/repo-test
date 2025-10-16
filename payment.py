def pay(amount, method):
    if method == "credit_card":
        return f"Paid {amount} using credit card."
    elif method == "paypal":
        return f"Paid {amount} using PayPal."
    else:
        return "Payment method not supported."


def wallet_payment():
    pass
