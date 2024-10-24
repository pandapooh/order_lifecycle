import json
import os
from datetime import datetime
from os.path import join, dirname
from dotenv import load_dotenv
from utils.mongdb import MongoDB

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

class Customer:
  def __init__(self, companyProfile=None, customerId=None):
    self.companyProfile = companyProfile
    self.customerId = customerId
    self.db = "Customer"
    self.collection = "customer"

    self.mongo = MongoDB(db=self.db, collection= self.collection)

    dt = datetime.now()
    self.ts = datetime.timestamp(dt)

  def get_customer(self) -> json:
    try:
      key = {}
      if self.customerId is not None:
        key = {
          "customerId": self.customerId
        }
      
      response = self.mongo.get_document(key)
      return response
    except Exception as e:
      print(e.args)
    
  def create_customer(self, data) -> json:
    try:
      if data is not None:
        doc = []

        if isinstance(data, list):
          doc = data
        else:
          doc.append(data)  

        response = self.mongo.put_document(document=doc)
        print(type(response))
        print(response)
        return response
    except Exception as e:
      print(f"Error creating customer {e}")

  def update_customer(self, data) -> str:
    if data is not None:
      return data
    
  def delete_customer(self, customerid) -> str:
    if customerid is not None:
      return customerid