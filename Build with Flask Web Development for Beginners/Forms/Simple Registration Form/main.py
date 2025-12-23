#work with HTML Forms using Flask
from flask import Flask, request, render_template, url_for, redirect

app = Flask(__name__)

dishes = [
    {
        'dish_name': 'Pasta',
        'recipe': '1. Cook spaghetti. 2. Fry pancetta/guanciale. 3. Whisk eggs, Pecorino Romano, black pepper. 4. Drain pasta (reserve water). 5. Combine pasta with pancetta. 6. Off heat, mix in egg mixture quickly, adding pasta water if needed. Serve immediately.'
    },
    {
        'dish_name': 'Scrambled Eggs',
        'recipe': '1. Whisk 2-3 eggs with a splash of milk/cream, salt, and pepper. 2. Melt butter in a non-stick pan over medium-low heat. 3. Pour in eggs, let set slightly. 4. Gently push cooked egg towards the center, tilting pan. 5. Remove just before fully set.'
    },
    {
        'dish_name': 'Salad',
        'recipe': '1. Make dressing: whisk egg yolk, Dijon, garlic, lemon juice, Worcestershire, anchovy paste (optional). Slowly whisk in oil. Stir in Parmesan. 2. Toss romaine lettuce with dressing. 3. Add croutons and more Parmesan.'
    }
]


@app.route('/search', methods=['POST'])
def search_dish():
    found_dish_details = None
    error_message = None
    dish_query = ''

    dish_query = request.form.get('dish_query')

    if not dish_query:
        return render_template('dish.html', error="Please enter a dish name.")
    
    dish_query_lower = dish_query.lower()
    # update your code below this line to show the recipe on the webpage.

    found_dish = None
    for dish in dishes:
        if dish_query_lower == dish['dish_name'].lower():
            found_dish = dish
            return render_template('dish.html', found_dish=found_dish)
    
    error_message = f"Dish '{dish_query}' not found."    
    return render_template('dish.html', error=error_message)

@app.route('/')
def root_redirect():
    return render_template('dish.html')


if __name__ == '__main__':
    app.run(debug=True)