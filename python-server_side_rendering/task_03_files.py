from flask import Flask, render_template, request
import json
import csv

app = Flask(__name__)

# ---------- READ JSON ----------
def read_json():
    try:
        with open('products.json', 'r') as file:
            return json.load(file)
    except:
        return []

# ---------- READ CSV ----------
def read_csv():
    products = []
    try:
        with open('products.csv', newline='') as file:
            reader = csv.DictReader(file)
            for row in reader:
                products.append({
                    "id": int(row["id"]),
                    "name": row["name"],
                    "category": row["category"],
                    "price": float(row["price"])
                })
    except:
        pass
    return products


@app.route('/products')
def products():

    source = request.args.get('source')
    product_id = request.args.get('id')

    # ---------- CHECK SOURCE ----------
    if source not in ['json', 'csv']:
        return render_template(
            'product_display.html',
            error="Wrong source",
            products=None
        )

    # ---------- LOAD DATA ----------
    data = read_json() if source == 'json' else read_csv()

    # ---------- FILTER BY ID ----------
    if product_id:
        product = [p for p in data if str(p["id"]) == product_id]

        if not product:
            return render_template(
                'product_display.html',
                error="Product not found",
                products=None
            )

        data = product

    return render_template(
        'product_display.html',
        products=data,
        error=None
    )


if __name__ == "__main__":
    app.run(debug=True, port=5000)
