# my_flask_app/app.py
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('base.html')

if __name__ == '__main__':
    # Runs the app in debug mode for development
    app.run(debug=True)