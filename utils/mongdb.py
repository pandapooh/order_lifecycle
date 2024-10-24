
import json
import traceback
from bson import json_util
from pymongo.mongo_client import MongoClient


class MongoDB:
    def __init__(self, db=None, collection=None) -> None:
      self.database = db
      self.collection = collection

      self.connection = "mongodb+srv://medussin:hTt1BFPPbIBjOe7H@pandacluster.kepjh.mongodb.net/?retryWrites=true&w=majority&appName=PandaCluster"
      
    def connection_health_check(self) -> bool:
      try:
        with MongoClient(self.connection) as client:
          client.admin.command('ping')
          print("Pinged your deployment. You successfully connected to MongoDB!")
          return True
      except Exception as e:
        print(e.args)

    def get_document(self, key) -> json:
      try:
        with MongoClient(self.connection) as client:
          db = client[self.database]
          collection = db[self.collection]

          document = list(collection.find(key))
          json_docs = json.dumps(document, default=json_util.default)

          return json_docs
      except Exception as e:
        tr = traceback.format_exc()
        print(tr)
        print(e.args)

    def put_document(self, document) -> dict:
      try:
        with MongoClient(self.connection) as client:
          db = client[self.database]
          collection = db[self.collection]

          result = collection.insert_many(document)

          inserted_ids_dict = {'inserted_ids': [str(oid) for oid in result.inserted_ids]} 

          return inserted_ids_dict
      except Exception as e:
        print(e.args)

    def delete_document(self, **kwargs) -> list:
      try:
        with MongoClient(self.connection) as client:
          db = client[self.database]
          collection = db[self.collection]

          doc = kwargs.get("document")

          if doc is None:
            raise Exception("Document is required")
          elif isinstance(doc, list): 
            result = collection.delete_many(doc)
          else:
            result = collection.delete_one(doc)

          print(result)
          return result.deleted_count
      except Exception as e:
        print(e.args)