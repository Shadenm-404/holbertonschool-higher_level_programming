from flask import Flask, render_template, request
import json
import csv
import sqlite3

app = Flask(__name__)

# ---------- JSON ----------
def read_json():
    try:
        with open('products.json', 'r') as file:
            return json.load(file)
    except:
        return []

# ---------- CSV ----------
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

# ---------- SQLITE ----------
def read_sqlite():
    products = []
    try:
        conn = sqlite3.connect('products.db')
        cursor = conn.cursor()

        cursor.execute("SELECT id, name, category, price FROM Products")

        rows = cursor.fetchall()

        for row in rows:
            products.append({
                "id": row[0],
                "name": row[1],
                "category": row[2],
                "price": row[3]
            })

        conn.close()

    except:
        pass

    return products


@app.route('/products')
def products():

    source = request.args.get('source')
    product_id = request.args.get('id')

    # ✅ تحقق من المصدر
    if source not in ['json', 'csv', 'sql']:
        return render_template(
            'product_display.html',
            error="Wrong source",
            products=None
        )

    # ✅ اختيار المصدر
    if source == 'json':
        data = read_json()
    elif source == 'csv':
        data = read_csv()
    else:
        data = read_sqlite()

    # ✅ فلترة ID
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
