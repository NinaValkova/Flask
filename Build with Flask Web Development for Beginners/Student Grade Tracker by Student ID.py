"""
    The application should have one route - A route to list all students and their grades.
"""

from flask import Flask, abort

app = Flask(__name__)

# Sample student grade database
students = {
    101: {"name": "Alice", "grade": "A"},
    102: {"name": "Bob", "grade": "B"},
    103: {"name": "Charlie", "grade": "C"}
}

@app.route('/')
def list_students():
    return f"Change the URL to see the grades of the students"

@app.route('/student/<int:id>')
def get_student(id):
    if id in students:
        student = students[id]
        return f"Student ID: {id}<br>Name: {student['name']}<br>Grade: {student['grade']}"
    else:
        # If you do: return "Student not found" Flask returns status 200 OK by default — meaning “everything worked”, even though the student wasn’t found.
        # If you do: abort(404, description="Student not found") Flask returns status 404 Not Found — meaning “the resource doesn’t exist”.
        abort(404, description="Student not found")
        # Use Flask's abort() function or return custom error messages when necessary.( return "User not found", 404) 

if __name__ == '__main__':
    app.run(debug=True)
