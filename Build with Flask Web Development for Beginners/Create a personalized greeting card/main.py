from flask import Flask, render_template, request, redirect, url_for
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def index():
    # Render the greeting page without user's name and occasion
    return render_template('greeting.html')

#URL as /greeting?name=Joe&occ=Holi
@app.route('/greeting')
def greeting():
    # Get the user's input from the query parameters
    name = request.args.get('name')
    occasion = request.args.get('occ')

    #  Render the greeting page with user's name and occasion
    return render_template('greeting.html', name=name,occasion=occasion)

if __name__ == '__main__':
    app.run(debug=True)
