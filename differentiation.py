# Function to calculate the derivative of x^n
def derivative(expr):
    # Split the expression to get the exponent
    parts = expr.split('^')

    # Ensure the expression is in the correct format
    if len(parts) == 2 and parts[0] == 'x':
        n = int(parts[1])  # Get the exponent
        # Calculate the derivative
        new_n = n - 1
        return f"{n}x^{new_n}" if new_n > 0 else str(n)  # Handle x^0 case

    return "Invalid input. Please enter in the form x^n."


# Get user input
user_input = input("Enter a polynomial term (e.g., x^3 or x^25): ")
result = derivative(user_input)

# Print the result
print(f"The derivative of {user_input} is: {result}")
