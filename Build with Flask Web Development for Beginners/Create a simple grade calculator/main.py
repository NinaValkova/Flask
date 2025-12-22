from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def grade_calculator():
    # Define a list of student dictionaries with name and score.
    students = [
        {'name': 'Alice', 'score': 85.234},
        {'name': 'Bob', 'score': 59.567},
        {'name': 'Charlie', 'score': 72.3},
        {'name': 'David', 'score': 49.8},
        {'name': 'Eve', 'score': 91.456}
    ]
    # Render the 'grades.html' template with the students data.
    return render_template('grades.html', students=students)

if __name__ == '__main__':
    app.run(debug=True)
