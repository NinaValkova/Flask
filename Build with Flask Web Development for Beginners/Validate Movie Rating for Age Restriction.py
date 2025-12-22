"""
Create a Flask application that validates a user's age against a movie's rating.
The route should take two parameters: the user's age and the movie rating.
The application should handle cases where the age or rating is missing, invalid, or doesn't meet the criteria for watching the movie.

"""

from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Change the URL to see if the age is valid for that particular rating"

@app.route('/movie/<age>/<rating>')
def movie_access(age, rating):
    # Check whether the age is an integer or not
    try:
        age = int(age)
    except ValueError:
        return "Error: Age must be an integer"

    # Check whether the rating is R or PG13 and if not, give error
    rating = rating.upper()
    if rating not in ['PG13', 'R']:
        return "Error: Rating must be either 'PG13' or 'R'"

    if rating == 'PG13':
        if age < 13:
            return "Error: User is not old enough for PG13 movies"
        else:
            return "Access granted for PG13 movie"
    elif rating == 'R':
        if age < 17:
            return "Error: User is not old enough for R-rated movies"
        else:
            return "Access granted for R-rated movie"
        
    return "None"

if __name__ == '__main__':
    app.run(debug=True)