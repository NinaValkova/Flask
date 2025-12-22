""""
Create a Flask application that provides information about planets in our solar system.
The application should have a route that accepts a planet name as a dynamic segment in the URL and returns basic information about that planet.
Use a dictionary to store planet information.
"""
from flask import Flask

app = Flask(__name__)

# Dictionary storing one-line descriptions for each planet
planets = {
    "mercury": "Mercury is the smallest planet in our solar system and closest to the Sun.",
    "venus": "Venus is the second planet from the Sun, known for its extreme heat and thick atmosphere.",
    "earth": "Earth is the third planet from the Sun and the only known place to harbor life.",
    "mars": "Mars, often called the 'Red Planet', is the fourth planet from the Sun.",
    "jupiter": "Jupiter is the largest planet in our solar system, a gas giant known for its Great Red Spot.",
    "saturn": "Saturn is the sixth planet, famous for its stunning and complex ring system.",
    "uranus": "Uranus is the seventh planet, an ice giant tilted nearly onto its side.",
    "neptune": "Neptune is the eighth and farthest known planet, a dark, cold ice giant."
}

@app.route('/')
def home():
    return f"Welcome to the planet dictionary, to know about the planet write the planet's name in the url"

# Route that accepts a planet name and returns its description string
@app.route('/<name>')
def info(name):
    key = name.lower()
    if key in planets:
        return planets[key]

    return "Planet not found"    


if __name__ == '__main__':
    app.run(debug=True)