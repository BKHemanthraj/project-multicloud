from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Sample Data for Menu and Orders
menu = [
    {"id": 1, "name": "Pizza", "price": 250},
    {"id": 2, "name": "Burger", "price": 150},
    {"id": 3, "name": "Pasta", "price": 200},
    {"id": 4, "name": "Ice Cream", "price": 100},
]

orders = []

@app.route('/')
def home():
    return render_template('dashboard.html')

@app.route('/menu')
def view_menu():
    return render_template('menu.html', menu=menu)

@app.route('/order', methods=['GET', 'POST'])
def place_order():
    if request.method == 'POST':
        food_id = int(request.form['food_id'])
        quantity = int(request.form['quantity'])
        food_item = next((item for item in menu if item['id'] == food_id), None)
        if food_item:
            order = {
                "id": len(orders) + 1,
                "food_name": food_item['name'],
                "quantity": quantity,
                "total_price": food_item['price'] * quantity
            }
            orders.append(order)
            return redirect(url_for('order_history'))
    return render_template('order.html', menu=menu)

@app.route('/history')
def order_history():
    return render_template('history.html', orders=orders)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)

  
 
