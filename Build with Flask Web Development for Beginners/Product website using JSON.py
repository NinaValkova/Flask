"""
Task:
The first api - /api/products should display all the products in json format.

The second api - /api/products/1 should display the product with id 1 and so on.

And if the product with the particular id doesn't exist like this /api/products/100 then it should show error :

image
 
"""

from flask import Flask, jsonify, render_template, abort

app = Flask(__name__)

products = [
    {"id": 1, "name": "Laptop", "price": 1200.50, "category": "Electronics"},
    {"id": 2, "name": "Mouse", "price": 25.00, "category": "Accessories"},
    {"id": 3, "name": "Keyboard", "price": 75.75, "category": "Accessories"},
    {"id": 4, "name": "Monitor", "price": 300.00, "category": "Electronics"},
    {"id": 5, "name": "Webcam", "price": 55.00, "category": "Accessories"}
]

# write an api to show all the products in json format
@app.route('/api/products', methods=['GET'])
def get_products():
    # The jsonify function in Flask helps to convert Python dictionaries or lists to JSON 
    return jsonify(products)


# write an api to show the product details based on particular id
@app.route('/api/products/<int:product_id>', methods=['GET'])
def get_product(product_id ):
    product = next((product for product in products if product['id']==product_id ), None)

    if product:
        return jsonify(product)
    else:
        return jsonify({"error": "Product not found", "id": product_id})    



@app.route('/')
def show_products_html():
    return render_template('products_display.html',
                           products_list=products)

# --- Run the App ---
if __name__ == '__main__':
    app.run(debug=True)