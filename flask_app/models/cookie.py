#this whole file can be changed depending on what we need to do with the data and how we want our OOP instances to appear.

# import the function that will return an instance of a connection
from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash

class Order:
    def __init__( self , data ):
        self.id = data['id']
        self.name = data['name']
        self.cookie_name = data['cookie_name']
        self.num_of_boxes = data['num_of_boxes']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    # Now we use class methods to query our database
    @classmethod
    def get_all(cls):
        # adjust the "FROM" target to be the required table
        query = "SELECT * FROM orders;"
        # make sure to call the connectToMySQL function with the DB schema you are targeting.
        results = connectToMySQL('cookie_orders_schema').query_db(query)
        orders = []
        for order in results:
            orders.append( cls(order) )
        return orders

    @classmethod
    def add_order(cls, data):
        query = "INSERT INTO orders (name, cookie_name, num_of_boxes) VALUES (%(name)s, %(cookie_name)s, %(boxes)s);"
        return connectToMySQL('cookie_orders_schema').query_db(query, data)

    @classmethod
    def get_one(cls, data):
        query = "SELECT * FROM orders WHERE id = %(order_id)s ;"
        results = connectToMySQL('cookie_orders_schema').query_db(query, data)
        orders = []
        for order in results:
            orders.append(cls(order))
        return orders

    @classmethod
    def edit_order(cls,data):
        query = "UPDATE orders SET name = %(name)s, cookie_name = %(cookie)s, num_of_boxes = %(boxes)s WHERE id = %(order_id)s ;"
        return connectToMySQL('cookie_orders_schema').query_db(query, data)

    @staticmethod
    def validate_order(order):
        is_valid = True
        if len(order['name']) < 2:
            flash('Name must be at least 2 characters long.')
            is_valid = False
        if len(order['cookie_name']) < 2:
            flash('Cookie Name must be at least 2 characters long.')
            is_valid = False
        if len(order['box_count']) < 1:
            flash ('Must have 1 or more boxes to order.')
        return is_valid