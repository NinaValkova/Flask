"""
Write python code to do simple calculation using given functions: add, subtract, multiply, divide.
2 integer values are passed to the function and the function returns the output.
"""

"""Function the sum of a and b."""
def add(num1, num2):
    sum = num1 + num2
    
    return sum

"""Function the difference between a and b."""
def subtract(num1, num2):
    sum = num1 - num2
    
    return sum

"""Function the product of a and b."""
def multiply(num1, num2):
    sum = num1 * num2
    
    return sum

"""Function the quotient of a and b.
Raises:
ValueError: If b is 0.

"""
def divide(num1, num2):
    try:
        sum = num1 / num2
    except ValueError:
        return "b is 0"
    
    return sum
    
if __name__ == "__main__":
    num1 = 10
    num2 = 5

    print("Addition:", add(num1, num2))
    print("Subtraction:", subtract(num1, num2))
    print("Multiplication:", multiply(num1, num2))
    print("Division:", divide(num1, num2))
