from flask import Flask, request, jsonify

app = Flask(__name__)

# Predefined landmark data
landmarks = {
    1: {"name": "Eiffel Tower", "location": "Paris, France", "year_built": 1889},
    2: {"name": "Statue of Liberty", "location": "New York City, USA", "year_built": 1886},
    3: {"name": "Great Wall of China", "location": "China", "year_built": "7th century BC"}
}

@app.route('/')
def home():
    return "Welcome, please change the URL to get the landmark details accordingly"

# Endpoint to get a specific landmark by ID or Name
# URL as landmark?id=1 
@app.route('/landmark', methods=['GET'])
def get_landmark():
    landmark_id = request.args.get('id')
    name = request.args.get('name')

    if landmark_id:
        try:
            landmark_id = int(landmark_id)
            landmark = landmarks.get(landmark_id)
            
            if landmark_id:
                # jsonify to convert the dictionary into a JSON (JavaScript Object Notation) format. This is the standard way to send data from a web server to a client (e.g., a web browser).
                return jsonify(landmark)  # Return as JSON
            else:
                #landmark?id=400 
                return "Landmark not found by ID", 404  # Include HTTP status code
        except ValueError:
            #landmark?id=abc
            return "Invalid 'id' parameter. Must be an integer.", 400  # Include HTTP status code
    elif name:
        name_lower = name.lower()
        for landmark_id, landmark in landmarks.items(): #Iterate through items
            if landmark["name"].lower() == name_lower:
                return jsonify(landmark)  # Return as JSON
        return "Landmark not found by name", 404  # Include HTTP status code
    else:
        return "Please provide either 'id' or 'name' as query parameter", 400  # Include HTTP status code

if __name__ == '__main__':
    app.run(debug=True)