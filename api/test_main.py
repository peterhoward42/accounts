import pytest
from fastapi.testclient import TestClient

import unittest

from main import app
from storage.in_memory_store import retrieve_transactions

client = TestClient(app)
    

def test_happy_path():
    
    # Post a simple two-line csv payload.
    files = {'data': two_line_csv_file}
    
   
    response = client.post("/transactions",files=files)
    
    # Check response is what is expected.
    assert(201 == response.status_code)
    obj = response.json()
    assert(len(obj) == 2)
    second_one = obj[1]
    assert(second_one['amount'] == '40.00')
    assert(second_one['date'] == '2020-07-04')
    assert(second_one['category'] == 'Income')
    assert(second_one['memo'] =='347 Woodrow')
    
    # Check the transactions got stored.
    stored = retrieve_transactions()
    a = 1
        
        
two_line_csv_file = """
    2020-07-01, Expense, 18.77, Fuel§
    2020-07-04, Income, 40.00, 347 Woodrow
"""
      
if __name__ == '__main__':
    unittest.main()