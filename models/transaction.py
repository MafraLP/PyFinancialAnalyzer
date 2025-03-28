# models/transaction.py
from dataclasses import dataclass
from datetime import datetime
from typing import Optional


@dataclass
class Transaction:
    date: datetime
    description: str
    amount: float
    category: Optional[str] = None

    def is_expense(self) -> bool:
        return self.amount < 0

    def is_income(self) -> bool:
        return self.amount > 0

    def absolute_amount(self) -> float:
        return abs(self.amount)