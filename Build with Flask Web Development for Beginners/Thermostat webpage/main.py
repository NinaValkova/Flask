from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

target_temperature = 21

@app.route('/')
def show_thermostat():
    return render_template('thermostat.html', current_temp=target_temperature)

# complete the route that handles the temperature change request.

@app.route('/set-temperature', methods=['POST'])
def set_temperature():
    global target_temperature
    # Accessing data from a form post
    temperature_input = request.form['temperature']

    new_temperature = int(temperature_input)
    target_temperature = new_temperature

    # url_for function is used to get the url for the particular function passed in the function. This is a special function in FLASK.
    return redirect(url_for('show_thermostat'))



if __name__ == '__main__':
    app.run(debug=True)