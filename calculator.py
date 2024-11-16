# Get user inputs
numberOne = input("Enter the first number or expression: ")
numberTwo = input("Enter the second number or expression: ")
mathOperation = input("Enter any mathematical operation (+, -, *, /): ")

try:
    # Convert inputs to numbers if they are valid, or evaluate if they are expressions
    numberOne = eval(numberOne) if mathOperation in ["+", "-", "*", "/"] else float(numberOne)
    numberTwo = eval(numberTwo) if mathOperation in ["+", "-", "*", "/"] else float(numberTwo)

    # Perform the calculation based on the operation
    if mathOperation == "+":
        result = numberOne + numberTwo
    elif mathOperation == "-":
        result = numberOne - numberTwo
    elif mathOperation == "*":
        result = numberOne * numberTwo
    elif mathOperation == "/":
        if numberTwo != 0:
            result = numberOne / numberTwo
        else:
            result = "Error: Division by zero is not allowed."

    # Display the result
    print(f"{numberOne} {mathOperation} {numberTwo} = {result}")

except ValueError:
    print("Error: Invalid input. Please enter a valid number or expression.")
except Exception as e:
    print(f"Error: {e}")
