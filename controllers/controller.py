from flask import render_template
from app import app
from models.order import orders

@app.route('/orders')
def index():
    return render_template('index.html', title = "Ikant", currentorders = orders)

@app.route('/orders/<index>')
def order(index):
    return render_template('order.html', title = "Ikant", order = orders[int(index)])