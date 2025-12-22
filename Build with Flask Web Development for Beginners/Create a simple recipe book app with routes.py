"""
Complete the Flask application by adding the necessary routes using decorators.
The application should have the following routes:

A home page at '/'
A page to view all recipes at '/recipes'
A page to view individual recipes at '/recipe/int:recipe_id'
"""
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return 'Welcome to the Recipe Book!'

@app.route('/recipes')
def recipes():
    return 'Here are all the recipes.'

@app.route('/recipe/<int:recipe_id>')
def view_recipe(recipe_id):
    return f'Viewing recipe {recipe_id}'

if __name__ == "__main__":
    app.run()
