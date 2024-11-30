
from typing import List
from fastapi import HTTPException
from models.transaction import Transaction, IncomeOrExpense
from models.report import Report
from storage.in_memory_store import store_transactions, retrieve_transactions

async def make_report() -> Report:
    transactions = await retrieve_transactions()
    
    # DRY these two near identical blocks
    income_transactions = [t for t in transactions if t.category == IncomeOrExpense.income]
    amounts = [t.amount for t in income_transactions]
    gross_revenue = sum(amounts)
    
    expense_transactions = [t for t in transactions if t.category == IncomeOrExpense.expense]
    amounts = [t.amount for t in expense_transactions]
    expenses = sum(amounts)
    
    net_revenue = gross_revenue - expenses
    try:
        report = Report(gross_revenue=gross_revenue, expenses=expenses, net_revenue=net_revenue)
    except Exception as err:
        raise HTTPException(500, f'Internal error: failed to parse stored transactions. Details: {str(err)}')
    
    return report