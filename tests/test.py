import pytest
import json 
from models.customer import Customer

@pytest.fixture
def customer():
    return Customer

def test_customer(customer):
    customer = Customer("Teams", "P928364989")

    assert customer.companyProfile == "Teams"


def test_create_customer(customer):
    data = {
        "companyProfile": "Teams",
        "customerId": "P928364989"
    }
    assert isinstance(data, dict)
    assert data["companyProfile"] == "Teams"