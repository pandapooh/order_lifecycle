import pytest
import json 
from models.customer import Customer

@pytest.fixture
def customer():
    return Customer

def test_customer(customer):
    customer = Customer("Teams", "P928364989")
    customerRequest = customer.get_customer()
    customerId = ""
    customerRequest = json.loads(customerRequest)

    if isinstance(customerRequest, list):
        customerId = customerRequest[0]["customerId"]
    else: 
        customerId = customerRequest["customerId"]

    assert isinstance(customerRequest, list)
    assert customerId == customer.customerId


def test_create_customer(customer):
    data = {
        "companyProfile": "Teams",
        "customerId": "P928364989"
    }

    customer = Customer()
    response = json.loads(customer.create_customer(data))

    assert isinstance(response, dict)
    assert isinstance(response["inserted_ids"], list)