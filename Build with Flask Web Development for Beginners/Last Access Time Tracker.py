# Task
# Complete the Flask application given in the IDE

# Imports the necessary modules
# Creates a Flask app instance
# Defines a global variable to store the last access time
# Creates a route that updates the last access time and returns the 'message'


from flask import Flask
from datetime import datetime  # Import datetime to track time

app = Flask(__name__)

# Global variable to store the last access time.
last_access_time = None

@app.route('/')
def track_last_access():
    global last_access_time
    # Get the current time formatted as a readable string.
    # datetime.now() fetches the current time from the server's system, not the user's machine.
    # To display the user's local time, you need to get the time on the client-side using JavaScript.
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    # If this is the first access, notify the user accordingly.
    if last_access_time is None:
        message = "This is the first access!"
    else:
        message = f"Last accessed at: {last_access_time}"
    
    # Update the last access time to the current time.
    last_access_time = current_time
    
    return message

if __name__ == '__main__':
    # Run the Flask application in debug mode.
    # Flask's debug mode - for identify the error 
    app.run(debug=True)
