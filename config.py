import boto3
import logging
import json 
from botocore.exceptions import ClientError

logger = logging.getLogger(__name__)

class GetSecretWrapper:
    def __init__(self, secretsmanager_client):
        self.client = secretsmanager_client

    def get_secret(self, secret_name):
        try:
            get_secret_value_response = self.client.get_secret_value(
                SecretId=secret_name
            )
            logging.info("Secret retrieved successfully.")
            secretjson = json.loads(get_secret_value_response["SecretString"])
            return secretjson["tomala"]
        except self.client.exceptions.ResourceNotFoundException:
            msg = f"The requested secret {secret_name} was not found."
            logger.info(msg)
            return msg
        except Exception as e:
            logger.error(f"An unknown error occurred: {str(e)}.")
            raise

secret_name = "tomala"
region_name = "us-east-2"

# Create a Secrets Manager client
session = boto3.session.Session()
client = session.client(
    service_name='secretsmanager',
    region_name=region_name
)

wrapper = GetSecretWrapper(client)

print(wrapper.get_secret("tomala"))