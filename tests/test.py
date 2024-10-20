import pytest
from models.customer import Customer

@pytest.fixture
def customer():
    return Customer

def test_customer(customer):
    customer = Customer("Teams", "P928364989")
    assert customer.get_customer() == customer.customerId


def test_create_customer(customer):
  data = {
     "customerId":  "P928364989",
     "name": "Teams",
     "address": "123 Main St",
     "city": "Anytown",
     "state": "CA",
     "postalCode": "12345",
     "country": "USA",
     "phone": "000000000000",
     "email": "XXXXXXXXXXXXXX",
     "creditLimit": 10000.00
  }
  customer = Customer("Teams", "P928364989")
  assert customer.create_customer(data=data) == "data"