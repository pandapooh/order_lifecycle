from flask import jsonify, request, Blueprint
from models.customer import Customer

customer = Blueprint('customer', __name__, template_folder='templates')

'''
  Customer flow
  Get, Create, Update
'''
@customer.route('/customer/<customerid>', methods=['GET'])
def get_customer(customerid):
  print("saca el customer")
  customer = Customer(customerId=customerid)
  resp = customer.get_customer()
  return jsonify(resp)

@customer.route('/customer', methods=['POST'])
def create_customer():
  print("create customer request")
  data = request.get_json()
  customer = Customer()
  resp = customer.create_customer(data=data)
  return jsonify(resp)

@customer.route('/customer/<customerid>', methods=['PATCH'])
def update_customer(customerid):
  print("update customer request")
  data = request.get_json()
  customer = Customer(customerId=customerid)
  resp = customer.update_customer(data=data)
  return jsonify(resp)

@customer.route('/delete/<customerid>', methods=['DELETE'])
def delete_customer(customerid):
  print("delete customer")
  customer = Customer()
  resp = customer.delete_customer(customerid=customerid)
  return jsonify(resp)