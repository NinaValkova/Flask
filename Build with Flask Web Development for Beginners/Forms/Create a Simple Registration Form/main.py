from flask import Flask, request, render_template, jsonify

app = Flask(__name__)

submissions_store = []

@app.route('/')
def index():
    return render_template('register.html')

# write the api to take the input from the html form, update the global list and give the json response.
@app.route('/submit', methods=['POST'])
def submit_data():
    name = request.form.get('user_name')
    email = request.form.get('user_email')
    phone = request.form.get('user_phone')

    new_submission = {
        'name': name,
        'email': email,
        'phone': phone
    }

    submissions_store.append(new_submission)

    return jsonify(submissions_store)

if __name__ == '__main__':
    app.run(debug=True)