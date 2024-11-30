
from typing import List
from fastapi import HTTPException
from models.transaction import Transaction, IncomeOrExpense
from models.report import Report
from storage.in_memory_store import store_transactions, retrieve_transactions
from decimal import Decimal


async def make_report() -> Report:
    transactions = await retrieve_transactions()
    
    if len(transactions) == 0:
        raise HTTPException(status_code=400, detail='Cannot generate report because there are no stored transactions - use the /transactions endpoint to put some in.')
    
    gross_revenue = await sum_transactions_of_type(transactions, IncomeOrExpense.income)
    expenses = await sum_transactions_of_type(transactions, IncomeOrExpense.expense)
    
    net_revenue = gross_revenue - expenses
    try:
        report = Report(gross_revenue=gross_revenue, expenses=expenses, net_revenue=net_revenue)
    except Exception as err:
        raise HTTPException(500, f'Internal error: failed to parse stored transactions. Details: {str(err)}')
    
    return report

async def sum_transactions_of_type(all_transactions: List[Transaction], category: IncomeOrExpense) -> Decimal:
    transactions = [t for t in all_transactions if t.category == category]
    amounts = [t.amount for t in transactions]
    return sum(amounts)