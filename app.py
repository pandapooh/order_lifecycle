import json 
import os 
import boto3
from flask_cors import CORS
from flask import Flask, jsonify, request
from templates.customer import customer
from templates.order import ord

app = Flask(__name__)

@app.route('/health-check', methods=['GET'])
def test():
  return jsonify("Health check, looking good!!!")

#  Customer flow
app.register_blueprint(customer)

#  Order flow
app.register_blueprint(ord)

CORS(app, resources={r"/*": {"origins": "*"}})

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=5000, debug=True)