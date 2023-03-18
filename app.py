from flask import Flask, render_template, jsonify

app = Flask(__name__)

PRODUCTS = [
  {
    'id': 1,
    'item': 'Sofa',
    'category': 'Living Room Furniture',
    'color': 'Gray',
    'price': '800'
  },
  {
    'id': 2,
    'item': 'Dining Table',
    'category': 'Dining Room Furniture',
    'color': 'Brown',
    'price': '1200'
  },
  {
    'id': 3,
    'item': 'Bed',
    'category': 'Bedroom Furniture',
    'price': '1500'
  },
  {
    'id': 4,
    'item': 'Armchair',
    'category': 'Living Room Furniture',
    'color': 'Blue',
    'price': '500'
  },
]


@app.route("/")
def hello_modern():
  return render_template('home.html', products=PRODUCTS, company_name="Modern")


@app.route("/products")
def list_products():
  return jsonify(PRODUCTS)


if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
