import json
import os
import boto3 
import pandas as pd
from datetime import datetime
from os.path import join, dirname
from dotenv import load_dotenv
from pydantic import BaseModel

from botocore.exceptions import ClientError
from models.dynamodb import Dynamo

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)
class Order:
  def __init__(self,  companyProfile=None, customerId=None, orderId=None):
    self.companyProfile = companyProfile
    self.customerId = customerId
    self.orderId = orderId

    dt = datetime.now()
    self.ts = datetime.timestamp(dt)

  def get_order(self) -> str:
    if self.customerId is not None:
      return self.customerId
      
  def put_order(self, params) -> str:
    if self.customerId is not None:
      return self.customerId
 
  def update_order(self, params) -> str:
    return "order updated"
    