from flask import render_template, request, redirect, session, url_for
from flask_app.models.cookie import Order  #change this import line based on your extra .py file for generating OOP instances
from flask_app import app


@app.route("/cookies")     # lines 6 through 11 can be changed depending on what we need server.py to do.
def r_show_orders():
    # call the get all classmethod to get all friends
    orders = Order.get_all()
    return render_template("show_cookies.html", orders = orders)

@app.route('/cookies/add')
def r_add_orders():
    return render_template('new_cookie.html')

@app.route('/cookies/add/new', methods = ['POST'])
def f_process_orders():
    data = {
        'name': request.form['name'],
        'cookie_name': request.form['cookie_name'],
        'boxes': request.form['box_count']
    }
    if not Order.validate_order(request.form):
        return redirect('/cookies/add')
    Order.add_order(data)
    return redirect('/cookies')

@app.route('/cookies/edit/<int:order_id>')
def r_edit_order(order_id):
    data = {
        'order_id': order_id
    }
    orders = Order.get_one(data)
    return render_template('edit_cookie.html', orders = orders)

@app.route('/cookies/process/edit', methods = ['POST'])
def f_process_edit():
    data = {
        'order_id': request.form['order_id'],
        'name': request.form['name'],
        'cookie': request.form['cookie_name'],
        'boxes': request.form['box_count']
    }
    if not Order.validate_order(request.form):
        return redirect(url_for('r_edit_order', order_id = request.form['order_id']))
    Order.edit_order(data)
    return redirect('/cookies')