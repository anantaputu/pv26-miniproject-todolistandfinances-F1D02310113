from dataclasses import dataclass


@dataclass
class FinanceRecord:
    record_date: str
    record_type: str
    category: str
    amount: float
    payment_method: str
    notes: str
