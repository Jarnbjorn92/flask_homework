from flask import render_template
from app import app
from models.customer import Customer
from models.music_shop import orders

@app.route('/orders')
def index():
    return render_template('index.html', title='Home', orders=orders)

@app.route('/orders/<int:id>')
def order(id):
    one_order=orders[id]
    return render_template('order.html', title='Home', orders=one_order)