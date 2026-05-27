# ============================================================
# PYTHON CALCULATOR - Beginner Portfolio Project
# Author: Your Name
# Description: A simple terminal calculator that supports
#              addition, subtraction, multiplication, division
# ============================================================


# ─────────────────────────────────────────────
# SECTION 1: HELPER FUNCTIONS
# Each function handles one math operation.
# Functions keep our code organized and reusable.
# ─────────────────────────────────────────────

def add(num1, num2):
    """Returns the sum of two numbers."""
    return num1 + num2


def subtract(num1, num2):
    """Returns the difference of two numbers."""
    return num1 - num2


def multiply(num1, num2):
    """Returns the product of two numbers."""
    return num1 * num2


def divide(num1, num2):
    """
    Returns the result of dividing num1 by num2.
    Returns None if num2 is zero (can't divide by zero!).
    """
    if num2 == 0:
        return None  # Signal that division by zero was attempted
    return num1 / num2


# ─────────────────────────────────────────────
# SECTION 2: DISPLAY HELPERS
# Functions that handle printing to the screen.
# Keeping print statements in one place makes
# it easy to restyle the output later.
# ─────────────────────────────────────────────

def print_separator():
    """Prints a decorative line to separate sections."""
    print("─" * 40)


def print_welcome():
    """Prints the welcome banner shown at startup."""
    print("\n" + "=" * 40)
    print("   🧮  PYTHON CALCULATOR  🧮")
    print("=" * 40)
    print("  Operations: +  -  *  /")
    print("  Type 'exit' at any prompt to quit.")
    print("=" * 40 + "\n")


def print_result(num1, operator, num2, result):
    """Prints the calculation and its result in a clean format."""
    print_separator()
    # Format numbers: show as int if they're whole numbers (e.g. 5 not 5.0)
    formatted_num1 = int(num1) if num1 == int(num1) else num1
    formatted_num2 = int(num2) if num2 == int(num2) else num2
    formatted_result = int(result) if result == int(result) else round(result, 6)

    print(f"  {formatted_num1} {operator} {formatted_num2} = {formatted_result}")
    print_separator()


# ─────────────────────────────────────────────
# SECTION 3: INPUT FUNCTIONS
# These functions ask the user for input and
# validate it before returning a value.
# ─────────────────────────────────────────────

def get_number(prompt):
    """
    Asks the user to enter a number.
    Keeps asking until they enter a valid number or 'exit'.
    Returns the number as a float, or the string 'exit'.
    """
    while True:  # Loop until we get valid input
        user_input = input(prompt).strip()  # .strip() removes accidental spaces

        # Allow the user to quit at any prompt
        if user_input.lower() == "exit":
            return "exit"

        try:
            # Try converting the input to a float (works for integers too)
            number = float(user_input)
            return number
        except ValueError:
            # If conversion fails, the user typed something that's not a number
            print("  ⚠️  Invalid input. Please enter a number (e.g. 5, -3, 2.7).\n")


def get_operator():
    """
    Asks the user to enter a math operator.
    Keeps asking until they enter a valid one or 'exit'.
    Returns the operator as a string, or 'exit'.
    """
    valid_operators = ["+", "-", "*", "/"]

    while True:
        user_input = input("  Enter operator (+, -, *, /): ").strip()

        if user_input.lower() == "exit":
            return "exit"

        if user_input in valid_operators:
            return user_input
        else:
            print("  ⚠️  Invalid operator. Please use +, -, *, or /.\n")


# ─────────────────────────────────────────────
# SECTION 4: CALCULATE FUNCTION
# This is the brain of the calculator.
# It takes two numbers and an operator, then
# calls the right math function and returns
# the result (or an error message).
# ─────────────────────────────────────────────

def calculate(num1, operator, num2):
    """
    Performs the calculation based on the operator.
    Returns the numeric result, or None if division by zero.
    """
    if operator == "+":
        return add(num1, num2)
    elif operator == "-":
        return subtract(num1, num2)
    elif operator == "*":
        return multiply(num1, num2)
    elif operator == "/":
        return divide(num1, num2)


# ─────────────────────────────────────────────
# SECTION 5: MAIN PROGRAM LOOP
# This is where everything comes together.
# The while loop keeps the calculator running
# until the user types 'exit'.
# ─────────────────────────────────────────────

def main():
    """Main function — runs the calculator loop."""
    print_welcome()

    while True:  # Keep running until the user exits
        print("  New Calculation")
        print_separator()

        # --- Step 1: Get the first number ---
        num1 = get_number("  Enter first number:  ")
        if num1 == "exit":
            break  # Exit the while loop

        # --- Step 2: Get the operator ---
        operator = get_operator()
        if operator == "exit":
            break

        # --- Step 3: Get the second number ---
        num2 = get_number("  Enter second number: ")
        if num2 == "exit":
            break

        # --- Step 4: Calculate the result ---
        result = calculate(num1, operator, num2)

        # --- Step 5: Display the result ---
        if result is None:
            # divide() returns None when dividing by zero
            print_separator()
            print("  ❌  Error: Cannot divide by zero!")
            print_separator()
        else:
            print_result(num1, operator, num2, result)

        # --- Step 6: Ask to continue or quit ---
        print()
        again = input("  Calculate again? (press Enter or type 'exit'): ").strip()
        print()
        if again.lower() == "exit":
            break  # User chose to quit

    # Farewell message shown when the loop ends
    print("\n" + "=" * 40)
    print("  Thanks for using Python Calculator!")
    print("  Goodbye! 👋")
    print("=" * 40 + "\n")


# ─────────────────────────────────────────────
# SECTION 6: ENTRY POINT
# This block runs main() only when the script
# is executed directly (not when imported).
# It's a Python best practice.
# ─────────────────────────────────────────────

if __name__ == "__main__":
    main()