# This is a simple calculator program in Python

# Function to perform the calculations
def calculate(expression):
    try:
        # Evaluate the expression and return the result
        return eval(expression)
    except:
        # Return an error message
        return "Hatalı bir işlem yaptınız"

# Main program loop
while True:
    # Get the user's input
    expression = input("Lütfen işlemi giriniz: ")

    # Exit the program if the user enters 'q'
    if expression == 'q':
        break

    # Print the result of the calculation
    print("Sonuç:", calculate(expression))
