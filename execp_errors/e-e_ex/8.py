def process_transaction(balance, amount, transaction_type):
    """
    Process deposit/withdrawal.
    - Raise ValueError if amount <= 0
    - Raise ValueError if withdrawal > balance
    - Raise ValueError if invalid transaction_type

    Use else to print success message.
    Use finally to print "Transaction complete"
    Return new balance.
    """
    try:
        if amount <= 0:
            raise ValueError("Amount must be positive")

        if transaction_type == "deposit":
            balance += amount
        elif transaction_type == "withdrawal":
            if amount > balance:
                raise ValueError("Withdrawal must not exceed balance")
            balance -= amount
        else:
            raise ValueError("Invalid transaction type")

    except ValueError as e:
        print(f"Error: {e}")

    else:
        print("Success")

    finally:
        print("Transaction complete")

    return balance

# Test
print(process_transaction(100, 50, "deposit"))      # 150
print(process_transaction(100, 150, "withdraw"))    # Error
