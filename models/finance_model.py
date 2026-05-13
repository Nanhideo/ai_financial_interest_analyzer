from pydantic import BaseModel, ConfigDict
from datetime import date
from typing import Optional

class FinanceRequest(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    name: str
    initial_balance: float
    interest_rate: float
    # months is no longer required, we will use end_date
    monthly_contribution: float = 0.0
    start_date: Optional[date] = None 
    end_date: date # This is now required to calculate duration