from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField

app = Flask(__name__)
app.config["SECRET_KEY"] = "mysecretkey"


# own form class
class InfoForm(FlaskForm):
    breed = StringField("What Breed are you?")
    submit = SubmitField("Submit")


@app.route("/", methods=["GET", "POST"])
def index():
    breed = False
    form = InfoForm()

    if form.validate_on_submit():
        breed = form.breed.data
        # reset data - clears the text input field after the form is successfully submitted.
        form.breed.data = ""
    return render_template("index.html", form=form, breed=breed)


if __name__ == "__main__":
    app.run(debug=True)
