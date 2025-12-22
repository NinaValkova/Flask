# app.py
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return f"Change the URL to see the product details."

@app.route('/product')
def show_product():
    # Define product data as a dictionary
    product_info = {
        'id': "XYZ123",
        'name': "Wireless Mouse",
        'description': "A comfortable and reliable wireless mouse.",
        'price': 24.99,
    }

    # Pass the dictionary to the template under the variable name 'product'
    return render_template("product_details.html",product=product_info)
    

if __name__ == '__main__':
    app.run(debug=True)