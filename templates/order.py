from flask import jsonify, request, Blueprint
from models.order import Order

ord = Blueprint('order', __name__, template_folder='templates')

'''
  Order flow
  Get, Create, Update, Preview
'''
@ord.route('/order/<customerid>', methods=['GET'])
def get_orders_for_customer(customerid):
  print("get the orders of a customer")
  order = Order(customerId=customerid)
  resp = order.get_order()
  return jsonify(resp)

@ord.route('/order/<customerid>/<orderid>', methods=['GET'])
def order_details(customerid, orderid):
  print("get order details")
  order = Order(customerId=customerid, orderId=orderid)
  resp = order.get_order()
  return jsonify(resp)

@ord.route('/order', methods=['POST'])
def order():
  print("put an order")
  data = request.get_json()
  order = Order()
  resp = order.put_order(params=data)
  return jsonify(resp)

@ord.route('/order/update', methods=['PATCH'])
def update_order():
  print("update order")
  data = request.get_json()
  order = Order()
  resp = order.update_order(params=data)
  return jsonify(resp)