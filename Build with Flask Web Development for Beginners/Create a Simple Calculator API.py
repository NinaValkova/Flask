"""
Create a Simple Calculator API
Let us complete Calculator API application.

Task:
Update the 'Subtraction', 'Multiplication' and 'Division' endpoints in the IDE.
"""
from flask import Flask, Response

app = Flask(__name__)

# Root endpoint remains the same
@app.route('/')
def home():
    # Returns a simple welcome message as plain text
    return f"Welcome to the Calculator API!"

# Addition endpoint - returns only the result as plain text
@app.route('/add/<int:a>/<int:b>')
def add(a, b):
    result = a + b
    # Convert the numerical result to a string for the Response body
    return f"{result}"

# Subtraction endpoint - returns only the result as plain text
@app.route('/subtract/<int:a>/<int:b>')
def subtract(a, b):
    result = a - b
    # Convert the numerical result to a string for the Response body
    return f"{result}"


# Multiplication endpoint - returns only the result as plain text
@app.route('/multiply/<int:a>/<int:b>')
def multiply(a, b):
    result = a * b
    # Convert the numerical result to a string for the Response body
    return f"{result}"


# Division endpoint - returns result or error message as plain text
@app.route('/divide/<int:a>/<int:b>')
def divide(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        return "Error: Division by zero"    
    # Convert the numerical result to a string for the Response body
    return f"{result}"

# def divide(a, b):
#     if b == 0:
#         # Return only the error message string with a 400 status code
#         return f"Error: Division by zero"
#     result = a / b
#     # Convert the numerical result (potentially a float) to a string
#     return f"{result}"


if __name__ == '__main__':
    # Run in debug mode for development
    app.run(debug=True)