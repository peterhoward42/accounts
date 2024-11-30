from typing import List
from models.transaction import Transaction

module_scope_store: List[Transaction] = []

async def store_transactions(transactions: List[Transaction]):
    module_scope_store.extend(transactions)
    
async def retrieve_transactions() -> List[Transaction]:
    # Return a read-only representation. 
    return tuple(module_scope_store)
