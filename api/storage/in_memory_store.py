from typing import Tuple
from models.transaction import Transaction

module_scope_store: Tuple[Transaction] = []

def store_transactions(transactions: Tuple[Transaction]):
    # Store a read-only copy.
    module_scope_store = tuple(transactions)
    
def retrieve_transactions() -> Tuple[Transaction]:
    # Return a read-only representation. 
    return module_scope_store
