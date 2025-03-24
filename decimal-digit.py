# 8.	Decimal Digit Transformation
# Write a function in an Object Orientated Programming language of your choice that, when passed a decimal digit X, calculates and returns the value of X + XX + XXX + XXXX. For example, if X is 3, the function should return 3702 (3 + 33 + 333 + 3333). Ensure the function handles valid inputs and provides meaningful error messages for invalid inputs.

def decimal_digit_transformation(X):
    # Calculate and add the value of X + XX + XXX + XXXX
    result = X + int(f"{X}{X}") + int(f"{X}{X}{X}") + int(f"{X}{X}{X}{X}")
    return result

# This function will get the user input only in int format from 0 to 9.
def get_user_input():
    while True:
        try:
            X = int(input("Enter a single decimal digit (0-9): "))
            if 0 <= X <= 9:
                return X
            else:
                print("Invalid input. Please enter a single decimal digit (0-9).")
        except ValueError:
            print("Invalid input. Please enter an integer.")

if __name__ == "__main__":
    X = get_user_input()
    result = decimal_digit_transformation(X)
    print(f"The result of the transformation for {X} is: {result}")