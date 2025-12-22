"""
Let's create a simple routing flask application.
Task:
Write the app routes which on home("/") should return "Welcome to the Calculator API!" on webpage.image
Write an endpoint in the IDE to do addition of two numbers and display the result on the webpage.
"""

from flask import Flask

# Create a Flask application instance
app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to the Calculator API!"

@app.route('/add/<int:num1>/<int:num2>')    
def add(num1, num2):
    sum = num1 + num2
    
    # Convert the numerical result to a string for the Response body
    return f"{sum}"


if __name__ == '__main__':
  # debug=True enables auto-reloading and detailed error pages
  app.run(debug=True)