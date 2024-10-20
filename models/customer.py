import json
import os
from datetime import datetime
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

class Customer:
  def __init__(self, companyProfile=None, customerId=None):
    self.companyProfile = companyProfile
    self.customerId = customerId

    dt = datetime.now()
    self.ts = datetime.timestamp(dt)

  def get_customer(self) -> str:
    return self.customerId
    
  def create_customer(self, data):
    if data is not None:
      return data

  def update_customer(self, data) -> str:
    if data is not None:
      return data
    
  def delete_customer(self, customerid) -> str:
    if customerid is not None:
      return customerid