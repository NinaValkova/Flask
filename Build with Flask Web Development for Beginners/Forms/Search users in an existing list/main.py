from flask import Flask, render_template, request, redirect, url_for
from wtforms import Form, StringField, SubmitField
from wtforms.validators import Optional

app = Flask(__name__)

users = [
    {'name': 'Alice', 'email': 'alice@example.com'},
    {'name': 'Bob', 'email': 'bob@example.com'},
    {'name': 'Charlie', 'email': 'charlie@example.com'},
    {'name': 'David', 'email': 'david@example.com'}
]

class SearchForm(Form):
    search = StringField('Search by name or email', validators=[Optional()])
    submit = SubmitField('Search')

@app.route('/', methods=['GET'])
def show_search():
    form = SearchForm()
    return render_template('search.html', form=form, results=[])

@app.route('/search', methods=['POST'])
def handle_search():
    form = SearchForm(request.form)
    results = users

    if form.validate():
        # if form.search.data is None → it becomes ""
        query = (form.search.data or "").strip().lower()
        if query:
            results = [
                user for user in users
                if query in user['name'].lower() or query in user['email'].lower()
            ]
        else:
            return render_template('search.html', form=form, results=[])
    return render_template('search.html', form=form, results=results)

if __name__ == '__main__':
    app.run(debug=True)
