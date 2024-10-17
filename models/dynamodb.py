import json 
import os 
import boto3

import boto3.dynamodb
import boto3.dynamodb.conditions
from botocore.exceptions import ClientError

dynamodb = boto3.resource('dynamodb', region_name="us-east-2")

class Dynamo:
    def __init__(self, table:str, partition_key=None, sort_key=None):
        self.table = table
        self.partition_key = partition_key
        self.sort_key = sort_key

        self.table_obj = dynamodb.Table(self.table)

    def get_item(self, value):
        response = self.table_obj.get_item(
            Key={
                self.partition_key : value
            }
        )
        
        return response
    
    def get_conditional_item(self):
        try:
            print(self.partition_key)
            print(self.sort_key)
            print(self.table_obj)

            response = self.table_obj.query(
                    KeyConditionExpression=boto3.dynamodb.conditions.Key('user_id').eq(self.partition_key) &
                    boto3.dynamodb.conditions.Key('customer_id').begins_with(self.sort_key)
                )

            print("algo o nada")
            print(response)

            return response["Items"]
        except ClientError as err:
            print("client exception")
            print(err.response["Error"]["Code"], err.response["Error"]["Message"])
        except Exception as exp:
            print("general exception")
            print(exp.args)
  
    def get_all_items(self):
        try:
            response = self.table_obj.scan()
            if response:
                return response
            else:
                return "false"
        except ClientError as err:
            print(err.response["Error"]["Code"], err.response["Error"]["Message"])
            return err.response["Error"]["Message"]
    
    def put_item(self, item):
        try:
            self.table_obj.put_item(
                Item=item
            )  
            return "true"
        except ClientError as err:
            print(err.response["Error"]["Code"],err.response["Error"]["Message"])
            return "false"
        except Exception as e:
            print(e.args)
            return "false"

    def update_item(self, value, item, expr, attrib):
        print("si entra aca ")
        try:
            key_item = {
                self.partition_key : value
            }
            
            if self.partition_key and self.sort_key:
                key_item = {
                    self.partition_key : value["user_id"],
                    self.sort_key : value["customer_id"]
                } 

            response = self.table_obj.update_item(
                Key=key_item,
                UpdateExpression=expr,
                ExpressionAttributeValues=item,
                ExpressionAttributeNames=attrib
            )

            print("respnse de la base")
            print(response)

            return response
        except ClientError as err:
            print(err.response["Error"]["Code"], err.response["Error"]["Message"])
            return err.response["Error"]["Message"]
        except Exception as e:
            print(e.args)
            return "false"